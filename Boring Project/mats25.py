import os,json
def a_25_mats():
    os.system('cls')
    print('25材料点')
    inst=''
    filename='stats.json'
    stats={'mats':'0','money':'0'}
    while True:
        inst=input('输入smugglemats来领取材料: ')
        if inst == 'smugglemats':
            break
        else:
            print('请输入正确的指令')

    with open(filename) as f_obj:
        stats=json.load(f_obj)
        stats['mats']=str(int(stats['mats'])+25)

    json_str=json.dumps(stats,indent=4)
    with open(filename,'w') as f_obj:
        f_obj.write(json_str)
        os.system('cls')
        print('材料领取成功! ')