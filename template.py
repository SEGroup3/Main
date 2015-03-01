#imports modules, aware of redundancy
import tkinter
from tkinter import ttk
from tkinter import *

#window setup
uc4 = tkinter.Tk()
uc4.title("Analysis Window")
uc4.geometry("500x400")
uc4.wm_iconbitmap('Untitled_converted.ico')

#placeholder buttons
for num in range(1):
    btn = tkinter.Button(uc4, text='I am a button bar for shortcuts',font=('Arial', 13), height = 3, width = 75)
    btn.pack()

#creates menubar funtions for window
def ph():
   filewin = Toplevel(uc4)
   button = Button(filewin, text="I am a function placeholder")
   button.pack()
   
def helpPopup():
   filewin = Toplevel(uc4)
   lblHelp = Label(filewin, text = 'I am a placeholder for real information \n #Use case 4#')
   lblHelp.pack()
   
def Access():
   filewin = Toplevel(uc4)
   lblAcc = Label(filewin, text = 'I will have options to change font \n size and colour for all widgets')
   lblAcc.pack()   

    
  
menu = Menu(uc4)
filemenu = Menu(menu, tearoff=0)
filemenu.add_command(label="Open", command=ph)
filemenu.add_command(label="Export", command=ph)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=uc4.quit)
menu.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menu, tearoff=0)
editmenu.add_command(label="Undo", command=ph)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=ph)
editmenu.add_command(label="Copy", command=ph)
editmenu.add_command(label="Paste", command=ph)

menu.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menu, tearoff=0)
helpmenu.add_command(label="About...", command=helpPopup)
helpmenu.add_command(label="Accessibility", command=Access)
menu.add_cascade(label="Help", menu=helpmenu)

uc4.config(menu=menu)

#placeholder tree    # real tree gets values from xlrd moudule   will itereate over excel 
tree = ttk.Treeview(uc4)
 
tree["columns"]=("one","two")
tree.column("one", width=100 )
tree.column("two", width=100)
tree.heading("one", text="Grade")
tree.heading("two", text="Belbin")
 
tree.insert("" , 0,    text="", values=("",""))
 
id2 = tree.insert("", 1, "dir2", text="Group 2")
tree.insert(id2, "end", "dir 2", text="Student", values=("60","paladin"))

 
tree.pack()

#mainloop
uc4.mainloop()
