import yaml
import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

homedir = os.path.expanduser('~')
filename = ".cred"
yamlfilename = ".netmiko.yml"

credfile = homedir + "/" + filename
yamlfile = homedir + "/" + yamlfilename

with open(credfile) as f:
    cred = f.read()

username, password = cred.split(":")
username = username.strip()
password = password.strip()

with open(yamlfile) as yf:
    yamldevices = yaml.load(yf)

#pprint(yamldevices)
#print(type(yamldevices["nxos"]))

#userinput = input("Enter hostname or groupname: ")
userinput = "cisco4"

def conDevFunc(device):
    conDev = ConnectHandler(session_log="my_session.txt", **yamldevices[device])
    print(conDev.find_prompt())
    output = conDev.send_command("show ip int brief")
    output = "test"
    return output

if userinput in yamldevices:
    #pprint(yamldevices[userinput])
    if type(yamldevices[userinput]) is list:
        for udevice in yamldevices[userinput]:
            output = conDevFunc(udevice)
    else:
        output = conDevFunc(userinput)

print(output)

with open("router_output.txt", "w") as outf:
    outf.write(output)



exit()
