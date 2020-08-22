invitations=['PlayerBotPro','Dark1pa','Stan']
for name in invitations:
    message=name+' Come to play'
    print(message)
dead='PlayerBotPro'
invitations.remove(dead)
message=dead+' is Dead, so he is not coming on'
print(message)
newppl='enevv'
invitations.append(newppl)
for name in invitations:
    message=name+' Come to play'
    print(message)
print('I found a larger table')
invitations.insert(0,'YnWay')
lens=int((len(invitations)/2))
invitations.insert(lens,'2142')
invitations.append('hr')
for name in invitations:
    message=name+' Come to play'
    print(message)
print('due to larger table is unavailable now, I can only invite two guests')
while(len(invitations)>2):
        guest=invitations.pop(0)
        print('sorry '+guest)
for name in invitations:
    message=name+' Come to play'
    print(message)

del invitations[0]
del invitations[0]
print(invitations)