import json
filename='10/number.json'
with open(filename) as f_obj:
    number=json.load(f_obj)
print('Your favourite number is: '+number)