from tkinter import *
import tkinter.messagebox
from students import *
import pickle # to save 
import glob #allow you to find the text files and import them 
import os,sys # allow you to use the os directory to find files
import Questionnaire

class Main_Menu (Frame):

    def __init__(self, master):

        super(Main_Menu, self).__init__(master)

        self.master = master
        self.grid()

        self.student_start()
        self.lecturer_start()


    def student_start (self):
    #Create student access buttons'''
        self.pack(pady = 150, padx = 120)
        self.students = Label (self, text = 'Students Section', font = ('MS',12, 'bold'))
        self.students.grid (row =1, column = 2, pady= 10)
        self.stu_but = Button (self, text = "Click Here to Start", command = self.launch_student)
        self.stu_but.grid(row = 2, column = 2)
        self.space1 = Label(self, text = '    ', font=('MS', 8, 'bold'))
        self.space1.grid(row= 3, column = 0, sticky = W)

    def lecturer_start (self):
        
        self.lecturer = Label (self, text = 'Lecturer Section', font = ('MS',12, 'bold'))
        self.lecturer.grid (row =5, column = 2, pady= 10)
        self.login_label = Label(self, text = 'Username', font = ('ms', 8,))
        self.login_label.grid (row = 6, column =1)
        self.login = Entry (self, width = 30)
        self.login.grid (row= 6, column = 2)
        self.passw_label = Label(self, text = 'Password', font = ('ms', 8,))
        self.passw_label.grid( row =7, column = 1)
        self.password = Entry(self, width = 30, show = "*")
        self.password.grid( row = 7, column = 2)

        self.stu_but = Button (self, text = "Login")
        self.stu_but.grid(row = 8, column = 2)

    def launch_student (self):
        new_window = Tk()
        Questionnaire.Questionnaire(new_window)
        self.master.destroy()
 

if __name__ == '__main__':
    root = Tk()
    root.title("The Sorting Hat")
    app = Main_Menu(root)
    root.mainloop()
