#8_6
def city_country(name,country):
    info=name.title()+','+country.title()
    return info

print(city_country('GuangZhou','china'))
print(city_country('rome','italy'))
print(city_country('London','UK'))

#8_7
def make_album(singer,albumname,snum=''):
    album={'singer':singer,'albumname':albumname}
    if snum:
        album['numofsong']=snum
    return album
print(make_album('singer1','album1','3'))
print(make_album('singer2','album2','5'))
print(make_album('singer3','album3'))

#8_8
while True:
    singer=input('singer(type q to exit): ')
    if singer == 'q':
        break
    albumname=input('albumname(type q to exit): ')
    if albumname == 'q':
        break
    snum=input('numofsong(type q to exit): ')
    if snum == 'q':
        break
    print(make_album(singer,albumname,snum))