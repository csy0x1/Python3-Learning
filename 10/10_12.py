import json
filename='10/number.json'
try:
    with open(filename) as f_obj:
        number=json.load(f_obj)
except FileNotFoundError:
    number=input('please input a number: ')
    with open(filename,'w') as f_obj:
        json.dump(number,f_obj)
else:
    print(number)
