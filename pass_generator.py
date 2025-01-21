# 🔑 Making a password generator with Python GUI

import random
import string
import tkinter as tk
import pyperclip

# Initialize the main Tkinter window
root = tk.Tk()
root.geometry('500x500')
root.title('PASSWORD GENERATOR')

# Character sets for password generation
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

pwd = ''  # To store the generated password

# Function to generate a password
def create_pass():
    global pwd
    lbl_alert.config(text="")  # Clear previous alerts
    text_result.config(text="")  # Clear previous password
    
    pwd_length = pass_length.get()
    
    # Validate input: Check if input is empty or not an integer
    if not pwd_length:
        lbl_alert.config(text="Error: Please enter a password length!", fg="red")
        return
    if not pwd_length.isdigit():
        lbl_alert.config(text="Error: Password length must be a number!", fg="red")
        return
    
    pwd_length = int(pwd_length)
    if pwd_length <= 0:
        lbl_alert.config(text="Error: Password length must be greater than zero!", fg="red")
        return

    # Generate the password
    pwd = ''.join(random.choice(alphabet) for _ in range(pwd_length))
    text_result.config(text=pwd, fg="blue")

# Function to copy password to clipboard
def copy_pwd():
    if not pwd:
        lbl_alert.config(text="Error: Create a password first!", fg="red")
    else:
        pyperclip.copy(pwd)
        lbl_alert.config(text="Password successfully copied to clipboard!", fg="green")

# UI Elements
tk.Label(root, text="Enter Password Length:", font=("Arial", 16)).pack(pady=10)
pass_length = tk.Entry(root, font=("Arial", 14))
pass_length.pack(pady=5)

btn_generate = tk.Button(root, text="Generate Password", command=create_pass, font=("Arial", 16))
btn_generate.pack(pady=10)

btn_copy = tk.Button(root, text="Copy to Clipboard", command=copy_pwd, font=("Arial", 16))
btn_copy.pack(pady=10)

text_result = tk.Label(root, text="", font=("Arial", 16), fg="blue")
text_result.pack(pady=10)

lbl_alert = tk.Label(root, text="", font=("Arial", 16), fg="red")
lbl_alert.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
