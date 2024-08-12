import tkinter as tk 
from tkinter import messagebox 
from tkinter import ttk 
import sqlite3 

def create_table(): 
    conn = sqlite3.connect('students.db') 
    cursor = conn.cursor() 
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS students ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            father_name TEXT, 
            contact_no TEXT, 
            email_address TEXT, 
            date_of_birth TEXT 
        ) 
    ''') 
    conn.commit() 
    conn.close() 

def add_student(): 
    conn = sqlite3.connect('students.db') 
    cursor = conn.cursor() 
    cursor.execute(''' 
        INSERT INTO students (name, father_name, contact_no, email_address, date_of_birth) 
        VALUES (?, ?, ?, ?, ?) 
    ''', (entry_name.get(), entry_father_name.get(), entry_contact_no.get(), entry_email_address.get(), entry_date_of_birth.get())) 
    conn.commit() 
    conn.close() 
    messagebox.showinfo("Success", "Student added successfully!") 
    clear_entries() 
    refresh_treeview() 

def clear_entries(): 
    entry_name.delete(0, tk.END) 
    entry_father_name.delete(0, tk.END) 
    entry_contact_no.delete(0, tk.END) 
    entry_email_address.delete(0, tk.END) 
    entry_date_of_birth.delete(0, tk.END) 
    entry_id.delete(0, tk.END) 

def refresh_treeview(): 
    for row in treeview.get_children(): 
        treeview.delete(row) 
    
    conn = sqlite3.connect('students.db') 
    cursor = conn.cursor() 
    cursor.execute('SELECT * FROM students') 
    rows = cursor.fetchall() 
    conn.close() 
    
    for row in rows: 
        treeview.insert("", tk.END, values=row) 

def select_record(event): 
    selected_item = treeview.selection()[0] 
    selected_values = treeview.item(selected_item, 'values') 
    entry_id.config(state='normal') 
    entry_id.delete(0, tk.END) 
    entry_id.insert(0, selected_values[0]) 
    entry_name.delete(0, tk.END) 
    entry_name.insert(0, selected_values[1]) 
    entry_father_name.delete(0, tk.END) 
    entry_father_name.insert(0, selected_values[2]) 
    entry_contact_no.delete(0, tk.END) 
    entry_contact_no.insert(0, selected_values[3]) 
    entry_email_address.delete(0, tk.END) 
    entry_email_address.insert(0, selected_values[4]) 
    entry_date_of_birth.delete(0, tk.END) 
    entry_date_of_birth.insert(0, selected_values[5]) 

def update_student(): 
    student_id = entry_id.get() 
    conn = sqlite3.connect('students.db') 
    cursor = conn.cursor() 
    cursor.execute(''' 
        UPDATE students 
        SET name = ?, father_name = ?, contact_no = ?, email_address = ?, date_of_birth = ? 
        WHERE id = ? 
    ''', (entry_name.get(), entry_father_name.get(), entry_contact_no.get(), entry_email_address.get(), entry_date_of_birth.get(), student_id)) 
    conn.commit() 
    conn.close() 
    messagebox.showinfo("Success", "Student updated successfully!") 
    clear_entries() 
    refresh_treeview() 

def delete_student(): 
    student_id = entry_id.get() 
    conn = sqlite3.connect('students.db') 
    cursor = conn.cursor() 
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,)) 
    conn.commit() 
    conn.close() 
    messagebox.showinfo("Success", "Student deleted successfully!") 
    clear_entries() 
    refresh_treeview() 

def enable_edit(): 
    # Make the entry fields editable 
    entry_name.config(state='normal') 
    entry_father_name.config(state='normal') 
    entry_contact_no.config(state='normal') 
    entry_email_address.config(state='normal') 
    entry_date_of_birth.config(state='normal') 

# Main window 
root = tk.Tk() 
root.title("Student Registration System") 

# Labels 
tk.Label(root, text="ID").grid(row=0, column=0) 
tk.Label(root, text="Name").grid(row=1, column=0) 
tk.Label(root, text="Father Name").grid(row=2, column=0) 
tk.Label(root, text="Contact No").grid(row=3, column=0) 
tk.Label(root, text="Email Address").grid(row=4, column=0) 
tk.Label(root, text="Date of Birth").grid(row=5, column=0) 

# Entries 
entry_id = tk.Entry(root, state='disabled') 
entry_name = tk.Entry(root) 
entry_father_name = tk.Entry(root) 
entry_contact_no = tk.Entry(root) 
entry_email_address = tk.Entry(root) 
entry_date_of_birth = tk.Entry(root) 
entry_id.grid(row=0, column=1) 
entry_name.grid(row=1, column=1) 
entry_father_name.grid(row=2, column=1) 
entry_contact_no.grid(row=3, column=1) 
entry_email_address.grid(row=4, column=1) 
entry_date_of_birth.grid(row=5, column=1) 

# Buttons 
tk.Button(root, text="Add", command=add_student).grid(row=6, column=0) 
tk.Button(root, text="Edit", command=enable_edit).grid(row=6, column=1) 
tk.Button(root, text="Update", command=update_student).grid(row=6, column=2) 
tk.Button(root, text="Delete", command=delete_student).grid(row=6, column=3) 
tk.Button(root, text="Clear", command=clear_entries).grid(row=6, column=4) 

# Treeview for displaying student records 
columns = ("ID", "Name", "Father Name", "Contact No", "Email Address", "Date of Birth") 
treeview = ttk.Treeview(root, columns=columns, show='headings') 
treeview.grid(row=7, column=0, columnspan=5) 

# Define column headings 
for col in columns: 
    treeview.heading(col, text=col) 
    treeview.column(col, width=150) 

treeview.bind('<ButtonRelease-1>', select_record) 

create_table() 
refresh_treeview() 
root.mainloop()
