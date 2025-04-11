from connection import get_connection

def delete_student(id_student):
    connection = get_connection()
    cursor=get_connection()
    sql="DELETE FROM student WHERE id=%s"
    cursor.execute(sql,(id_student,))
    connection.commit()

    if cursor.rowcount>0:
        print("diagrafike")
    else:
        print("den vrethike")
        cursor.close()
        connection.close()


        try:
        id_student=int(input("eisagetai  to id : "))
        delete_student(id_student)
        except ValueError:
        print("denvrethike id")