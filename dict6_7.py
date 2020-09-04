people1={
    'first_name':'Joey',
    'last_name':'Pu',
    'age':'21',
    'city':'ctu',
}

people2={
    'first_name':'a',
    'last_name':'b',
    'age':'12',
    'city':'can',
}

people3={
    'first_name':'c',
    'last_name':'d',
    'age':'24',
    'city':'pek',
}

people=[people1,people2,people3]

for i in people:
    print(i)

#6_9
favplc1=['a','b','c']
favplc2=['d','e','f']
favplc3=['g','h']

favorite_places={'ppl1':favplc1,'ppl2':favplc2,'ppl3':favplc3}

for name,plc in favorite_places.items():
    print('\n'+name+"'s favourite places is:")
    for place in plc:
        print(place)

#6_11
cities={
    'city1':{
        'country':'a',
        'population':'8M',
        'fact':'a',
    },

    'city2':{
        'country':'b',
        'population':'6M',
        'fact':'b',
    },

    'city3':{
        'country':'c',
        'population':'16M',
        'fact':'c',
        },
}




for name,info in cities.items():
    print('\n'+name+"'s info in below: ")
    for key,value in info.items():
        print('\t'+key+': '+value)