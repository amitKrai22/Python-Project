'''import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input!")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the widgets
label_num1 = tk.Label(window, text="Number 1:")
entry_num1 = tk.Entry(window)
label_num2 = tk.Label(window, text="Number 2:")
entry_num2 = tk.Entry(window)
button_calc = tk.Button(window, text="Calculate", command=calculate)
label_result = tk.Label(window, text="Result:")

# Place the widgets in the window using the grid manager
label_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num1.grid(row=0, column=1, padx=5, pady=5)
label_num2.grid(row=1, column=0, padx=5, pady=5)
entry_num2.grid(row=1, column=1, padx=5, pady=5)
button_calc.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
label_result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Start the main event loop
window.mainloop()'''
import tkinter as tk
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="221011",
    database="MySQL"
)
cursor = db.cursor()

def save_password():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    # Insert the password into the database
    query = "INSERT INTO passwords (website, username, password) VALUES (%s, %s, %s)"
    values = (website, username, password)
    cursor.execute(query, values)
    db.commit()

    # Clear the input fields
    entry_website.delete(0, tk.END)
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

def retrieve_password():
    website = entry_website.get()

    # Retrieve the password from the database
    query = "SELECT password FROM passwords WHERE website = %s"
    value = (website,)
    cursor.execute(query, value)
    result = cursor.fetchone()

    if result:
        password = result[0]
        label_result.config(text=f"Password:  { password}")
    else:
        label_result.config(text="Password not found!")

# Create the main window
window = tk.Tk()
window.title("Password Manager")

# Create the widgets
label_website = tk.Label(window, text="Website:")
entry_website = tk.Entry(window)
label_username = tk.Label(window, text="Username:")
entry_username = tk.Entry(window)
label_password = tk.Label(window, text="Password:")
entry_password = tk.Entry(window, show="*")
button_save = tk.Button(window, text="Save Password", command=save_password)
button_retrieve = tk.Button(window, text="Retrieve Password", command=retrieve_password)
label_result = tk.Label(window, text="")

# Place the widgets in the window using the grid manager
label_website.grid(row=0, column=0, padx=5, pady=5)
entry_website.grid(row=0, column=1, padx=5, pady=5)
label_username.grid(row=1, column=0, padx=5, pady=5)
entry_username.grid(row=1, column=1, padx=5, pady=5)
label_password.grid(row=2, column=0, padx=5, pady=5)
entry_password.grid(row=2, column=1, padx=5, pady=5)
button_save.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
button_retrieve.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
label_result.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Start the main event loop
window.mainloop()
