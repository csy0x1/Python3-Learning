#8_12
def sandwich(*addings):
    print('your adding are: ')
    for adding in addings:
        print('- '+adding)

sandwich('1')
sandwich('2','5','9')
sandwich('1','5','7','0')
sandwich()

#8_13
def build_profile(first,last,**user_info):
    profile={}
    profile['first_name']=first.title()
    profile['last_name']=last.title()
    for key,value in user_info.items():
        profile[key]=value
    print(profile)

build_profile('first','last',locations='test')
build_profile('nick','wilde')
build_profile('test','loveu',testitem='test',testitem2='2')

#8_14
def car_info(manufactor,model,**more_car_info):
    info={}
    info['manufactor']=manufactor
    info['model']=model
    for key,value in more_car_info.items():
        info[key]=value
    print(info)
car_info('Mitsubishi','Lancer Evolution IX',Color='White',Modified='True')