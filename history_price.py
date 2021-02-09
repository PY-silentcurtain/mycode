import tkinter
import requests
from bs4 import BeautifulSoup


def getAnswer():
    url = 'http://www.lsjgcx.com/'
    input_ = url_entry.get()
    print(url)
    print(input_)
    url_ = "http://p.zwjhl.com/price.aspx?url=" + input_
    print(url_)
    response = requests.get(url_)
    print(response.encoding)
    html = response.content.decode("gb2312")
    soup = BeautifulSoup(html, 'html.parser')
    ans = soup.findAll(name="div", attrs={"class": "bigwidth"})

    for x in soup.find_all('h1'):
        print(x)
        name_ = str(x).replace('<h1 style="color: #333333; font-size: 16px; margin: 10px; text-align: center; font-weight: bold;">',"").replace("</h1>","")
        a.set(name_)

    answ = ""
    for i in ans:
        answ = str(i.find_all('span'))
        answ = answ.replace('[<span style="color: #333; font-size: 14px;">',"")
        answ = answ.replace('<font style="font-size:12px;">',"")
        answ = answ.replace('<font style="font-size: 12px;">',"")
        answ = answ.replace('<font class="bigwordprice">',"")
        answ = answ.replace('<b>',"").replace("</b>","").replace(" ","").replace(" ","").replace("</font>","").replace("</span>","").replace("[","").replace("]","")
        print(answ)
    if answ == "":
        v.set("查询无结果")
    else:
        v.set(answ)

if __name__ == '__main__':
    startUrl = 'http://www.lsjgcx.com/'

    root = tkinter.Tk()
    root.title('获取历史价格')
    root.geometry('550x360+400+200')  # 指定窗口大小，和显示的偏移量,在屏幕中显示的位置

    url_entry = tkinter.Entry(root, font=('微软雅黑', 20))
    url_entry.grid(row=0, column=1, columnspan=6, pady=5)

    tkinter.Button(root, text='获取历史价格', font=('微软雅黑', 15), width='15', height='1', command=getAnswer).grid(row=3, column=1, columnspan=5, pady=5)

    v = tkinter.StringVar()
    w = tkinter.Label(root, textvariable=v)
    w.grid()

    a = tkinter.StringVar()
    b = tkinter.Label(root, textvariable=a)
    b.grid()

    root.mainloop()  # 窗口持久化