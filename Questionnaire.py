from tkinter import *
import tkinter.messagebox
from students import *
import pickle # to save scoreboard and wordsets
import glob #to allow me to find the text files and import them 
import os,sys # to allow it to use the os directory to find files

class Questionnaire (Frame):
    #GUI Setup
    def __init__(self, master):
        # Initialise Questionnaire Class

        
        super(Questionnaire, self).__init__(master)
        self.master = master
        self.grid()
       
        self.create_student_info()
        self.create_team_Exp_Quest()
        self.create_button()
        self.stu_dict = self.startup()


    def startup(self):
        if os.path.isfile('stu_dict.pkl'):
            with open("stu_dict.pkl", "rb") as f:
                stu_dict = pickle.load(f) #load high scores file or create it if new
                return stu_dict
        else:
            stu_dict = dict()
            return stu_dict
           

    def create_student_info(self):
        '''create button, text, and entry widgets'''
        #pack sides
        self.pack(pady = 40, padx = 40)
        #Get info
        self.ask_firstname = Label(self, text='First Name:', font = ('MS', 8, 'bold'))
        self.ask_firstname.grid(row=2, column = 1, columnspan=1, rowspan =2, sticky = NW)

        self.get_firstname = Entry(self)
        self.get_firstname.grid(row=2, column = 4, columnspan=1, sticky=NE)

        self.ask_surname = Label(self, text='Surname:', font = ('MS', 8, 'bold'))
        self.ask_surname.grid(row=3, column = 1, columnspan=1, rowspan =2, sticky = NW)

        self.get_surname = Entry(self)
        self.get_surname.grid(row=3, column = 4, columnspan=1, sticky=NE)

        self.ask_numb = Label(self, text='Student Number:', font = ('MS', 8, 'bold'))
        self.ask_numb.grid(row=4, column = 1, columnspan=1, rowspan =2, sticky = NW)

        self.get_numb = Entry(self)
        self.get_numb.grid(row=4, column = 4, columnspan=1, sticky=NE)

        self.ask_email = Label(self, text='Email:', font = ('MS', 8, 'bold'))
        self.ask_email.grid(row=5, column = 1, columnspan=1, rowspan =2, sticky = NW)

        self.get_email = Entry(self)
        self.get_email.grid(row=5, column = 4, columnspan=1, sticky=NE)

        

        '''self.listProg = Listbox(self, height= 3)
        scroll = Scrollbar(self, command= self.listProg.yview)
        self.listProg.configure(yscrollcommand=scroll.set)

        self.listProg.grid(row=0, column =2, columnspan= 2, sticky = NE)
        scroll.grid(row=0, column=4, sticky= W)

        for item in ["CS", "CS with", "BIS", "SE", "Joints", ""]:
            self.listProg.insert(END, item)

        self.listProg.selection_set(END)'''

    def create_team_Exp_Quest (self):
        # Create widgets to ask Team Expereince Questions
        qu1 = '1. Do you feel you have prior\n computing experience?'
        ExpHead = Label(self, text= 'Prior Computing Expereince:', font=('MS', 8, 'bold'))
        ExpHead.grid(row= 7, column= 1, rowspan= 1, sticky = NE)

        lblStrAgr = Label(self, text = 'Yes', font = ('MS', 8, 'bold'))
        lblStrAgr.grid(row = 7, column = 4, rowspan= 1)

        lblStrAgr2 = Label(self, text = 'No', font = ('MS', 8, 'bold'))
        lblStrAgr2.grid(row = 7, column = 5, rowspan = 1)
        
        lblQu1 = Label(self, text= qu1, font=('MS', 8, ''))
        lblQu1.grid(row= 8, column= 1, rowspan= 1)

        self.varQ1 = IntVar()

        R1Q1 = Radiobutton(self, variable=self.varQ1, value=4)
        R1Q1.grid(row=8, column=4)

        R2Q1 = Radiobutton(self, variable=self.varQ1, value=3)
        R2Q1.grid(row=8, column=5)

    def create_button (self,):   
        self.submit_bttn = Button(self, text= 'Submit', command = self.store_response, font=('MS', 8, 'bold')).grid(row = 10, column = 4, sticky = S)

    def store_response(self):
        str_msg = ""
        if self.get_firstname.get().isalpha():
            firstname= self.get_firstname.get()
        else: str_msg = "Please Add First Name \n"
        if self.get_surname.get().isalpha():
            surname= self.get_surname.get()
        else: str_msg = str_msg + "Please Add Surname \n"
        if self.get_numb.get().lower().strip('c').isdigit():
            number = self.get_numb.get()
        else: str_msg = str_msg + "Please Add Number \n"
        if self.get_email.get() != "":
            email = self.get_email.get()
        else: str_msg = str_msg + "Please Add Email \n"
        if (self.varQ1.get() ==0):
            str_msg = str_msg + "Please Answer Experience Question \n"
          
        if str_msg == "":
            tkinter.messagebox.showinfo("Questionnaire", "Questionnaire Submitted", command = self.master.destroy())
            student = Student(firstname, surname, number, email)
            print(student)
            self.stu_dict[number] = student
            with open("stu_dict.pkl","wb") as out:
                pickle.dump(self.stu_dict, out) #save file     
            for item in self.stu_dict:
                print (self.stu_dict[item])
            
            #self.destroy()    

            #self.clear_response
        else:
            tkinter.messagebox.showinfo("Please Fix the Following Errors", str_msg)
      
        
    def clear_response(self):
        self.get_firstname.delete(0,END)
        self.get_surname.delete(0,END)
        self.get_numb.delete(0,END)
        self.get_email.delete(0,END)
        self.R1Q1.set(0)
        self.R2Q1.set(0)

  
    
     
#main
if __name__ == '__main__':
    root = Tk()
    root.title("Teamwork Questionnaire")
    app = Questionnaire(root)
    root.mainloop()
