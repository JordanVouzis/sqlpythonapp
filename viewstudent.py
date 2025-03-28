from connection import get_connection

def view_students(name,lastname,age):
    connection = get_connection()
    cursor = connection.cursor()
    sql=" SELECT * FROM student"
    cursor.execute(sql)
    student =cusrsor.fetchall()

    if students:
        print("λιστα μαθητων")
         for student in students:
           print(f"name :{student[0]},lastname : {[1]},age :{[2]}")
    else :
       print("δεν υπαρχουν μαθητες")
       cursor.close()
       connection.close()

       view_students()    

