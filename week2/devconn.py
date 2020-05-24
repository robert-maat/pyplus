#!/
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

pprint(yamldevices["nxos"])


for ydevice in yamldevices["nxos"]:
    conDev = ConnectHandler(**yamldevices[ydevice])
    print(conDev.find_prompt())

exit()

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": username, 
    "password": password, 
    "port": "22",
}

nxos2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": username, 
    "password": password, 
    "port": "22",
}

devices = [nxos1, nxos2]

for device in devices:
    conDev = ConnectHandler(**device)
    print(conDev.find_prompt())


