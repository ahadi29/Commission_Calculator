## Employee adding page

from tkinter import*
import mysql.connector

conn=mysql.connector.connect(host='localhost',database='commission',user='root',password='123456')
cursor=conn.cursor()

class add_user:
    def __init__(self,root):
        self.f=Frame(root.title("Add User Page"),height=600,width=600,bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()
        
        self.n=Label(text='ADD EMPLOYEE',fg="black",bg="dodgerblue3",font=('Calibri Bold',26))
        self.n1=Label(text='Emp ID:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n2=Label(text='Name:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n3=Label(text='Location:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n4=Label(text='Salary:',fg="black",bg="dodgerblue3",font=('Calibri',14))

        self.b1=Button(text='ADD EMPLOYEE',fg='white',bg='dark red',width=20,height=2,command=lambda: self.buttonclick(0))

        self.e1=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e2=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e3=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e4=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))

        self.n.place(x=200,y=0)    
        self.n1.place(x=50,y=100)
        self.e1.place(x=250,y=100)
        self.n2.place(x=50,y=150)
        self.e2.place(x=250,y=150)
        self.n3.place(x=50,y=200)
        self.e3.place(x=250,y=200)
        self.n4.place(x=50,y=250)
        self.e4.place(x=250,y=250)

        self.b1.place(x=300,y=450)

    def buttonclick(self,num):
          
        a=self.e1.get()
        b=self.e2.get()
        c=self.e3.get()
        d=self.e4.get()

        if(num==0):
            empAdd = " insert into EMP VALUES (%s,%s,%s,%s)"

            insert_emp = (a, b, c, d)

            cursor.execute(empAdd, insert_emp)
            
            conn.commit()
            cursor.close()
            conn.close()

        else:
            return 

def add_emp():
    root=Tk()

    mb=add_user(root)

    root.mainloop()
