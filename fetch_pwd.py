# fetches password form DB

import mysql.connector

def matchID(id,pw):
    conn=mysql.connector.connect(host='localhost',database='commission',user='root',password='123456')
    cursor=conn.cursor()
    conn.commit()

    pwd = "SELECT pass from ADMIN where usrId=%s and pass=%s"
    cursor.execute(pwd,(id,pw))
    pwd = cursor.fetchone()

    conn.close()

    return pwd[0]