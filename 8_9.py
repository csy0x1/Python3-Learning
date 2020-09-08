#8_9
magicians=['a','b','c','d','e']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

show_magicians(magicians)

#8_10
def make_great(magicians):
    i=0
    for i in range(len(magicians)):
        temp=magicians.pop()+' the Great'
        magicians.insert(0,temp)
    print(magicians)

#make_great(magicians)
#show_magicians(magicians)

#8_11
make_great(magicians[:])
show_magicians(magicians)