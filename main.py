import tkinter as tk
from tkinter import messagebox
import pyodbc

# Connect to SQL Server
import pyodbc

# Connect to SQL Server
conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-BLPH810\\SQLEXPRESS;DATABASE=Kavya;Trusted_Connection=yes'
)
cursor = conn.cursor()



# GUI Setup
root = tk.Tk()
root.title("ICICI Bank System")
root.geometry("400x400")

# Add Customer
def add_customer():
    name = entry_name.get()
    balance = entry_balance.get()
    try:
        cursor.execute("INSERT INTO icici_bank(Name, Balance) VALUES (?, ?)", (name, float(balance)))
        conn.commit()
        messagebox.showinfo("Success", "Customer added successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# View Customers
def view_customers():
    cursor.execute("SELECT * FROM icici_bank")
    records = cursor.fetchall()
    output = "\n".join([f"{r.id} | {r.Name} | ₹{r.Balance}" for r in records])
    messagebox.showinfo("Customers", output)

# Update Balance
def update_balance():
    name = entry_name.get()
    amount = float(entry_balance.get())
    cursor.execute("UPDATE icici_bank SET Balance = Balance + ? WHERE Name = ?", (amount, name))
    conn.commit()
    messagebox.showinfo("Success", "Balance updated!")

# Delete Customer
def delete_customer():
    name = entry_name.get()
    cursor.execute("DELETE FROM icici_bank WHERE Name = ?", (name,))
    conn.commit()
    messagebox.showinfo("Success", "Customer deleted!")

# View Logs
def view_logs():
    cursor.execute("SELECT * FROM icici_log")
    logs = cursor.fetchall()
    output = "\n".join([f"{l.id} | {l.Name} | {l.Action_type} | ₹{l.old_Balance} → ₹{l.new_Balance}" for l in logs])
    messagebox.showinfo("Logs", output)

# GUI Widgets
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Amount").pack()
entry_balance = tk.Entry(root)
entry_balance.pack()

tk.Button(root, text="Add Customer", command=add_customer).pack(pady=5)
tk.Button(root, text="View Customers", command=view_customers).pack(pady=5)
tk.Button(root, text="Update Balance", command=update_balance).pack(pady=5)
tk.Button(root, text="Delete Customer", command=delete_customer).pack(pady=5)
tk.Button(root, text="View Logs", command=view_logs).pack(pady=5)

root.mainloop()
