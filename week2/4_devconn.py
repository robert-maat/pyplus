import yaml
import os  # use to get local home directory
from netmiko import ConnectHandler # use to connect to devices
from getpass import getpass # use to enter passoword
from pprint import pprint # used to print list/dict. in readable maner
from datetime import datetime # get current time


# get file and directory paths
homedir = os.path.expanduser('~')
filename = ".cred"
yamlfilename = ".netmiko.yml"

# exact filename and place
credfile = homedir + "/" + filename
yamlfile = homedir + "/" + yamlfilename

# read creditfile to get user and password
with open(credfile) as f:
    cred = f.read()

username, password = cred.split(":")
username = username.strip()
password = password.strip()

# read all devices and device groups from file
with open(yamlfile) as yf:
    yamldevices = yaml.load(yf)

# ask user for input of devicename/group
userinput = input("Enter hostname or groupname: ")

commands = "ip name-server 1.1.1.1\n"
commands += "ip name-server 1.0.0.1\n"
commands += "ip domain-lookup\n"


listcommands = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]

print("commands in one string")
print(commands)

print("commands in one list")
print(listcommands)

def conDevFunc(device):
    conDev = ConnectHandler(session_log="my_session.txt", fast_cli=True, **yamldevices[device])
    print(conDev.find_prompt())
    output = conDev.send_config_set(listcommands)
    output += "\n"
    conDev.disconnect()
    return output

# check if input excists and if its an group or single device is entered by user
if userinput in yamldevices:
    #pprint(yamldevices[userinput])
    if type(yamldevices[userinput]) is list:
        output = ""
        for udevice in yamldevices[userinput]:
            output += conDevFunc(udevice)
    else:
        output = conDevFunc(userinput)
else:
    print("incorrect device/group is given. Use one of the following options:")
    for key in yamldevices:
        print(key)
    exit()


pprint(output)
print(output)

#with open("router_output.txt", "w") as outf:
#    outf.write(output)



exit()
