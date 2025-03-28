from connection import get_connection

def insert_student(name,lastname,age):
    connection = get_connection()
    cursor = connection.cursor()
    sql="INSERT INTO student (name,lastname,age) values (%s,%s,%s)"
    values = (name,lastname,age)
    cursor.execute(sql,values)
    connection.commit()
    print("ο μαθητης προστεθηκε")
    cursor.close()
    connection.close()
    
name=input("ονομα :")
lastname=input("επιθετο :")
age=int(input("ηλικια :"))

insert_student(name,lastname,age)