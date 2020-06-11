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

#pprint(yamldevices)
#print(type(yamldevices["nxos"]))

print(datetime.now())
now = datetime.now()

# get userinput which devices to connect
userinput = input("Enter hostname or groupname: ")
#userinput = "cisco4"

def conDevFunc(device):
    conDev = ConnectHandler(session_log="my_session.txt", **yamldevices[device])
    print(conDev.find_prompt())
    #now = datetime.now()
    #output = "Current starttime is : " + str(now) + "\n"
    output = conDev.send_command("show version", use_textfsm=True)
    output += conDev.send_command("show lldp neighbors", use_textfsm=True)
    #now = datetime.now()
    #output += "Current finishtime is : " + str(now) +"\n"
    conDev.disconnect()
    return output

# check if input excists and if its an group or single device is entered by user
if userinput in yamldevices:
    #pprint(yamldevices[userinput])
    if type(yamldevices[userinput]) is list:
        for udevice in yamldevices[userinput]:
            output = conDevFunc(udevice)
    else:
        output = conDevFunc(userinput)
else:
    print("incorrect device/group is given. Use one of the following options:")
    for key in yamldevices:
        print(key)
    exit()


pprint(output)

print("type of output is: " + str(type(output)))

print("lldp neighbor interface number is : " + str(output[1].get('neighbor_interface')))

#with open("router_output.txt", "w") as outf:
#    outf.write(output)



exit()
