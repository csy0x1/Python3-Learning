import sqlite3,datetime,time,os
conn=sqlite3.connect('C://Users//Desktop-P21//codeDB.db') #连接到数据库
print('connected')
c=conn.cursor()
filename='G:/result.txt' #指定摄像头识别结果输出文件目录
cursor = c.execute("SELECT amount,value from CODE where ID=0") #链接数据库，获取最新的ID编号
amount=0    #数量
iid=0       #数据库ID编号

for row in cursor:  #读取最后一次存入数据库的内容
    cid=row[0]
    temp=row[1]

def CheckDuplicate():
    cdcom="select * from code where value='%s' AND ID!=0"%(content)
    items = c.execute(cdcom)
    for item in items:
        eid=item[0]      #获取已存在内容的ID
        evalue=item[1]   #将已在数据库中的内容赋值给变量evalue
        eamount=item[2] #获取已存在内容的数量
        if content==evalue:
            global amount,iid
            amount=eamount
            iid=eid
            return True
        else:
            return False

def removefile():
    if os.path.exists(filename):
        os.remove(filename)
    else:
        pass

while True:
    try:
        date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename) as f:
            #date="%s/%s/%s %s-%s-%s"%(i.year,i.month,i.day,i.hour,i.minute,i.second) #获取当前时间
            content=f.read()
        #if content!=temp:
        if(CheckDuplicate()):   #数据库中存在此内容
            print("duplicated")
            amount+=1
            sqlcom="update code set amount=%s,DATE='%s' where ID='%s'"%(amount,date,iid)
            c.execute(sqlcom)
            conn.commit()
            temp=content
            sqlcom="update code set VALUE = '%s',AMOUNT=%s where ID=0"%(temp,cid)  #SQL指令
            c.execute(sqlcom)
            conn.commit()
            removefile()
        else:
            print(content)
            sqlcom="INSERT INTO CODE(ID,VALUE,AMOUNT,DATE) VALUES('%s','%s',1,'%s')"%(cid,content,date) #SQL指令
            c.execute(sqlcom)
            conn.commit()
            cid+=1  #编号+1
            temp=content
            sqlcom="update code set value = '%s',amount=%s where ID=0"%(temp,cid)  #SQL指令
            c.execute(sqlcom)
            conn.commit()
            removefile()
        time.sleep(3)
    except (FileNotFoundError,OSError):
        pass

