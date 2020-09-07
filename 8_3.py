#8_3
def make_shirt(size,text):
    print('your size is: '+size)
    print('your text is: '+text)
make_shirt(text='Make America Great Again',size='L')

#8_4
print('\n')
def make_shirt2(size,text='I love Python'):
    print('your size is: '+size)
    print('your text is: '+text)
make_shirt2(size='L')
make_shirt2('M')
make_shirt2('S','I love C++')

#8_5
print('\n')
def describe_city(name,country='China'):
    print(name+' is in '+country)
describe_city('Chengdu')
describe_city('Guangzhou')
describe_city('Reykjavik','Iceland')