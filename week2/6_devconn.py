from netmiko import ConnectHandler
from getpass import getpass
import time

password = getpass()
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}


netconnect = ConnectHandler(**device)
print(netconnect.find_prompt())
netconnect.config_mode()
print(netconnect.find_prompt())
netconnect.exit_config_mode()
print(netconnect.find_prompt())
netconnect.write_channel("disable\n")
time.sleep(2)
print(netconnect.read_channel())
netconnect.enable()
print(netconnect.find_prompt())




netconnect.disconnect()

