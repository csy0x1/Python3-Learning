import sqlite3
conn=sqlite3.connect('C://Users//Desktop-P21//codeDB.db')
print('connected')

c=conn.cursor()
c.execute('''CREATE TABLE CODE
        (ID INT PRIMARY KEY NOT NULL,
        VALUE            TEXT    NOT NULL,
        AMOUNT             INT     NOT NULL,
        DATE         TEXT);''')
print('successed')
#c.execute("INSERT INTO TEST(ID,NAME,AGE,ADDRESS,SALARY)\ VALUES(1,'paul',32,'california',20000.00)")
conn.commit()
conn.close()