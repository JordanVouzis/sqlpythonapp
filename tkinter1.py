import tkinter as tk
from tkinter import messagebox
from connection import get_connection

# Συνάρτηση για εισαγωγή βιβλίου
def insert_student(name,lastname,age):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO student (name,lastname,age) VALUES (%s, %s, %s)"
        values =(name,lastname,age)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        print("Σφάλμα:", e)
        return False

# Συνάρτηση για χειρισμό του κουμπιού
def submit_student():
    name= entry_name.get()
    lastname = entry_lastname.get()
    age = entry_age.get()
    

    if not (name and lastname and age):
        messagebox.showwarning("Σφάλμα", "Συμπλήρωσε όλα τα πεδία!")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Σφάλμα", "Το έτος πρέπει να είναι αριθμός!")
        return

    if insert_student(name,lastname,age):
        messagebox.showinfo("Επιτυχία", "Το βιβλίο προστέθηκε επιτυχώς!")
        entry_name.delete(0, tk.END)
        entry_lastname.delete(0, tk.END)
        entry_age.delete(0, tk.END)
       
    else:
        messagebox.showerror("Αποτυχία", "Αποτυχία εισαγωγής βιβλίου.")

# Δημιουργία παραθύρου
window = tk.Tk()
window.title("Εισαγωγή Μαθητή")
window.geometry("400x300")

# Ετικέτες και πεδία
tk.Label(window, text="Όνομα:").pack(pady=5)
entry_name = tk.Entry(window, width=40)
entry_name.pack()

tk.Label(window, text="Επίθετο:").pack(pady=5)
entry_lastname = tk.Entry(window, width=40)
entry_lastname.pack()

tk.Label(window, text="Έτος Γέννησης:").pack(pady=5)
entry_age = tk.Entry(window, width=40)
entry_age.pack()

# Κουμπί καταχώρησης
submit_button = tk.Button(window, text="Καταχώρηση μαθητή", command=submit_student)
submit_button.pack(pady=20)

# Εκκίνηση εφαρμογής
window.mainloop()


