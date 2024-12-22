capitals = {
    'AK':'Juneau',
    'AL':'Montgomery',
    'AR':'Little Rock',
    'AZ':'Phoenix',
    'CA':'Sacramento',
    'CO':'Denver',
}

print()
print(capitals['AK'])
print()

capitals['US'] = 'Washington DC'

print() 
print(capitals['US'])
print() 

del capitals['AK']

for key in capitals:
    print(key)
