from pprint import pprint
import re

with open("1_arptable.txt") as f:
    arpt = f.read()

pprint (arpt)
print("start converting to list")

# create list of string
arpt_list = arpt.split("\n")
#pprint(arpt_list)
del arpt_list[-1]
pprint(arpt_list)

# get header and convert to keys
header = arpt_list.pop(0)
keys = header.split()

#pprint(keys)
del keys[4]
pprint(keys)

# convert each line to dict
arpt_listdict = []
for line in arpt_list:
    values = line.split()
    #pprint(values)
    arpt_dict = {}
    i = 0
    for key in keys:
        #print(key + " en "  + values[i])
        arpt_dict.update( {key : values[i]} ) 
        i += 1
    #pprint(arpt_dict)
    arpt_listdict.append(arpt_dict)
pprint(arpt_listdict)
