# 🔑 Making a password generator with Python GUI

import random
import string
import tkinter as tk
import pyperclip
root = tk.Tk()
root.geometry('500x500')
root.title('PASSWORD GENERATOR')

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

pwd_length = ''
pwd = ''

def create_pass():
    global alphabet
    global pwd_length
    global pwd
    pwd_length = int(pass_length.get())
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(random.choice(alphabet))
    text_result.config(text=pwd)

def copy_pwd():
    if pwd == '':
        lbl_alert.config(text='Create a password first')
    else:
        pyperclip.copy(pwd)
        lbl_alert.config(text='Succesfuly copied')

text_result = tk.Label(root, text='Length',font=("Arial", 16))
text_result.pack()

pass_length = tk.Entry(root)
pass_length.pack()

btn = tk.Button(root, text='Generate', command=create_pass,font=("Arial", 16))
btn.pack()

btn_copy = tk.Button(root, text='Copy to clipboard', command=copy_pwd,font=("Arial", 16 ))
btn_copy.pack()

text_result = tk.Label(root, text='',font=("Arial", 16))
text_result.pack()

lbl_alert = tk.Label(root, text='',font=("Arial", 16))
lbl_alert.pack()

root.mainloop()
