import sqlite3,datetime,time
conn=sqlite3.connect('C://Users//Desktop-P21//codeDB.db') #连接到数据库
print('connected')
c=conn.cursor()
filename='G:/result.txt' #指定摄像头识别结果输出文件目录
cursor = c.execute("SELECT amount,value from CODE where ID=0") #链接数据库，获取最新的ID编号
for row in cursor:
    cid=row[0]
    temp=row[1]
while True:
    try:
        with open(filename) as f:
            date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #date="%s/%s/%s %s-%s-%s"%(i.year,i.month,i.day,i.hour,i.minute,i.second) #获取当前时间
            content=f.read()
            if content!=temp:
                print(content)
                sqlcom="INSERT INTO CODE(ID,VALUE,AMOUNT,DATE) VALUES('%s','%s',1,'%s')"%(cid,content,date) #SQL指令
                c.execute(sqlcom)
                cid+=1  #编号+1
                temp=content
                sqlcom="update code set value = '%s',amount=%s where ID=0;"%(temp,cid)  #SQL指令
                c.execute(sqlcom)
                conn.commit()
                time.sleep(3)
    except (FileNotFoundError,OSError):
        pass