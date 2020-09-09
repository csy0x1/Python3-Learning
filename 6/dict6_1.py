people={
    'first_name':'Joey',
    'last_name':'Pu',
    'age':'21',
    'city':'ctu',
}

print(people['first_name']+ '\t' +
    people['last_name']+'\t' +
    people['age']+'\t' +
    people['city']
)

peonum={
    'a':'1',
    'b':'2',
    'c':'3',
    'd':'4',
    'e':'5',
}
for i in peonum:
    for j in peonum[i]:
        print(i+"'s num is "+j)

for k,v in peonum.items():
    print('key: '+k+' value: '+v)