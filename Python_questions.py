#the GUI to ask students programming questions, assess and save the results

from tkinter import *
import tkinter.messagebox as tk
import shelve
from Response import Response

class results_viewer(Frame):
    def __init__(self,master):        
        Frame.__init__(self,master)
        self.grid()
        self.header()
        self.exit_button()

    def header(self):
        self.pack(pady = 20, padx = 20)
        lblHeader = Label(self, text = "Table of Results", font=('MS', 10, 'bold'))
        lblHeader.grid(row =0, column = 0, columnspan = 2, sticky = NW)

    def close_window(self):
        self.root.destroy()
        
    def exit_button(self):
        #a button to quit the results viewer
        butSubmit = Button(self, text = 'Quit', font = ('MS', 8, 'bold'))
        butSubmit['command']=self.close_window
        butSubmit.grid(row = 99, column = 1, columnspan = 1, sticky = N)

 

class prog_questions (Frame):

    def __init__(self,master):

        Frame.__init__(self,master)
        self.grid()
        self.header()
        self.q_header()
        self.q1()
        self.q2()
        self.q3()
        self.q4()
        self.q5()
        self.submit_Button()
        self.clear_Button()
        self.view_Button()

    def header(self):
        
        self.pack(pady = 20, padx = 20)
        lblHeader = Label(self, text = "Programming Questions: ", font = ('MS', 10, 'bold'))
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

        self.q1answer = Text(self, height=3, width = 40)
        scroll = Scrollbar(self, command = self.q1answer.yview)
        self.q1answer.configure(yscrollcommand=scroll.set)

        self.q1answer.grid(row = 10, column = 0, columnspan = 3, sticky = E)
        scroll.grid(row =10, column = 3, sticky = W)

    def q2(self):

        q2header = Label(self,text = "Question 2:", font = ('MS',8, 'bold'))
        q2header.grid(row = 11, column = 0, sticky = W)
        q2body1 = Label(self,text = ">>> import re", font = ('MS', 8))
        q2body1.grid(row = 12, column = 0, sticky = W)
        q2body2 = Label(self,text = ">>> words = 'cat, cow, dog, dig, ding, song, sing, tower, grow, glow, lower'", font = ('MS', 8))
        q2body2.grid(row = 13, column = 0, sticky = W)
        q2body3 = Label(self, text = ">>> re.findall(r'(\w+), grow, (\w+)', words)", font = ('MS', 8))
        q2body3.grid(row = 14, column = 0, sticky = W)

        self.q2answer = Text(self, height=3, width = 40)
        scroll = Scrollbar(self, command = self.q2answer.yview)
        self.q2answer.configure(yscrollcommand=scroll.set)

        self.q2answer.grid(row = 15, column = 0, columnspan = 3, sticky = E)
        scroll.grid(row = 15, column = 3, sticky = W)

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


        self.q3answer = Text(self, height=3, width = 40)
        scroll = Scrollbar(self, command = self.q3answer.yview)
        self.q3answer.configure(yscrollcommand=scroll.set)

        self.q3answer.grid(row = 23, column = 0, columnspan = 3, sticky = E)
        scroll.grid(row = 23, column = 3, sticky = W)

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


        self.q4answer = Text(self, height=3, width = 40)
        scroll = Scrollbar(self, command = self.q4answer.yview)
        self.q4answer.configure(yscrollcommand=scroll.set)

        self.q4answer.grid(row = 30, column = 0, columnspan = 3, sticky = E)
        scroll.grid(row = 30, column = 3, sticky = W)

    def q5(self):

        q5header = Label(self,text = "Question 5:", font = ('MS',8, 'bold'))
        q5header.grid(row = 31, column = 0, sticky = W)
        q5body1 = Label(self,text = ">>>for i in range(10,25,5):", font = ('MS', 8))
        q5body1.grid(row = 32, column = 0, sticky = W)
        q5body2 = Label(self,text = "            print i, ': ',", font = ('MS', 8))
        q5body2.grid(row = 33, column = 0, sticky = W)
        q5body3 = Label(self, text = "           for j in range (i/5):", font = ('MS', 8))
        q5body3.grid(row = 34, column = 0, sticky = W)
        q5body4 = Label(self, text = "                   print i/5,", font = ('MS', 8))
        q5body4.grid(row = 35, column = 0, sticky = W)
        q5body5 = Label(self, text = "           print", font = ('MS', 8))
        q5body5.grid(row = 36, column = 0, sticky = W)


        self.q5answer = Text(self, height=3, width = 40)
        scroll = Scrollbar(self, command = self.q5answer.yview)
        self.q5answer.configure(yscrollcommand=scroll.set)

        self.q5answer.grid(row = 37, column = 0, columnspan = 3, sticky = E)
        scroll.grid(row = 37, column = 3, sticky = W)

        buffer = Label(self, text = "", font = ('MS',8))
        buffer.grid(row = 38, column = 0, sticky = W)
                       

    def submit_Button(self):
        #a button to allow the user to submit answers
        butSubmit = Button(self, text = 'Submit', font = ('MS', 8, 'bold'))
        butSubmit['command']=self.store_Response
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
            self.q5answer.delete(1.0,END)
            tk.showinfo("Programming Questions", "All answers cleared.")
        else:
            return
        
    def store_Response(self):
        #store the response using shelving
        
        db = shelve.open('responsedb')
        responseCount = len(db)
        Ans = Response(str(responseCount+1),self.q1answer.get(1.0, END),self.q2answer.get(1.0,END),
                           self.q3answer.get(1.0, END), self.q4answer.get(1.0,END),self.q5answer.get(1.0,END)
                           )
        db[Ans.respNo] = Ans
        butSubmit['command']=tk.showinfo("Programming Questions", "Your answers have been saved.")
        db.close
        #TODO//jump to next part of program here

    def print_data(self):
        pass
#        root = Tk()
#        root.title("Results Viewer")
#        app = prog_questions(root)
#        root.mainloop()
#        db = shelve.open('responsedb')
        #display the results
#        db.close

#Main
root = Tk()
root.title("Programming Questions")
app = prog_questions(root)
root.mainloop()



                    
                    
