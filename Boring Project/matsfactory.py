import os,json
def factory():
    os.system('cls')
    print('材料厂')
    filename='stats.json'
    while True:
        inst=input('输入sellmats来出售材料(1:75): ')
        if inst == 'sellmats':
            sellmats()
            break
        else:
            print('请输入正确的指令')

    with open(filename) as f_obj:
        stats=json.load(f_obj)
        stats['mats']=str(int(stats['mats'])+25)


def sellmats():
    filename='stats.json'
    os.system('cls')
    with open(filename) as f_obj:
        stats=json.load(f_obj)
        print('你现在拥有: '+stats['mats']+' 个材料')
        while True:
            sell=input('请输入你要出售的材料数: ')
            if int(sell) > int(stats['mats']):
                print('你没有那么多材料')
            elif int(sell) <=0:
                print('出售材料个数必须大于0')
            else:
                earn=int(sell)*75
                stats['mats']=str(int(stats['mats'])-int(sell))
                stats['money']=str(earn)
                json_str=json.dumps(stats,indent=4)
                with open(filename,'w') as f_obj:
                    f_obj.write(json_str)
                    os.system('cls')
                    print('材料出售成功! ')
                break