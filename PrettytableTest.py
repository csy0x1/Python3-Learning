import sqlite3
import prettytable as pt
conn=sqlite3.connect('C://Users//Desktop-P21//codeDB.db')
print('connected')
tb=pt.PrettyTable()
tb.field_names={"ID","Value","Amount","Date"}
c=conn.cursor()
#sqlcom1="header on"
#sqlcom2="mode column"
sqlcom3="select * from code where ID!=0"
#c.execute(sqlcom1)
#c.execute(sqlcom2)
i=c.execute(sqlcom3)
for j in i:
    tb.add_row(j)
print(tb)
with open ("test.txt","w") as f:
    f.write(str(tb))
print('successed')
#c.execute("INSERT INTO TEST(ID,NAME,AGE,ADDRESS,SALARY)\ VALUES(1,'paul',32,'california',20000.00)")
conn.commit()
conn.close()