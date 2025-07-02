import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = {}

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", f"Contact '{name}' added.")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Name cannot be empty.")

def view_contacts():
    if not contacts:
        messagebox.showinfo("Contacts", "No contacts to display.")
    else:
        result = ""
        for name, info in contacts.items():
            result += f"{name}: {info['phone']}, {info['email']}, {info['address']}\n"
        messagebox.showinfo("Contact List", result)

def search_contact():
    keyword = simpledialog.askstring("Search", "Enter name or phone number:")
    if keyword:
        for name, info in contacts.items():
            if keyword.lower() in name.lower() or keyword in info['phone']:
                messagebox.showinfo("Found Contact",
                    f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
                return
        messagebox.showwarning("Not Found", "No contact found.")

def update_contact():
    name = simpledialog.askstring("Update", "Enter the name of the contact to update:")
    if name in contacts:
        phone = simpledialog.askstring("Update Phone", f"New phone (current: {contacts[name]['phone']}):")
        email = simpledialog.askstring("Update Email", f"New email (current: {contacts[name]['email']}):")
        address = simpledialog.askstring("Update Address", f"New address (current: {contacts[name]['address']}):")

        contacts[name] = {
            'phone': phone or contacts[name]['phone'],
            'email': email or contacts[name]['email'],
            'address': address or contacts[name]['address']
        }
        messagebox.showinfo("Success", f"Contact '{name}' updated.")
    else:
        messagebox.showerror("Error", "Contact not found.")

def delete_contact():
    name = simpledialog.askstring("Delete", "Enter the name of the contact to delete:")
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
    else:
        messagebox.showerror("Error", "Contact not found.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# ----------------- GUI Setup -----------------

root = tk.Tk()
root.title("📒 Contact Book")
root.configure(bg="#f0f4f7")
root.geometry("400x400")
root.resizable(False, False)

# Title Label
tk.Label(root, text="Contact Book", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#333").pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=5)

# Labels and Entry fields
tk.Label(frame, text="Name", bg="#f0f4f7").grid(row=0, column=0, sticky="e", pady=4, padx=5)
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, pady=4)

tk.Label(frame, text="Phone", bg="#f0f4f7").grid(row=1, column=0, sticky="e", pady=4)
phone_entry = tk.Entry(frame, width=30)
phone_entry.grid(row=1, column=1, pady=4)

tk.Label(frame, text="Email", bg="#f0f4f7").grid(row=2, column=0, sticky="e", pady=4)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=2, column=1, pady=4)

tk.Label(frame, text="Address", bg="#f0f4f7").grid(row=3, column=0, sticky="e", pady=4)
address_entry = tk.Entry(frame, width=30)
address_entry.grid(row=3, column=1, pady=4)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f0f4f7")
btn_frame.pack(pady=20)

btn_width = 18
tk.Button(btn_frame, text="➕ Add Contact", width=btn_width, command=add_contact).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="📜 View Contacts", width=btn_width, command=view_contacts).grid(row=0, column=1, padx=5, pady=5)

tk.Button(btn_frame, text="🔍 Search Contact", width=btn_width, command=search_contact).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="✏️ Update Contact", width=btn_width, command=update_contact).grid(row=1, column=1, padx=5, pady=5)

tk.Button(btn_frame, text="❌ Delete Contact", width=btn_width, command=delete_contact).grid(row=2, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="🚪 Exit", width=btn_width, command=root.quit).grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
