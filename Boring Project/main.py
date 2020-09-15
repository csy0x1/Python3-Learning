from mats25 import a_25_mats
from matsfactory import factory
import os
def main_menu():
    os.system('cls')
    while True:
        print('©2020 csy_x All rights reserved. \n')
        print('地点列表: ')
        print('1. 25材料点')
        print('2. 材料厂')
        tele=input('请输入前往地点编号: ')
        if tele == '1':
            a_25_mats()
        elif tele=='2':
            factory()
        else:
            print('地点不存在')

main_menu()