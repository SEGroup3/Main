from tkinter import *
import tkinter.messagebox
import Student
class Questionnaire (Frame):
    #GUI Setup
    def __init__(self, master):
        # Initialise Questionnaire Class

        
        super(Questionnaire, self).__init__(master)
        self.grid()
       # self.create_widgets()
        self.create_student_info()
        self.create_team_Exp_Quest()
        self.create_button()

  #  def create_widgets(self):
        
        #create instruction label
        #self.inst_lbl = 
    def create_student_info(self):
        '''create button, text, and entry widgets'''
        #pack sides
        self.pack(pady = 30, padx = 30)
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

    def create_button (self):   
        self.submit_bttn = Button(self, text= 'Submit', command = self.storeResponse, font=('MS', 8, 'bold')).grid(row = 10, column = 4, sticky = S)
        
        
    def storeResponse (self):
        firstname= self.get_firstname.get()
        surname= self.get_surname.get()
        number = self.get_numb.get()
        email = self.get_email.get()

        messagebox.showinfo("Questionnaire", "Questionnaire Submitted")
        self.clearResponse()
        student = Student(firstname, surname, number, email)
        getStudentInfo()
   # def clear_response (self):
	#self.GetName.delete(0,END)
	#self.R1Q1.set(0)
	#self.R2Q1.set(0)

    #def storeResponse(self):
	#Store the questionnaire results
	#index = self.GetName.curselection()[0]
	#strProg = str(self.GetName.get(index))
	#strMsg = ""
		
	#if strProg == "":
       #     strMsg = "Please Enter a Name."
		
	#if (self.varQ1.get() ==0):
       #     strMsg = strMsg + "You need to answer experience question."

    
     
#main
root = Tk()
root.title("Teamwork Questionnaire")
app = Questionnaire(root)
root.mainloop()
