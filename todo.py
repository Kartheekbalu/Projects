#TO DO LIST GUI
import tkinter
from tkinter import *
from tkinter import messagebox

root=tkinter.Tk()

#Heading Label
lab1=tkinter.Label(root,text='TO-DO LIST')
lab1.grid(row=0,column=1)

#task enter label
lab2=tkinter.Label(root,text='Enter Task')
lab2.grid(row=1,column=0)

#Main bar entry
bar=Entry(root,width=20,justify=RIGHT)
bar.grid(row=1,column=1)
def clear():
    bar.delete(0,END)

#text collection
def clear():
    bar.delete(0,END)

#button power
def btn_clk(num):
    cur_val=bar.get()
    #clearing screen
    clear()
    fin_val=cur_val + num
    bar.insert(0,fin_val)
    
a=''
def add():
    global a
    a=bar.get()
    clear()
    text.config(text=a)

def dlt():
    text=' '

#three buttons add,del,clear
add=Button(root,text='Add Task',command=add)
add.grid(row=2,column=0)
dele=Button(root,text='Del Task',command=dlt)
dele.grid(row=2,column=1)
clr=Button(root,text='Clear',command=clear)
clr.grid(row=2,column=2)

#Saved text box
text = tkinter.Label(root, text="")
text.grid(row=4,column=0)

#Exit box
def ex():
     messagebox.showinfo('info','Thanks for visiting')
     root.destroy()
exit=Button(root,text='Exit',command=ex,bg='#FE1111',padx=100)
exit.grid(row=6,column=2)

root.mainloop()
