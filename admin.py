## Admin Login in page

from tkinter import*
from fetch_pwd import matchID
from main_pg import mnpg
import time
import mysql.connector

conn=mysql.connector.connect(host='localhost',database='commission',user='root',password='123456')
cursor=conn.cursor()

class login:
    def __init__(self,root):
        self.root=root
        self.f=Frame(root.title("Admin Page"),height=600,width=600,bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()
        self.n4=Label(text='LOGIN',bg='dodgerblue3',font=('Bold Calibri',30))
        self.n1=Label(text='ID:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n2=Label(text='Password:',fg="black",bg="dodgerblue3",font=('Calibri',14))

        self.b1=Button(text='Log In',fg='white',bg='dark red',width=20,height=2,command=lambda: self.buttonclick(0))

        self.e1=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e2=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
  
        self.n1.place(x=50,y=100)
        self.e1.place(x=250,y=100)
        self.n2.place(x=50,y=150)
        self.e2.place(x=250,y=150)
        self.n4.place(x=250,y=25)
        
        self.b1.place(x=300,y=250)

    def buttonclick(self,num=0):
               
        id=self.e1.get()
        pw=self.e2.get()

        if(num==0):
            pwd=matchID(id,pw)
            # print(pwd)
            # if(pwd!=pw):
            #     time.sleep(0.5)
            #     self.n5=Label(text='Password did not match',font=('Calibri',14),fg='darkred',bg="dodgerblue3")
            #     self.n5.place(x=50,y=200)
            #     self.root.destroy()
            #     # login(root)
            
            # # mnpg()
            # else:
            self.root.destroy()
            mnpg()

        else:
            return 

root=Tk()

mb=login(root)

root.mainloop()