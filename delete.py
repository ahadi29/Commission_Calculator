## Employee Commission reset page

from tkinter import *
import mysql.connector

conn=mysql.connector.connect(host='localhost',database='commission',user='root',password='123456')
cursor=conn.cursor()

class del_user:
    def __init__(self,root):
        self.f=Frame(root.title("Payout Page"),height=600,width=600,bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()
        
        self.n=Label(text='PAYOUT',fg="black",bg="dodgerblue3",font=('Calibri Bold',26))
        self.n1=Label(text='Emp ID:',fg="black",bg="dodgerblue3",font=('Calibri',14))

        self.b1=Button(text='PAY EMPLOYEE',fg='white',bg='dark red',width=20,height=2,command=lambda: self.buttonclick(0))

        self.e1=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))

        self.n.place(x=200,y=0)    
        self.n1.place(x=50,y=100)
        self.e1.place(x=250,y=100)

        self.b1.place(x=300,y=250)

    def buttonclick(self,num):
          
        a=self.e1.get()

        if(num==0):
            empDEL = "update CALC SET sales=NULL where empId=%s"
            print(a)
            del_emp = (a,)

            cursor.execute(empDEL, del_emp)
            
            conn.commit()
            cursor.close()
            conn.close()

        else:
            return 

def del_emp():
    root=Tk()

    mb=del_user(root)

    root.mainloop()