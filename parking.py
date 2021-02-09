#先创建数据库
import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")
c = conn.cursor()
#INTEGER PRIMARY KEY AUTOINCREMENT主键自增
c.execute('''CREATE TABLE PARKING
       (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
       NAME           TEXT     NOT NULL,
       NUMBER         TEXT     NOT NULL);''')
print("表创建成功！")
conn.commit()

#----------------------分割线---------------------------------

#下面是代码部分的处理

import sqlite3
#打开数据库文件
conn = sqlite3.connect('test.db')
print("Opened database successfully")
c = conn.cursor()
#查询
def park_1():
    #i = '豫F-x1234'
    qw = []
    cursor = c.execute("SELECT  number from PARKING")
    for row in cursor:
        qw.append(row[0])
    
    h = input('车牌号格式xx-xxxxx:''\n')
    if h in qw:
        print("尊敬的业主您好，欢迎回家.")
    else:
        print("抱歉，您不是业主，禁止入内！")
#插入  
def insert_1():
    j = input('请输入您的名字：')
    k = input('请输入您的车牌号：')
    print('添加成功！')

    c.execute("INSERT INTO PARKING (NAME,NUMBER) \
              VALUES ('%s','%s')" % (j,k))
    conn.commit()
#列出 
def select_1():
    cursor = c.execute("SELECT id, name, number from PARKING")
    for row in cursor:
       print("ID = ", row[0])
       print("NAME = ", row[1])
       print("NUMBER = ", row[2],'\n')
#删除
def delete_1():
    m = input('请输入您要删除的id：')
    c.execute("DELETE from PARKING where ID=('%s')" % (m))
    conn.commit()
    print ("删除成功！删除的行总数 :", conn.total_changes )

def drop_1():
    cursor = c.execute("DROP TABLE PARKING")
    conn.commit()
    print("删库成功，抓紧跑路！")
    
def main():
    print('='*30)
    print('您好，欢迎使用停车场管理系统。')
    print('1.添加车辆')
    print('2.查找车辆')
    print('3.删除车辆')
    print('4.列出车辆')
    print('5.删库跑路')
    print('6.退出系统')
    print('='*30)

    while True:
        option = input("请输入选项：")

        if option == '1':
            insert_1()
        elif option == '2':
            park_1()
        elif option == '3':
            delete_1()
        elif option == '4':	
            select_1()
        elif option == '5':
            drop_1()
        elif option == '6':	
            print('您已退出系统。')
            break
        else:
            print("请输入正确的选项")
main()
conn.close()