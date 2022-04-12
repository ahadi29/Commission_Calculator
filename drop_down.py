# Fetches IDs from DB

import mysql.connector

def db_dropdown(): 
    conn=mysql.connector.connect(host='localhost',database='commission',user='root',password='123456')
    cursor=conn.cursor()
    conn.commit()

    sql = 'SELECT empid FROM EMP' 

    cursor.execute(sql)
    list_tested = cursor.fetchall()  
    list_tested = [i for sub in list_tested for i in sub]  

    return list_tested