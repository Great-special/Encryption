import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
from ende import ENDE

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('dark-blue')


def to_encrypt():
    global main_file
    home_path = os.environ.get('HOMEPATH')
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))
    # Get Filename
    main_file = filedialog.askopenfilename(initialdir=f"{home_path}/Documents", title='Select A File To Encrypt', filetypes=filetypes)
    print(main_file)
    lbl_main = ctk.CTkLabel(body, text='')
    lbl_main.place(relx=0.05, rely=0.1)
    lbl_main.destroy()
    lbl_main = ctk.CTkLabel(body, text=main_file,)
    lbl_main.place(relx=0.05, rely=0.1)
    
    
def to_save():
    global ende_file
    home_path = os.environ.get('HOMEPATH')
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))
    # Get Filename
    ende_file = filedialog.asksaveasfilename(initialdir=f"{home_path}/Documents", title='Type A File Name To Save', filetypes=filetypes)
    print(ende_file)
   
    lbl_ende = ctk.CTkLabel(body, text='',)
    lbl_ende.place(relx=0.05, rely=0.3)
    lbl_ende.destroy()
    lbl_ende = ctk.CTkLabel(body, text=ende_file,)
    lbl_ende.place(relx=0.05, rely=0.3)
    
    
   

def encrypt():
    ende = ENDE(main_file, ende_file)
    ende.ende()
    print('done encrypting')
    lbl_ = ctk.CTkLabel(body, text="Done Encryption",)
    lbl_.place(relx=0.05, rely=0.6)
    lbl_.destroy()
    lbl_ = ctk.CTkLabel(body, text="Done Encryption",)
    lbl_.place(relx=0.05, rely=0.6)
 

root = ctk.CTk()

root.title('ENDE-Encode Decode')
root.geometry('700x450')
root.iconbitmap('crypto-ENDE.ico')


head = ctk.CTkFrame(root, height=150)
head.place(relx=0.05, rely=0.05, relwidth=0.9)

label_file = ctk.CTkLabel(head, text='Enter File Name to be encrypted', height=25)
label_file.place(relx=.1, rely=.1)

file_1 = ctk.CTkButton(head, text='To encrypt',  width=120, height=25, corner_radius=7, command=to_encrypt)
file_1.place(relx=.47, rely=.1)

label_file_2 = ctk.CTkLabel(head, text='Enter File Name to be saved', height=25)
label_file_2.place(relx=.1, rely=.35)

file_2 = ctk.CTkButton(head, text='To be saved', width=120, height=25, corner_radius=7, command=to_save)
file_2.place(relx=.47, rely=.35)

button_ende = ctk.CTkButton(head, text='Encryption', corner_radius=15, command=encrypt)
button_ende.place(relx=.35, rely=.7)

body = ctk.CTkFrame(root, corner_radius=10)
body.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.25)

lbl_ = ctk.CTkLabel(root, text="Please Enter A Text File To Encrypt It \nClick On The Encryption Button To Encrypt The File")
lbl_.place(relwidth=1, relheight=0.2, rely=0.7)

foot = ctk.CTkLabel(root, text='ENDE - Encode Decode | Developed By Global Concept Tech \n For Any Technical Issue Contact: +234 703 207 4053 ',
                    corner_radius=5)
foot.place(rely=0.9, relwidth=1, relheight=0.1)

root.mainloop()