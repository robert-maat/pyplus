

from pprint import pprint

"""
cisco3:
  device_type: cisco_ios
  host: cisco3.lasthop.io
cisco4:
  device_type: cisco_ios
  host: cisco4.lasthop.io
arista1:
  device_type: arista_eos
  host: arista1.lasthop.io
  global_delay_factor: 1
arista2:
  device_type: arista_eos
  host: arista2.lasthop.io
  global_delay_factor: 1
arista3:
  device_type: arista_eos
  host: arista3.lasthop.io
  global_delay_factor: 1
arista4:
  device_type: arista_eos
  host: arista4.lasthop.io
  global_delay_factor: 1
"""


devlist = []
cisco3 = {}
cisco3.update( {"host": "cisco3.lasthop.io", "device_type": "cisco_ios", "username": "tester", "password": "cisco123"} )
devlist.append(cisco3)

cisco4 = {}
cisco4.update( {"host": "cisco4.lasthop.io", "device_type": "cisco_ios", "username": "tester", "password": "cisco123"} )
devlist.append(cisco4)

arista3 = {}
arista3.update( {"host": "arista3.lasthop.io", "device_type": "arista_eos", "username": "tester", "password": "cisco123"} )
devlist.append(arista3)


arista4 = {}
arista4.update( {"host": "arista4.lasthop.io", "device_type": "arista_eos", "username": "tester", "password": "cisco123"} )
devlist.append(arista4)


pprint(devlist)


