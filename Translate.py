from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import googletrans
from textblob import *
import os
import sys


def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def trans():
    global lang
    try:
        te = text1.get(1.0, END)
        o1 = op1.get()
        o2 = op2.get()
        if te:
            words = TextBlob(te)
            lan1 = ""
            lan2 = ""
            for i, j in lang.items():
                if j.capitalize() == o1:
                    lan1 = i
                if j.capitalize() == o2:
                    lan2 = i
            words = words.translate(from_lang=lan1, to=lan2)
            text2.delete(1.0, END)
            text2.insert(END, words)
    except Exception as e:
        messagebox.showerror("Translate", "Please check your text")


root = Tk()
root.title("Translate")
root.geometry("700x470")
root.resizable(False, False)
root.configure(bg='black')
raj=resource_path("translate.ico")
root.iconbitmap(raj)
raj1=resource_path("trans.png")
photo1 = PhotoImage(file=raj1)
lang = googletrans.LANGUAGES
langv = [i.capitalize() for i in lang.values()]
langk = lang.keys()
Label(root, text="To:", font=("roboto bold", 12), bg="black", fg="yellow").place(x=10, y=10)
Label(root, text="From:", font=("roboto bold", 12), bg="black", fg="yellow").place(x=10, y=250)

op1 = Combobox(root, values=langv, width=15, height=10, font=("lucida", 12), state="r")
op1.place(x=55, y=10)
op1.set("English")

op2 = Combobox(root, values=langv, width=15, height=10, font=("lucida", 12), state="r")
op2.place(x=55, y=250)
op2.set("Hindi")

f1 = Frame(root, bg="grey", bd=5)
f1.place(x=240, y=10, width=450, height=210)

text1 = Text(f1, font=("lucida bold", 13), bg="black", fg="white", wrap=WORD, relief=GROOVE)
text1.place(x=0, y=0, width=440, height=200)

scbar1 = Scrollbar(f1)
scbar1.pack(side="right", fill="y")
scbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scbar1.set)

f2 = Frame(root, bg="grey", bd=5)
f2.place(x=240, y=250, width=450, height=210)

text2 = Text(f2, font=("lucida bold", 13), bg="black", fg="white", wrap=WORD, relief=GROOVE)
text2.place(x=0, y=0, width=440, height=200, )

scbar2 = Scrollbar(f2)
scbar2.pack(side="right", fill="y")
scbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scbar2.set)

Button(root, compound=LEFT, image=photo1, bg="black", cursor="hand2", activebackground="green", width=65,
       command=trans).place(x=70, y=100)

root.mainloop()
