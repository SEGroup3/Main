#the GUI to ask students Python questions, assess and save the results

from tkinter import *
import tkinter.messagebox as tk
import pickle
import students
import auto_test

class results_viewer(Frame):
    def __init__(self,master):        
        Frame.__init__(self,master)
        self.grid()
        self.header()
        self.exit_button()
        self.print_button()

    def header(self):
        self.pack(pady = 20, padx = 20)
        lblHeader = Label(self, text = "Table of Results", font=('MS', 10, 'bold'))
        lblHeader.grid(row =0, column = 0, columnspan = 2, sticky = NW)

    def print_button(self):
        butPrint = Button(self, text = "Print", font = ('MS', 8, 'bold'))
        butPrint['command']=self.print_results
        butPrint.grid(row=99, column = 0, columnspan= 1, sticky = N)

    def print_results(self):
        db = shelve.open('responsedb')
        for line in db:
            print (line, end = ",")
        db.close        

    def close_window(self):
        self.master.destroy()
        
    def exit_button(self):
        #a button to quit the results viewer
        butSubmit = Button(self, text = 'Quit', font = ('MS', 8, 'bold'))
        butSubmit['command']=self.close_window
        butSubmit.grid(row = 99, column = 1, columnspan = 1, sticky = N)

class Python_Questions (Frame):

    def __init__(self,master,student_No):

        Frame.__init__(self,master)
        self.grid()
        self.header()
        self.q_header()
        self.q1()
        self.q2()
        self.q3()
        self.q4()
        self.student_No = student_No
        #self.q5()
        self.submit_Button()
        self.clear_Button()
        self.view_Button()
        self.master = master

    def header(self):
        
        self.pack(pady = 20, padx = 20)
        lblHeader = Label(self, text = "Python Programming Questions: ", font = ('MS', 10, 'bold'))
        lblHeader.grid(row = 0, column = 0, columnspan = 2, sticky = NW)

    def q_header(self):
        
        line1 = Label(self, text = "Assume you are interacting with the Python interactive shell in version 3.x", font = ('MS',8))
        line1.grid(row = 2, column = 0, sticky = W)
        line2 = Label(self, text = "with the following statements. For each statement you input, the shell will execute", font = ('MS',8))
        line2.grid(row = 3, column = 0, sticky = W)
        line3 = Label(self, text = "immediately return a result. In the text box, enter the expected output for each statement.",
                    font = ('MS', 8))
        line3.grid(row = 4, column = 0, sticky = W)
            
    def q1(self):
        q1header = Label(self,text = "Question 1:", font = ('MS',8, 'bold'))
        q1header.grid(row = 6, column = 0, sticky = W)
        q1body1 = Label(self,text = ">>> a list = range(0,20,2)", font = ('MS', 8))
        q1body1.grid(row = 7, column = 0, sticky = W)
        q1body2 = Label(self,text = ">>> blist = [2*x for x in alist if x%3 ==0]", font = ('MS', 8))
        q1body2.grid(row = 8, column = 0, sticky = W)
        q1body3 = Label(self,text = ">>> blist", font = ('MS', 8))
        q1body3.grid(row = 9, column = 0, sticky = W)

        self.q1answer = Entry(self, width = 30)

        self.q1answer.grid(row = 10, column = 0, columnspan = 3, sticky = E)

    def q2(self):

        q2header = Label(self,text = "Question 2:", font = ('MS',8, 'bold'))
        q2header.grid(row = 11, column = 0, sticky = W)
        q2body1 = Label(self,text = ">>> import re", font = ('MS', 8))
        q2body1.grid(row = 12, column = 0, sticky = W)
        q2body2 = Label(self,text = ">>> words = 'cat, cow, dog, dig, ding, song, sing, tower, grow, glow, lower'", font = ('MS', 8))
        q2body2.grid(row = 13, column = 0, sticky = W)
        q2body3 = Label(self, text = ">>> re.findall(r'(\w+), grow, (\w+)', words)", font = ('MS', 8))
        q2body3.grid(row = 14, column = 0, sticky = W)

        self.q2answer = Entry(self, width = 30)

        self.q2answer.grid(row = 15, column = 0, columnspan = 3, sticky = E)

    def q3(self):
        
        q3header = Label(self,text = "Question 3:", font = ('MS',8, 'bold'))
        q3header.grid(row = 16, column = 0, sticky = W)
        q3body1 = Label(self,text = ">>> global a", font = ('MS', 8))
        q3body1.grid(row = 17, column = 0, sticky = W)
        q3body2 = Label(self,text = ">>> a = 20", font = ('MS', 8))
        q3body2.grid(row = 18, column = 0, sticky = W)
        q3body3 = Label(self, text = ">>> def g(b):", font = ('MS', 8))
        q3body3.grid(row = 19, column = 0, sticky = W)
        q3body4 = Label(self, text = "       a=b", font = ('MS', 8))
        q3body4.grid(row = 20, column = 0, sticky = W)
        q3body5 = Label(self, text = ">>>g(100)", font = ('MS', 8))
        q3body5.grid(row = 21, column = 0, sticky = W)
        q3body6 = Label(self, text = ">>>print(a)", font = ('MS', 8))
        q3body6.grid(row = 22, column = 0, sticky = W)

        self.q3answer = Entry(self, width = 30)

        self.q3answer.grid(row = 23, column = 0, columnspan = 3, sticky = E)

    def q4(self):

        q4header = Label(self,text = "Question 4:", font = ('MS',8, 'bold'))
        q4header.grid(row = 24, column = 0, sticky = W)
        q4body1 = Label(self,text = ">>> a=[1,2,3]", font = ('MS', 8))
        q4body1.grid(row = 25, column = 0, sticky = W)
        q4body2 = Label(self,text = ">>> if a: ", font = ('MS', 8))
        q4body2.grid(row = 26, column = 0, sticky = W)
        q4body3 = Label(self, text = "        print ('a is not None')", font = ('MS', 8))
        q4body3.grid(row = 27, column = 0, sticky = W)
        q4body4 = Label(self, text = "else:", font = ('MS', 8))
        q4body4.grid(row = 28, column = 0, sticky = W)
        q4body5 = Label(self, text = "        print ('a is None')", font = ('MS', 8))
        q4body5.grid(row = 29, column = 0, sticky = W)

        self.q4answer = Entry(self, width = 30)

        self.q4answer.grid(row = 30, column = 0, columnspan = 3, sticky = E)
        buffer = Label(self, text = "", font = ('MS', 8))
        buffer.grid(row =98, column = 0)

    def q5(self):

        q5header = Label(self,text = "Question 5:", font = ('MS',8, 'bold'))
        q5header.grid(row = 31, column = 0, sticky = W)
        q5body1 = Label(self,text = ">>>for i in range(10,25,5):", font = ('MS', 8))
        q5body1.grid(row = 32, column = 0, sticky = W)
        q5body2 = Label(self,text = "            print (i, ': ')", font = ('MS', 8))
        q5body2.grid(row = 33, column = 0, sticky = W)
        q5body3 = Label(self, text = "           for j in range (i/5):", font = ('MS', 8))
        q5body3.grid(row = 34, column = 0, sticky = W)
        q5body4 = Label(self, text = "                   print (i/5)", font = ('MS', 8))
        q5body4.grid(row = 35, column = 0, sticky = W)
        q5body5 = Label(self, text = "           print("")", font = ('MS', 8))
        q5body5.grid(row = 36, column = 0, sticky = W)


        self.q5answer = Entry(self, width = 30)

        self.q5answer.grid(row = 37, column = 0, columnspan = 3, sticky = E)

        buffer = Label(self, text = "", font = ('MS',8))
        buffer.grid(row = 38, column = 0, sticky = W)
                       

    def submit_Button(self):
        #a button to allow the user to submit answers
        butSubmit = Button(self, text = 'Submit', font = ('MS', 8, 'bold'))
        butSubmit['command']=self.assess_Results
        butSubmit.grid(row = 99, column = 1, columnspan = 1, sticky = N)

    def clear_Button(self):
        #a button to clear the form
        butClear = Button(self, text = 'Clear All', font = ('MS',8, 'bold'))
        butClear['command']=self.clear_All
        butClear.grid(row = 99, column = 0, columnspan = 21, sticky = N)

    def view_Button(self):
        butView = Button(self, text = 'Show Data (Test)', font = ('MS', 8, 'bold'))
        butView['command']=self.print_data
        butView.grid(row = 99, column = 2, columnspan = 1, sticky = N)

    def clear_All(self):
        response = tk.askquestion("Programming Questions", "Are you sure you wish to clear all of your answers?")
        if response == 'yes':
            self.q1answer.delete(1.0,END)
            self.q2answer.delete(1.0,END)
            self.q3answer.delete(1.0,END)
            self.q4answer.delete(1.0,END)
            #self.q5answer.delete(1.0,END)
            tk.showinfo("Programming Questions", "All answers cleared.")
        else:
            return

    def assess_Results(self):
        countAll = 0

        if (self.q1answer.get().strip(" ") == "[0,12,24,36]") or (self.q1answer.get().strip(" ") == "0,12,24,36"):
            countAll += 1
        if self.q2answer.get().strip(" ") == "tower,glow" or self.q2answer.get().strip(" ") == "[(tower,glow)]":
            countAll += 1
        if self.q3answer.get().strip(" ") == "20":
            countAll += 1
        if self.q4answer.get() == "a is not None":
            countAll += 1

        if countAll == 0:
            tk.showinfo("Programming Questions", "You scored 0/4(0%).")
            self.python_Incompetent()
        if countAll == 1:
            tk.showinfo("Programming Questions", "You scored 1/4(25%).")
            self.python_Incompetent()
        if countAll == 2:
            tk.showinfo("Programming Questions", "You scored 2/4(50%).")
            self.python_Competent()
        if countAll == 3:
            tk.showinfo("Programming Questions", "You scored 3/4(75%).")
            self.python_Competent()
        if countAll == 4:
            tk.showinfo("Programming Questions", "You scored 4/4(100%).")
            self.python_Competent()

    def print_data(self):
        window = Tk()
        window.title("Results Viewer")
        app = results_viewer(window)
        window.mainloop()
        with open ("stu_dict.pkl", "rwb") as db:
            stu_dict = pickle.load(db)
            for line in db:
                print (line)
                
    def python_Competent(self):
        with open ("stu_dict.pkl", "rb") as db:
            stu_dict = pickle.load(db)
        stu_dict[self.student_No].changeCompetency(True)
        with open("stu_dict.pkl", "wb") as db:
            pickle.dump(stu_dict, db)
        self.master.destroy()
##        print (self.student_No)
##        with open ("stu_dict.pkl", "rb") as db:
##           stu_dict = pickle.load(db)
##        print (stu_dict[self.student_No])


    def python_Incompetent(self):
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
    root.title("Python Programming Questions")
    app = Python_Questions(root, number_arg)
    root.mainloop()



                    
                    
