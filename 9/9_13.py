from collections import OrderedDict

dict_test=OrderedDict()

dict_test['test1']='1'
dict_test['test2']='2'
dict_test['test3']='3'
dict_test['test4']='4'

for key,value in dict_test.items():
    print(key+' = '+value)