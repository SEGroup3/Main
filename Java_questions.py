#the GUI to ask Java questions
#'number' not 'Student_No because I lost rock paper scissors

from tkinter import *
import tkinter.messagebox as tk
import pickle
import students
import auto_test
import Personality

class Java_Questions(Frame):

    def __init__(self,master,number):

        Frame.__init__(self,master)
        master.title("Java Programming Questions")
        self.grid()
        self.header()
        self.q_header()
        self.q1()
        self.q2()
        self.q3()
        self.q4()
        #self.q5()
        self.number = number
        self.submit_Button()
        self.clear_Button()

    def header(self):
        #a header to appear at the top of the window
        self.pack(pady = 20, padx = 20)
        lblHeader = Label(self, text = "Java Programming Questions: ",
                          font = ('MS', 10, 'bold'))
        lblHeader.grid(row = 0, column = 0, columnspan = 2, sticky = NW)

    def q_header(self):
        #the first line of questions
        line1 = Label(self, text = "Review the following Java code and choose the correct answer from the options shown.",
                      font = ("MS", 8))
        line1.grid(row = 2, column = 0, sticky = W)
        line2 = Label(self, text = "When you are finished, click Submit and your answers will be saved.", font = ('MS', 8))
        line2.grid(row = 3, column = 0, sticky = W)
        line3 = Label(self, text= "", font = ('MS', 8))
        line3.grid(row = 4, column = 0, sticky = W)

    def submit_Button(self):
        #a button to allow the user to submit answers
        butSubmit = Button(self, text = 'Submit', font = ('MS', 8, 'bold'))
        butSubmit['command']=self.assess_Results
        butSubmit.grid(row = 99, column = 1, columnspan = 1, sticky = N)
    
    def clear_Button(self):
        #a button to clear the form
        butClear = Button(self, text = 'Clear All', font = ('MS',8, 'bold'))
        butClear['command']=self.clear_All
        butClear.grid(row = 99, column = 0, columnspan = 2, sticky = N)

    def q1(self):
        line1 = Label(self, text = "Question 1: Which statement is true for the class java.util.ArrayList?",
                      font = ('MS', 8))
        line1.grid(row = 5, column = 0, columnspan = 2, sticky = W)

        self.varQ1 = IntVar()

        A1Q1 = Label(self, text = "A. The elements in the collection are ordered.",
                   font = ('MS', 8))
        A1Q1.grid(row=6, column = 0, columnspan = 1, sticky = W) 
        R1Q1 = Radiobutton(self, variable = self.varQ1, value=4)
        R1Q1.grid(row= 6, column = 1)

        A2Q1 = Label(self, text = "B. The collection is guaranteed to be immutable.",
                   font = ('MS', 8))
        A2Q1.grid(row = 6, column = 2, columnspan = 1, sticky = W)
        R2Q1 = Radiobutton(self, variable = self.varQ1, value=3)
        R2Q1.grid(row= 6, column = 3)

        A3Q1 = Label(self, text = "C. The elements in the collection are guaranteed to be unique.",
                     font = ('MS', 8))
        A3Q1.grid(row = 7, column = 0, columnspan = 1, sticky = W)
        R3Q1 = Radiobutton(self, variable = self.varQ1, value=2)
        R3Q1.grid(row= 7, column = 1)


        A4Q1 = Label(self, text = "D. The elements in the collection are accessed using a unique key.",
                     font = ('MS',8))
        A4Q1.grid(row=7, column = 2, columnspan = 1, sticky = W)
        R4Q1 = Radiobutton(self, variable = self.varQ1, value=1)
        R4Q1.grid(row= 7, column = 3)

        buffer = Label(self, text = "", font = ('MS', 8))
        buffer.grid(row = 8, column = 0)


    def q2(self):
        line1 = Label(self,text = "Question 2: If you want your condition to depend upon two conditions BOTH being true,", font = ('MS', 8))
        line1.grid(row =9, column = 0, sticky = W)
        line2 = Label(self,text = "which is the correct notation to put between the two Boolean statements?", font = ('MS', 8))
        line2.grid(row =10, column = 0, sticky = W)

        self.varQ2 = IntVar()

        A1Q2 = Label(self, text = "A. !=",font = ('MS', 8))
        A1Q2.grid(row=11, column = 0, columnspan = 1, sticky = W) 
        R1Q2 = Radiobutton(self, variable = self.varQ2, value=4)
        R1Q2.grid(row= 11, column = 1)

        A1Q2 = Label(self, text = "B. ||",font = ('MS', 8))
        A1Q2.grid(row=11, column = 2, columnspan = 1, sticky = W) 
        R1Q2 = Radiobutton(self, variable = self.varQ2, value=3)
        R1Q2.grid(row= 11, column = 3)

        A3Q2 = Label(self, text = "C. &&",font = ('MS', 8))
        A3Q2.grid(row = 12, column = 0, columnspan = 1, sticky = W)
        R3Q2 = Radiobutton(self, variable = self.varQ2, value=2)
        R3Q2.grid(row= 12, column = 1)

        A4Q2 = Label(self, text = "D. and if",font = ('MS',8))
        A4Q2.grid(row=12, column = 2, columnspan = 1, sticky = W)
        R4Q2 = Radiobutton(self, variable = self.varQ2, value=1)
        R4Q2.grid(row= 12, column = 3)

        buffer = Label(self, text = "", font = ('MS', 8))
        buffer.grid(row = 13, column = 0)
        
    def q3(self):

        line1 = Label(self, text = "Question 3: What will be the output of the following program?",
                      font = ('MS', 8))
        line1.grid(row = 14, column = 0, sticky = W)
        
        photo = PhotoImage(file="q3.gif")
        w = Label(self, image=photo)
        w.photo = photo #binding widget to tkinter object
        w.grid(row = 15, column = 0, columnspan = 4, sticky = W)

        self.varQ3 = IntVar()

        A1Q3 = Label(self, text = "A. 'odd' will always be displayed. ",font = ('MS', 8))
        A1Q3.grid(row=16, column = 0, columnspan = 1, sticky = W) 
        R1Q3 = Radiobutton(self, variable = self.varQ3, value=4)
        R1Q3.grid(row= 16, column = 1)

        A1Q3 = Label(self, text = "B. NullPointerException at runtime.",font = ('MS', 8))
        A1Q3.grid(row=16, column = 2, columnspan = 1, sticky = W) 
        R1Q3 = Radiobutton(self, variable = self.varQ3, value=3)
        R1Q3.grid(row= 16, column = 3)

        A3Q3 = Label(self, text = "C. 'even' will always be displayed.",font = ('MS', 8))
        A3Q3.grid(row = 17, column = 0, columnspan = 1, sticky = W)
        R3Q3 = Radiobutton(self, variable = self.varQ3, value=2)
        R3Q3.grid(row= 17, column = 1)

        A4Q3 = Label(self, text = "D. '1' will always be displayed. ",font = ('MS',8))
        A4Q3.grid(row=17, column = 2, columnspan = 1, sticky = W)
        R4Q3 = Radiobutton(self, variable = self.varQ3, value=1)
        R4Q3.grid(row= 17, column = 3)

        buffer = Label(self, text = "", font = ('MS', 8))
        buffer.grid(row = 18, column = 0)

    def q4(self):
        line1 = Label(self, text = "Question 4: What will be the output of the following program?",
                      font = ('MS', 8))
        line1.grid(row = 19, column = 0, sticky = W)
        
        photo = PhotoImage(file="q4.gif")
        w = Label(self, image=photo)
        w.image = photo #binding widget to tkinter object
        w.grid(row = 20, column = 0, columnspan = 4, sticky = W)

        self.varQ4 = IntVar()

        A1Q4 = Label(self, text = "A. 1 and 2",font = ('MS', 8))
        A1Q4.grid(row=21, column = 0, columnspan = 1, sticky = W) 
        R1Q4 = Radiobutton(self, variable = self.varQ4, value=4)
        R1Q4.grid(row= 21, column = 1)

        A1Q4 = Label(self, text = "B. 2 and 3",font = ('MS', 8))
        A1Q4.grid(row=21, column = 2, columnspan = 1, sticky = W) 
        R1Q4 = Radiobutton(self, variable = self.varQ4, value=3)
        R1Q4.grid(row= 21, column = 3)

        A3Q4 = Label(self, text = "C. 3 and 4",font = ('MS', 8))
        A3Q4.grid(row = 22, column = 0, columnspan = 1, sticky = W)
        R3Q4 = Radiobutton(self, variable = self.varQ4, value=2)
        R3Q4.grid(row= 22, column = 1)

        A4Q4 = Label(self, text = "D. 1 and 4",font = ('MS',8))
        A4Q4.grid(row=22, column = 2, columnspan = 1, sticky = W)
        R4Q4 = Radiobutton(self, variable = self.varQ4, value=1)
        R4Q4.grid(row= 22, column = 3)
        
        buffer = Label(self, text = "", font = ('MS', 8))
        buffer.grid(row = 23, column = 0)

    def q5(self):
        line1 = Label(self, text = "Question 5: What will be the output of the following program?",
                      font = ('MS', 8))
        line1.grid(row = 24, column = 0, sticky = W)
        
        photo = PhotoImage(file="q5.gif")
        w = Label(self, image=photo)
        w.image = photo #binding widget to tkinter object
        w.grid(row = 25, column = 0, columnspan = 4, sticky = W)

        self.varQ5 = IntVar()

        A1Q4 = Label(self, text = "A. Zero",font = ('MS', 8))
        A1Q4.grid(row=26, column = 0, columnspan = 1, sticky = W) 
        R1Q4 = Radiobutton(self, variable = self.varQ5, value=4)
        R1Q4.grid(row= 26, column = 1)

        A1Q4 = Label(self, text = "B. Twelve",font = ('MS', 8))
        A1Q4.grid(row=26, column = 2, columnspan = 1, sticky = W) 
        R1Q4 = Radiobutton(self, variable = self.varQ5, value=3)
        R1Q4.grid(row= 26, column = 3)

        A3Q4 = Label(self, text = "C. Default",font = ('MS', 8))
        A3Q4.grid(row = 27, column = 0, columnspan = 1, sticky = W)
        R3Q4 = Radiobutton(self, variable = self.varQ5, value=2)
        R3Q4.grid(row= 27, column = 1)

        A4Q4 = Label(self, text = "D. Compilation fails",font = ('MS',8))
        A4Q4.grid(row=27, column = 2, columnspan = 1, sticky = W)
        R4Q4 = Radiobutton(self, variable = self.varQ5, value=1)
        R4Q4.grid(row= 27, column = 3)

        buffer = Label(self, text = "", font = ('MS', 8))
        buffer.grid(row = 28, column = 0)

    def assess_Results(self):
        countAll = 0
        if self.varQ1.get() == 4:
            countAll += 1
        if self.varQ2.get() == 4:
            countAll += 1
        if self.varQ3.get() == 4:
            countAll += 1
        if self.varQ4.get() == 4:
            countAll +=1
##        if self.varQ5.get() == 4:
##            countAll +=1 

        if countAll == 0:
            tk.showinfo("Programming Questions", "You scored 0/4(0%).")
            self.incompetent()
        if countAll == 1:
            tk.showinfo("Programming Questions", "You scored 1/4(25%).")
            self.incompetent()
        if countAll == 2:
            tk.showinfo("Programming Questions", "You scored 2/4(50%).")
            self.competent()
        if countAll == 3:
            tk.showinfo("Programming Questions", "You scored 3/4(75%).")
            self.competent()
        if countAll == 4:
            tk.showinfo("Programming Questions", "You scored 4/4(100%).")
            self.competent()

    def incompetent(self):
        self.master.destroy()
        self.next_Screen()

    def competent(self):
        with open("stu_dict.pkl", "rb") as db:
            stu_dict=pickle.load(db)
        stu_dict[self.number].changeCompetency(True)
        with open ("stu_dict.pkl", "wb") as db:
            pickle.dump(stu_dict, db)
        #self.master.destroy()
        self.next_Screen()
    
        
##        print (self.number)
##        with open ("stu_dict.pkl", "rb") as db:
##           stu_dict = pickle.load(db)
##        print (stu_dict[self.number])

        
    def clear_All(self):
        response = tk.askquestion("Programming Questions", "Are you sure you wish to clear all of your answers?")
        if response == 'yes':
            self.varQ1.set(0)
            self.varQ2.set(0)
            self.varQ3.set(0)
            self.varQ4.set(0)
            #self.varQ5.set(0)
            tk.showinfo("Programming Questions", "All answers cleared.")
        else:
            return
        
    def next_Screen(self):
        Personality.Personality(self.master, number =number )
        self.master.destroy()


#Main
if __name__ == '__main__':
##TESTING
##    s_dict = {}
##    student_list = auto_test.list_of_students(15)
##    for item in student_list:
##        s_dict[item.number] = item
##        number_arg = item.number
##    with open ("stu_dict.pkl", "wb+") as db:
##            pickle.dump(s_dict, db)
    root = Tk()
    app = Java_Questions(root, number)
    root.mainloop()
