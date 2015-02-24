#The GUI for calculating group sizes based on either the desired number of students per group or
#the overall number of groups

#//TODO: throw to group calculator using user inputs

from tkinter import *
import tkinter.messagebox

class createGroups(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)
        self.grid()
        self.header()
        self.createGroupSelect()
        self.createSizeSelect()
        self.calculate()
        self.clear()
        self.back()

    def header(self):

        lblHeader = Label(self, text = "Select Parameters: ", font = ('MS', 10, 'bold'))
        lblHeader.grid(row = 0, column = 0, columnspan = 2, sticky = NW)

        lblHeader2 = Label(self, text = "Please select the desired number of students in a group OR " +
                                           "the maximum number of groups.", font = ('MS', 8, 'italic'))
        lblHeader2.grid(row = 2, column = 0, columnspan = 4, sticky = W)

    def createGroupSelect(self):
        #select number of groups from a dropdown list
        lblGroup = Label (self, text = "Select Number of Groups: ", font = ('MS', 8))
        lblGroup.grid(row = 5, column = 0, columnspan= 1, sticky= W)

        self.listGroup = Listbox (self, height = 3)
        scroll = Scrollbar(self, command = self.listGroup.yview)
        self.listGroup.configure(yscrollcommand=scroll.set)

        self.listGroup.grid(row = 5, column = 1, columnspan = 1, sticky = W)
        scroll.grid(row = 5, column = 1, sticky = NE)

        for item in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            self.listGroup.insert(END, item)

        self.listGroup.selection_set(END)

    def createSizeSelect(self):
        #select number of students per group from a dropdown
        lblSize = Label (self, text = "Select Students per Group: ", font = ('MS', 8))
        lblSize.grid(row = 5, column = 3, columnspan= 1, sticky= W)

        self.listSize = Listbox (self, height = 3)
        scroll = Scrollbar(self, command = self.listSize.yview)
        self.listSize.configure(yscrollcommand=scroll.set)

        self.listSize.grid(row = 5, column = 4, columnspan = 1, sticky = W)
        scroll.grid(row = 5, column = 4, sticky = NE)

        lblBlank = Label (self, text = "", font = ('MS', 8))
        lblBlank.grid(row = 3, column =0, columnspan = 4, sticky = W)

        lblBlank2 = Label (self, text = "", font = ('MS', 8))
        lblBlank2.grid(row = 6, column =0, columnspan = 4, sticky = W)

        for item in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            self.listSize.insert(END, item)

        self.listSize.selection_set(END)

    def calculate(self):
        #a button to allow the user to create groups with the selected parameters
        butSubmit = Button(self, text = 'Calculate Groups', font = ('MS', 8, 'bold'))
        butSubmit['command']=self.calculateGroups
        butSubmit.grid(row = 8, column = 1, columnspan = 2, sticky = N)

    def clear(self):
        #a button to clear selections
        butClear = Button(self, text = "Clear", font = ('MS', 8, 'bold'))
        butClear['command'] = self.clearSelection
        butClear.grid(row = 8, column = 0, columnspan = 1, sticky = N)

    def back(self):
        #a button to go back to the last screen
        butBack = Button(self, text = "Back", font = ('MS', 8, 'bold'))
        butBack['command'] = self.goBack
        butBack.grid(row = 8, column = 3, columnspan = 1, sticky = N)

    def clearSelection(self):
        self.listGroup.selection_clear(0,END)
        self.listSize.selection_clear(0,END)
        self.listGroup.selection_set(END)
        self.listSize.selection_set(END)

    def calculateGroups(self):
        #eventually this will throw to the method for caluclating the groups but for now it
        #simply pops a dialog window
        tkinter.messagebox.showinfo("Group Calculator", "Calculating... ")
        self.clearSelection()
        #//TODO: throw to group calculator

    def goBack(self):
        tkinter.messagebox.askquestion("Group Calculator", "Are you sure you wish to return to the previous " +
                                       "screen? All changes will be lost.")
        #//TODO: connect back to the previous screen

#Main
root = Tk()
root.title("Group Calculator")
app = createGroups(root)
root.mainloop()
