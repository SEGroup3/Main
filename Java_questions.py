#the GUI to ask Java questions

from tkinter import *
import tkinter.messagebox as tk
import shelve

class java_responses:
    def __init__(self, respNo="", q1 = 0, q2 = 0, q3 = 0, q4 = 0, q5 = 0):
        self.respNo = respNo
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5

class java_questions(Frame):

    def __init__(self,master):

        Frame.__init__(self,master)
        self.grid()
        self.header()
        self.q_header()
        self.q1()
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
        line1 = Label(self, text = "Review the following Java code and answer the questions in the text boxes shown.",
                      font = ("MS", 8))
        line1.grid(row = 2, column = 0, sticky = W)
        line2 = Label(self, text = "When you are finished, click Submit and your answers will be saved.", font = ('MS', 8))
        line2.grid(row = 3, column = 0, sticky = W)
        line3 = Label(self, text= "", font = ('MS', 8))
        line3.grid(row = 4, column = 0, sticky = W)

    def submit_Button(self):
        #a button to allow the user to submit answers
        butSubmit = Button(self, text = 'Submit', font = ('MS', 8, 'bold'))
        butSubmit['command']=self.store_Response
        butSubmit.grid(row = 99, column = 1, columnspan = 1, sticky = N)
    
    def clear_Button(self):
        #a button to clear the form
        butClear = Button(self, text = 'Clear All', font = ('MS',8, 'bold'))
        butClear['command']=self.clear_All
        butClear.grid(row = 99, column = 0, columnspan = 2, sticky = N)

    def q1(self):
        line1 = Label(self, text = "Which statement is true for the class java.util.ArrayList?",
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


    def q2(self):
        pass

    def q3(self):
        pass

    def q4(self):
        pass

    def q5(self):
        pass

    def store_Response(self):
        #store the response using shelving
        #q2-5 commented out until they are implemented above
        db = shelve.open('javaresponsedb')
        responseCount = len(db)
        Ans = java_responses(str(responseCount+1),
                       self.varQ1.get(), #self.varQ2.get(), self.varQ3.get(), self.varQ4.get(),
                       #self.varQ5.get()
                       )
        db[Ans.respNo] = Ans
        db.close
        tk.showinfo("Programming Questions", "Your answers have been saved.")
        self.master.destroy()
        #TODO//jump to next part of program here
        
    def clear_All(self):
        response = tk.askquestion("Programming Questions", "Are you sure you wish to clear all of your answers?")
        if response == 'yes':
            self.varQ1.set(0)
            #self.varQ2.set(0)
            #self.varQ3.set(0)
            #self.varQ4.set(0)
            #self.varQ5.set(0)
            tk.showinfo("Programming Questions", "All answers cleared.")
        else:
            return

#Main
if __name__ == '__main__':
    root = Tk()
    root.title("Java Programming Questions")
    app = java_questions(root)
    root.mainloop()
