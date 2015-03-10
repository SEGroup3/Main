#imports modules, handles import error (version based)
import tkinter
from tkinter import *
from tkinter import ttk
import csv
from tkinter import filedialog 
from tkinter.filedialog import askopenfilename    
from tkinter.messagebox import showerror


#window setup
uc4 = tkinter.Tk()
uc4.title("Analysis Window")
uc4.geometry("1000x450")
uc4.wm_iconbitmap('icon.ico')


#sets the default csv to be opened
open_file='Results.csv'


#Imports the csv file as a list of Tuples
with open(open_file, 'Ur') as f:
    RawCsv = list(tuple(rec) for rec in csv.reader(f, delimiter=','))
headings=RawCsv[0]
data=RawCsv[1:]


################   
def repack():
    tree.pack()
          
def kill_table():
    tree.destroy()
################


#Function allowing new files to be loaded into the reader

def openfile():
    global headings
    global data
    global tree
    global scrollbar

    open_file=(ent1.get())
    with open(open_file, 'Ur') as f:
        RawCsv = list(tuple(rec) for rec in csv.reader(f, delimiter=','))
        
    headings=RawCsv[0]
    data=RawCsv[1:]
    
    tree = ttk.Treeview(uc4,selectmode='extended', columns=headings, show='headings',height=50)
    for title in headings:
        tree.heading(title, text=title, command=lambda c=title: sortby(tree, c, 0))

    for student in data:
        tree.insert('', 'end', values=student)


    #open_file=(ent1.get())
   #with open(open_file, 'Ur') as f:
    #    RawCsv = list(tuple(rec) for rec in csv.reader(f, delimiter=','))

    tree.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)

#Slices the list and reassigns them seperate variables
    headings=RawCsv[0]
    data=RawCsv[1:]
        
def combo():
    kill_table()
    openfile()
    repack()

#creates menubar funtions for window
def ph():
   filewin = Toplevel(uc4)
   button = Button(filewin, text="I am a function placeholder")
   button.pack()
   
def helpPopup():
   filewin = Toplevel(uc4)
   lblHelp = Label(filewin, height=8, width=50, text = 'To import your own .csv files into the reader type \n the full directory address into the bar. \n To use the default .csv file, double click \n "default". To modify the default file, locate \n the the file in the folder containing \n the application and save as a .csv file type. ')
   lblHelp.pack()
   
def Access():
   filewin = Toplevel(uc4)
   lblAcc = Label(filewin, text = 'This software uses Python 3.4, and the modules\n csv, tkinter, and the ttk package.\n Analysis window is the 4th use case of \n a larger project. I am made by Calum Davies.')
   lblAcc.pack()

def load():
    global ent1
    file_name = askopenfilename(filetypes=(('Template files', '*tplate'),('Comma Seperated Values', '*.csv')))

    if file_name:
        try:
            ent1.config(text = (file_name))
            kill_table()
            
            global open_file
            global headings
            global data
            global tree
            global scrollbar

            open_file=(file_name)
            with open(open_file, 'Ur') as f:
                RawCsv = list(tuple(rec) for rec in csv.reader(f, delimiter=','))

            headings=RawCsv[0]
            data=RawCsv[1:]
            
            tree = ttk.Treeview(uc4,selectmode='extended', columns=headings, show='headings',height=50)
            for title in headings:
                tree.heading(title, text=title, command=lambda c=title: sortby(tree, c, 0))

            for student in data:
                tree.insert('', 'end', values=student)
        

            #open_file=(file_name)
            #with open(open_file, 'Ur') as f:
            #    RawCsv = list(tuple(rec) for rec in csv.reader(f, delimiter=','))

            tree.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=tree.yview)

            #headings=RawCsv[0]
            #data=RawCsv[1:]
            repack()
            
        except:                     
            showerror('Error, could not read filename')
        return
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'FUNCTION TO SORT CONTENTS OF COLUMN'

def sortby(tree, col, descending):
    # get data to sort
    data = [(tree.set(child, col), child) for child in tree.get_children('')]

    # sort data
    data.sort(reverse=descending)
    for indx, item in enumerate(data):
        tree.move(item[1], '', indx)

    # sort data in opposite direction
    tree.heading(col,
        command=lambda col=col: sortby(tree, col, int(not descending)))
  
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''  
'FUNCTIONS FOR MENUBAR'

menu = Menu(uc4)
filemenu = Menu(menu, tearoff=0)
filemenu.add_command(label="Open", command=load)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=uc4.quit)
menu.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menu, tearoff=0)
helpmenu.add_command(label="Help", command=helpPopup)
helpmenu.add_command(label="About", command=Access)
menu.add_cascade(label="Help", menu=helpmenu)

uc4.config(menu=menu)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#WIDGETS#
#^^^^^^^#

#Spacer
spacer=tkinter.LabelFrame(uc4, relief=FLAT, height=40)
spacer.pack()


#Treeview
tree = ttk.Treeview(uc4,selectmode='extended', columns=headings, show='headings',height=50)
for title in headings:
    tree.heading(title, text=title, command=lambda c=title: sortby(tree, c, 0))

for student in data:
    tree.insert('', 'end', values=student)


        
#Entry
ent1 = Entry(uc4, width=85)
ent1.place(x=350, y=12)


#placeholder buttons
btn1 = tkinter.Button(uc4, text='Open', height = 1, width = 9, command=combo)

scrollbar = Scrollbar(uc4)
scrollbar.pack(side=RIGHT, fill=Y)
#atatch scrolbar
tree.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tree.yview)
#Radiobuttons

def normal():
    ent1.configure(state='normal')
    btn1.configure(state='normal')
 
# function 'disabled' has to reuse modified code from the standard 'open' function, it uses a fixed file directory
def disabled(): 
    ent1.configure(state='disabled')
    btn1.configure(state='disabled')
    kill_table()
    global headings
    global data
    global tree
    global scrollbar

    open_file=('Results.csv')
    with open(open_file, 'Ur') as f:
        RawCsv = list(tuple(rec) for rec in csv.reader(f, delimiter=','))

    headings=RawCsv[0]
    data=RawCsv[1:]

    
    tree = ttk.Treeview(uc4,selectmode='extended', columns=headings, show='headings',height=50)
    for title in headings:
        tree.heading(title, text=title, command=lambda c=title: sortby(tree, c, 0))

    for student in data:
        tree.insert('', 'end', values=student)

    tree.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)

    repack()

#sets the radiobuttons to be mutually exclusive
var = IntVar()
R1 = Radiobutton(uc4, text="Default data", variable=var, value=1, command = disabled)
R1.place(x=35, y=10)

lbl3 = tkinter.Label(uc4, text='|',font=('Arial',12), fg='gray50')
lbl3.place(x=145, y=8)

R2 = Radiobutton(uc4, text="Custom file", variable=var, value=2, command = normal)
R2.place(x=170, y=10)


#invokes and packs widgets
R1.invoke()
btn1.place(x=890, y=8)
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack()
tree.pack()


#mainloop
uc4.mainloop()
