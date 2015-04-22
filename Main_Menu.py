from tkinter import *
import tkinter.messagebox
from students import *
import pickle # to save 
import glob #allow you to find the text files and import them 
import os,sys # allow you to use the os directory to find files
import Questionnaire
import Lecturer_Menu

class Main_Menu (Frame):

    def __init__(self, master):

        super(Main_Menu, self).__init__(master)
        self.master = master
        self.master.title("The Sorting Hat")
        self.grid()
        self.hat()
        self.student_start()
        self.lecturer_start()

    def hat(self):
        photo = PhotoImage(file="hat.gif")
        w = Label(self, image = photo)
        w.photo = photo
        w.grid(row = 1, column = 0, sticky = NSEW)


    def student_start (self):
    #Create student access buttons'''
        self.grid(pady = 40, padx = 40)
        self.students = Label (self, text = 'Student Section', font = ('MS',12, 'bold'))
        self.students.grid (row =2, column = 0, pady= 10)
        self.stu_but = Button (self, text = "Click Here to Start", command = self.launch_student)
        self.stu_but.grid(row = 3, column = 0)
        self.space1 = Label(self, text = '    ', font=('MS', 8, 'bold'))
        self.space1.grid(row= 4, column = 0, sticky = W)

    def lecturer_start (self):
        
        self.lecturer = Label (self, text = 'Lecturer Section', font = ('MS',12, 'bold'))
        self.lecturer.grid (row =6, column = 0, pady= 10)
        self.login_label = Label(self, text = 'Username', font = ('ms', 8,))
        self.login_label.grid (row = 7, column =0)
        self.login = Entry (self, width = 30)
        self.login.grid (row= 8, column = 0)
        self.passw_label = Label(self, text = 'Password', font = ('ms', 8,))
        self.passw_label.grid( row =9, column = 0)
        self.password = Entry(self, width = 30, show = "*")
        self.password.grid( row = 10, column = 0)

        self.stu_but = Button (self, text = "Login", command = self.launch_lecturer)
        self.stu_but.grid(row = 11, column = 0)

    def launch_student (self):
        self.grid_forget()
        self.destroy()
        Questionnaire.Questionnaire(self.master)

        
    def launch_lecturer (self):
        with open("credentials.pkl", "rb") as user_pass:
            credentials = pickle.load(user_pass)

        if self.login.get() in credentials:
            if credentials[self.login.get()] == self.password.get():
                self.success()

            else:
                self.failure(cause = "Inccorrect password")

        else:
            self.failure(cause = "Incorrect username")


    def failure (self, cause):
        tkinter.messagebox.showinfo("Error", cause)
           
        
    def success (self):
        
        self.grid_forget()
        self.destroy()
        Lecturer_window = Lecturer_Menu.Lecturer_Menu(self.master)
 

if __name__ == '__main__':
    root = Tk()
    root.title("The Sorting Hat")
    app = Main_Menu(root)
    root.mainloop()
