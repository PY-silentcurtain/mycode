import requests
from bs4 import BeautifulSoup
import bs4
import xlwt

def getHTMLText(url):  #抓取网页
    try:
        r = requests.get(url, timeout = 30)  #设置超时时间为30秒
        r.raise_for_status()  #异常情况
        r.encoding = r.apparent_encoding  #替换编码
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):  #提取关键信息添加到列表(核心功能)
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:   #tr的子标签里可能含有字符串，影响我们抓取下一所大学的信息
        if isinstance(tr, bs4.element.Tag):  #我们过滤掉非标签信息的其他信息
            tds = tr('td')  #将所有的td标签存为新的tds列表
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
            #抓取标签之间的内容，这一步我们可以控制想要抓取的信息

def printUnivList(ulist, num):
    workbook = xlwt.Workbook()
    #创建工作表
    # 创建工作表worksheet,填入表名
    worksheet = workbook.add_sheet('中国排名爬取')
    h=0
    #print("{:^10}\t\t{:^6}\t\t{:^10}\t\t{:^10}".format("排名","学校名称","省份","总分"))
    for i in range (num):
        u = ulist[i]
        print("{:^10}\t\t{:^6}\t\t{:^10}\t\t{:^10}".format(u[0], u[1], u[2], u[3]))
    
        # 在表中写入相应的数据
        worksheet.write(h, 0, u[0])
        worksheet.write(h, 1, u[1])
        worksheet.write(h, 2, u[2])
        worksheet.write(h, 3, u[3])
        h=h+1
    # 保存表
    workbook.save('hello2.xls')
               
def main():
    uinfo = []
    url =  'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 310)#想打印多少自己选的大学
main()