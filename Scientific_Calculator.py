from tkinter import Tk
from tkinter import StringVar,Entry,Button
import math

class calculator:
    def __init__(self):
        window=Tk()
        window.title('基于TK的科学计算器')
        window.configure(background="white")
        self.string=StringVar()
        entry=Entry(window,textvariable=self.string,)
        entry.grid(row=0,column=0,columnspan=6)
        entry.configure(background="white")
        entry.focus()
    
        values=["C","DEL","(",")","%","gcd",
                "sin","sqrt","e","pow","/","radians",
                "cos","7","8","9","*","degrees",
                "tan","4","5","6","-","ceil",
                "pi","1","2","3","+","hypot",
                "log",",","0",".","="]
        
        text=1
        i=0
        row=1
        col=0
        for txt in values:
            padx=10
            pady=10
            if(i==6):
                row=2
                col=0
            if(i==12):
                row=3
                col=0
            if(i==18):
                row=4
                col=0
            if(i==24):
                row=5
                col=0
            if(i==30):
                row=6
                col=0
            if(txt=='='):
                btn=Button(window,height=2,width=4,padx=50,pady=pady,text=txt,command=lambda txt=txt:self.equals())
                btn.grid(row=row,column=col,columnspan=3,padx=2,pady=2)
                btn.configure(background="yellow")

            elif(txt=='DEL'):
                btn=Button(window,height=2,width=4,padx=padx,pady=pady, text=txt ,command=lambda txt=txt:self.delete())
                btn.grid(row=row,column=col,padx=1,pady=1)
                btn.configure(background="grey")
            elif(txt=='C'):
                btn=Button(window,height=2,width=4,padx=padx,pady=pady,text=txt,command=lambda txt=txt:self.clearall())
                btn.grid(row=row,column=col,padx=1,pady=1)
                btn.configure(background="red")
            else:
                btn=Button(window,height=2,width=4,padx=padx,pady=pady,text=txt ,command=lambda txt=txt:self.addChar(txt))
                btn.grid(row=row,column=col,padx=1,pady=1)
                btn.configure(background="white")

            col=col+1
            i=i+1
        window.mainloop()
        

    def clearall(self):
        self.string.set("")

    def equals(self):
        result=""

        try:
            result=eval(self.string.get())
            self.string.set(result)
        except:
            result="无效输入"
        self.string.set(result)
        
    def addChar(self,char):
        i = ['log','sqrt','pi','sin','cos','tan','e',"gcd","radians","degrees","ceil","hypot"]
        if char in i:
            self.string.set(self.string.get()+'math.'+(str(char)))
        else:
            self.string.set(self.string.get()+(str(char)))
        
    def delete(self):
        self.string.set(self.string.get()[0:-1])
           
calculator()
