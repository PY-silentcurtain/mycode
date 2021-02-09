#输入某年某月某日，判断这一天是这一年的第几天？


def outter(func):
    def inner():
        year = int(input("请输入一个年份:"))
        # global year
        if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
            print("%d是闰年"%year)
            dict1[2]=29
            func()
        else:
            print("%d是平年"%year)
            func()
    return inner

dict1 ={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:30,9:31,10:31,11:30,12:31}

def f():
    ymd2 = input("输入年-月-日[year-month-day]:")
    ymd1 =ymd2.split('-')
    day =0
    for x in range(1,int(ymd1[1])):
        day += dict1[x]
    Day = day+int(ymd1[2])
    print("这一天是这一年的第%d天"%Day)

f()