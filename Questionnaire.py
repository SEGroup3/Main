from tkinter import *
import tkinter.messagebox
from students import *
import pickle # to save 
import glob #allow you to find the text files and import them 
import os,sys # allow you to use the os directory to find files
import Java_questions
import Python_questions
import Personality

class Questionnaire (Frame):
    #GUI Setup
    def __init__(self, master):
        # Initialise Questionnaire Class
        super(Questionnaire, self).__init__(master)
        self.master= master

        self.master.title("Teamwork Questionnaire")
        self.grid()
       
        self.get_student_info()
        self.get_team_exp_quest()
        self.create_button()
        self.stu_dict = self.startup()
        self.master.mainloop()

    def startup(self):
        if os.path.isfile('stu_dict.pkl'):
            with open("stu_dict.pkl", "rb") as f:
                stu_dict = pickle.load(f) #load 
                return stu_dict
        else:
            stu_dict = dict()
            return stu_dict
           

    def get_student_info(self):
        '''create button, text, and entry widgets'''
        #pack sides
    
        #Get info
        self.ask_firstname = Label(self, text='Forename:', font = ('MS', 8, 'bold'))
        self.ask_firstname.grid(row=2, column = 1, columnspan=1, rowspan =2, sticky = NW)

        self.get_firstname = Entry(self)
        self.get_firstname.grid(row=2, column = 4, columnspan=3, sticky=NE)

        self.ask_surname = Label(self, text='Surname:', font = ('MS', 8, 'bold'))
        self.ask_surname.grid(row=3, column = 1, columnspan=1, rowspan =2, sticky = NW)

        self.get_surname = Entry(self)
        self.get_surname.grid(row=3, column = 4, columnspan=3, sticky=NE)

        self.ask_numb = Label(self, text='Student Number:', font = ('MS', 8, 'bold'))
        self.ask_numb.grid(row=4, column = 1, columnspan=1, rowspan =2, sticky = NW)

        self.get_numb = Entry(self)
        self.get_numb.grid(row=4, column = 4, columnspan=3, sticky=NE)

        self.ask_email = Label(self, text='Email:', font = ('MS', 8, 'bold'))
        self.ask_email.grid(row=5, column = 1, columnspan=1, rowspan =2, sticky = NW)

        self.get_email = Entry(self)
        self.get_email.grid(row=5, column = 4, columnspan=3, sticky=NE)

        

    def get_team_exp_quest (self):
        # Create widgets to ask Team Expereince Questions
        qu1 = 'Do you feel you have prior\n computing experience?'
        ExpHead = Label(self, text= 'Prior Computing Experience:', font=('MS', 8, 'bold'))
        ExpHead.grid(row= 7, column= 1, rowspan= 1, sticky = NE)

        lblStrAgr = Label(self, text = 'Java', font = ('MS', 8, 'bold'))
        lblStrAgr.grid(row = 7, column = 4, rowspan= 1)

        lblStrAgr2 = Label(self, text = 'Python', font = ('MS', 8, 'bold'))
        lblStrAgr2.grid(row = 7, column = 5, rowspan = 1)

        lblStrArg3 = Label(self, text = 'None', font = ('MS', 8, 'bold'))
        lblStrArg3.grid(row = 7, column = 6, rowspan = 1, padx=10)

        lblQu1 = Label(self, text= qu1, font=('MS', 8, ''))
        lblQu1.grid(row= 8, column= 1, rowspan= 1)
        self.varQ1 = 0
        self.varQ1 = IntVar()

        self.R1Q1 = Radiobutton(self, variable=self.varQ1, value=4)
        self.R1Q1.grid(row=8, column=4)

        self.R2Q1 = Radiobutton(self, variable=self.varQ1, value=3)
        self.R2Q1.grid(row=8, column=5)

        self.R3Q1 = Radiobutton(self, variable=self.varQ1, value=2)
        self.R3Q1.grid(row=8, column=6)

    def create_button (self,):   
        self.submit_bttn = Button(self, text= 'Submit', command = self.store_response, font=('MS', 8, 'bold')).grid(row = 10, column = 4, sticky = S)

    def store_response(self):
        str_msg = ""
        if self.get_firstname.get().isalpha():
            firstname= self.get_firstname.get()
        else: str_msg = "Please add first name \n"
        if self.get_surname.get().isalpha():
            surname= self.get_surname.get()
        else: str_msg = str_msg + "Please add surname \n"
        if self.get_numb.get().lower().strip('c').isdigit():
            number = self.get_numb.get()
        else: str_msg = str_msg + "Please add number \n"
        if self.get_email.get() != "":
            email = self.get_email.get()
        else: str_msg = str_msg + "Please add email \n"
        if (self.varQ1.get() ==0):
            str_msg = str_msg + "Please answer experience question \n"
          
        if str_msg == "":
           # tkinter.messagebox.showinfo("Questionnaire", "Questionnaire Submitted")
            student = Student(firstname, surname, number, email)
            
            self.stu_dict[number] = student
            with open("stu_dict.pkl","wb") as out:
                pickle.dump(self.stu_dict, out) #save file     

            if (self.varQ1.get() ==4):
                java_window = Java_questions.Java_Questions(self.master, number)
                self.destroy()
            elif (self.varQ1.get() ==3):
                Python_questions.Python_Questions(self.master, number)
                self.destroy()    
            elif (self.varQ1.get() ==2):
                Personality.Personality(self.master, number)
                self.destroy()   
                

            #self.clear_response
        else:
            tkinter.messagebox.showinfo("Please fix the following errors", str_msg)
      
        
    def clear_response(self):
        self.get_firstname.delete(0,END)
        self.get_surname.delete(0,END)
        self.get_numb.delete(0,END)
        self.get_email.delete(0,END)
        self.R1Q1.set(0)
        self.R2Q1.set(0)

  
    
     
#main
if __name__ == '__main__':
    
    app = Questionnaire()
    
