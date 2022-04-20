# Commission Calculate page

from tkinter import *
from fetch_pwd import matchID
from drop_down import *
import mysql.connector

conn=mysql.connector.connect(host='localhost',database='commission',user='root',password='123456')
cursor=conn.cursor()
com_cursor=conn.cursor()
conn.commit()

class comm():
    def __init__(self,root):
        self.root=root
        self.f=Frame(root.title("Commission Calculate Page"),height=600,width=600,bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()
        
        self.n1=Label(text='Commission Calculate',bg='dodgerblue3',font=('Bold Calibri',30))
        self.n2=Label(text='Emp ID:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n3=Label(text='Sales:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n4=Label(text='Commission:',fg="black",bg="dodgerblue3",font=('Calibri',14))
    
        self.b1=Button(text='Calculate',fg='white',bg='dark red',width=20,height=2,font=('Calibri',15),command=lambda: self.buttonclick(0))

        options = db_dropdown()

        self.clicked= StringVar()
        self.clicked.set("select ID")

        self.e2=OptionMenu( self.f , self.clicked , *options,command= self.getValue())
        self.e3=Entry(self.f,width=30,fg="black",bg="white",font=('Calibri',14))


        self.n1.place(x=150,y=25)
        self.n2.place(x=50,y=100)
        self.e2.place(x=250,y=100,height=25, width=300)
        # self.e2.config(width=10, height=2)
        self.n3.place(x=50,y=150)
        self.e3.place(x=250,y=150)
        self.n4.place(x=50,y=200)

        self.b1.place(x=50,y=500)


    def getValue(self):
            self.choice = self.clicked.get()  

    def buttonclick(self,num):
        if(num==0):
            a=int(self.clicked.get())
            b=self.e3.get()

            com = " insert into CALC(empId, sales) VALUES (%s,%s)"
            cursor.execute(com,(a,b))
            conn.commit()

            com_calc = "SELECT commision from CALC WHERE empId=%s"
            com_cursor.execute(com_calc,(a,))
            com_calc = com_cursor.fetchall()

            lis=[i[0] for i in com_calc]

            self.e4=Label(text=str(lis[-1]),width=30,fg="black",bg="white",font=('Calibri',14))
            self.e4.place(x=250,y=200)

            cursor.close()
            conn.close()

def add_comm():
    root=Tk()

    mb=comm(root)

    root.mainloop()
            