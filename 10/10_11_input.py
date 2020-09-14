import json
number=input('please input a number: ')
filename='10/number.json'
with open(filename,'w') as f_obj:
    json.dump(number,f_obj)