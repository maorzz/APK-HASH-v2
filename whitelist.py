# Maor/[apkinfo+hashapk V1]
# האפליקציה לא חייבת להיות באותה תקייה אבל התוכנה כן (AAPT)

from tkinter import *
import hashlib
import sys
import subprocess
import os
import re
import tkinter
from tkinter import filedialog
import tkinter as tk
import sys
import count
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename


# G-U-I

root = Tk()
root.title('פורמט אפליקצייה למייבס')
root.iconbitmap('zoro.ico')
app_width = 250
app_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
my_img = ImageTk.PhotoImage(Image.open("logo.jpg"))
my_label = Label(image=my_img)
my_label.pack()


def browse_file():
    global file_path
    file_path = askopenfilename(
        filetypes=(('APK FILES', 'apk'),))
    root.destroy()


T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, "WHITELIST PR0JECT by -M-")


browse_button = Button(root, text="בחר אפליקציה",
                       command=browse_file, fg='#0059b3')
browse_button.pack(pady=30)

root.mainloop()


# OPEN CMD AND RUN COMMAND :
# get apk name
def apk():
    command = 'aapt.exe dump badging ' + file_path + '| findstr package:'
    result = ""
    p = subprocess.Popen(command, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    output = str(output, encoding='utf8')
    if output != "":
        result = output.split()[1][6:-1]
    return result


# get apk Label
def label():
    command = 'aapt.exe dump badging ' + file_path + '| findstr package:'
    result = ""
    p = subprocess.Popen(command, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    output = str(output, encoding='utf8')
    if output != "":
        result = output.split()[3][13:-1]
    return result


def version():
    command = 'aapt.exe dump badging ' + file_path + '| findstr package:'
    result = ""
    p = subprocess.Popen(command, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    output = str(output, encoding='utf8')
    if output != "":
        result = output.split()[2][13:-1]
    return result


# TAKE APK AND CONVERT TO HASH


def hash():
    import hashlib


sha256_hash = hashlib.sha256()
with open(file_path, "rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096), b""):
        sha256_hash.update(byte_block)


id = label()
hash = sha256_hash.hexdigest()
apkname = apk()
versionc = version()

# תוצאה
result = ("\n" + "<package" + "\n" + "label=" + f"'{id}'" + "\n"

          "hash=" + f'"{hash}"' + "\n" +

          "id=" + f"'{apkname}'" + "\n" + f"version='{versionc}'" + "\n" + 'networkMode="private"/>' + "\n" + "</msiApplicationWhitelist>"+"\n")

# saveing file
f = open("whitelist.xml", 'a')
sys.stdout = f
print(result)


# G-U-I
root = Tk()
root.title('פורמט אפליקצייה למייבס')
app_width = 500
app_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.iconbitmap('zoro.ico')


def open_txt():
    text_file = open("whitelist.xml", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    open_button.configure(state=DISABLED)
    text_file.close()


def exit():
    root.destroy()


my_text = Text(root, width=40, height=10, font=("Helvetica", 16))
my_text.pack(pady=20)

open_button = Button(root, text="הצג קובץ",
                     command=open_txt, font=("Helvetica", 16))
open_button.pack(pady=20)


num = Button(root,   text='   אפליקציות = ' + str(count.appsum) + ' (מוגבל ל52 אפליקציות)', command=exit,
             font=("Helvetica", 16), fg='#8B0000')
num.pack(pady=20)

# deletelastline
deletelastline = open("whitelist.xml", "r")
d = deletelastline.read()
deletelastline.close()
m = d.split("\n")
s = "\n".join(m[:-3])
deletelastline = open("whitelist.xml", "w")
for i in range(len(s)):
    deletelastline.write(s[i])
deletelastline.close()


f.close()
root.mainloop()
