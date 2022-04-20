## Main page

from tkinter import *
from comis import add_comm
from drop_down import *
from add_emp import add_emp
from delete import del_emp

class main:
    def __init__(self,root):
        self.root=root
        self.f=Frame(root.title("Main Page"),height=600,width=600,bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()
    
        self.b1=Button(text='Add Employees',fg='white',bg='dark red',width=20,height=2,font=('Calibri',15),command=lambda: self.buttonclick(1))
        self.b2=Button(text='Calculate Commission',fg='white',bg='dark red',width=20,height=2,font=('Calibri',15),command=lambda: self.buttonclick(0))
        self.b3=Button(text='Payout',fg='white',bg='dark red',width=20,height=2,font=('Calibri',15),command=lambda: self.buttonclick(2))

        self.b1.place(x=200,y=150)
        self.b2.place(x=200,y=250)
        self.b3.place(x=200,y=350)

    def getValue(self):
            self.choice = self.clicked.get()  

    def buttonclick(self,num):
        if(num==1):
            self.root.destroy()
            add_emp()

        if(num==0):
            self.root.destroy()
            add_comm()
        if(num==2):
            self.root.destroy()
            del_emp()
        else:
            return

def mnpg():
    root=Tk()

    mb=main(root)

    root.mainloop()
        