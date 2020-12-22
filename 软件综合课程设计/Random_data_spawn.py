'''
自动随机生成20个信息并插入数据库
'''

import random
import string
from database import Insert_Info

Teacher={}

for i in range(20):
    Teacher['工号']=ran_str = ''.join(random.sample(string.digits, 8))
    Teacher['姓名']=ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    Teacher['年龄']=ran_str = ''.join(random.sample(string.digits, 2))
    Teacher['职称']=ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    Teacher['系名']=ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    Teacher['手机号码']=ran_str = ''.join(random.sample(string.digits, 11))
    Teacher['联系地址']=ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    Insert_Info(Teacher)