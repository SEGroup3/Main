#The GUI for calculating group sizes based on either the desired number of students per group or
#the overall number of groups

#//TODO: throw to group calculator using user inputs

from tkinter import *
import tkinter
import tkinter.messagebox as tk
import os, sys
import pickle
import sort_alg
import group_viewer
import Lecturer_Menu

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

        lblHeader2 = Label(self, text = "Please select the desired number of students in a group AND " +
                                           "the number of groups.", font = ('MS', 8, 'italic'))
        lblHeader2.grid(row = 2, column = 0, columnspan = 4, sticky = W)

        lblBuffer = Label(self, text = "", font = ('MS', 8))
        lblBuffer.grid(row = 98, column = 0)
        with open ("stu_dict.pkl", "rb") as db:
            stu_dict = pickle.load(db)
            no_students = len(stu_dict)
        
        lblFooter = Label(self, text = "There are currently " + str(no_students) + " unallocated students.",
                          font = ('MS', 8))
        lblFooter.grid(row = 99, column = 0, columnspan = 4, sticky = W)

    def createGroupSelect(self):
        #select number of groups from a dropdown list
        lblGroup = Label (self, text = "Select Number of Groups: ", font = ('MS', 8))
        lblGroup.grid(row = 5, column = 0, columnspan= 1, sticky= W)

        self.listGroup = Listbox (self,exportselection = 0, height = 3)
        scroll = Scrollbar(self,   command = self.listGroup.yview)
        self.listGroup.configure(yscrollcommand=scroll.set)

        self.listGroup.grid(row = 5, column = 1, columnspan = 1, sticky = W)
        scroll.grid(row = 5, column = 1, sticky = "NSE")

        for item in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            self.listGroup.insert(END, item)

        self.listGroup.selection_set(END)

    def createSizeSelect(self):
        #select number of students per group from a dropdown
        lblSize = Label (self, text = "Select Students per Group: ", font = ('MS', 8))
        lblSize.grid(row = 5, column = 3, columnspan= 1, sticky= W)

        self.listSize = Listbox (self,exportselection = 0, height = 3)
        scroll = Scrollbar(self,  command = self.listSize.yview)
        self.listSize.configure(yscrollcommand=scroll.set)

        self.listSize.grid(row = 5, column = 4, columnspan = 1, sticky = W)
        scroll.grid(row = 5, column = 4, sticky ="NSE")

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
        butSubmit['command']=self.calculate_groups
        butSubmit.grid(row = 8, column = 2, columnspan = 2, sticky = N)

    def clear(self):
        #a button to clear selections
        butClear = Button(self, text = "Clear", font = ('MS', 8, 'bold'))
        butClear['command'] = self.clearSelection
        butClear.grid(row = 8, column = 1, columnspan = 1, sticky = N)

    def back(self):
        #a button to go back to the last screen
        butBack = Button(self, text = "Back", font = ('MS', 8, 'bold'))
        butBack['command'] = self.goBack
        butBack.grid(row = 8, column = 4, columnspan = 1, sticky = N)

    def clearSelection(self):
        self.listGroup.selection_clear(0,END)
        self.listSize.selection_clear(0,END)
        self.listGroup.selection_set(END)
        self.listSize.selection_set(END)

    def goBack(self):
        response = tk.askquestion("Group Calculator", "Are you sure you wish to return to the previous " +
                                       "screen? All changes will be lost.")
        if response == 'yes':
            self.destroy()
            Lecturer_Menu.Lecturer_Menu(self.master)
        else:
            return
        

    def calculate_groups(self):

        desired_number = int(self.listGroup.curselection()[0]) + 1
        desired_size = int(self.listSize.curselection()[0]) + 1

        warning = "Do you want to create groups using these parameters?"

        with open ("stu_dict.pkl", "rb") as db:
            stu_dict = pickle.load(db)
            no_students = len(stu_dict)

        if desired_number * desired_size < no_students:
            warning += "\n\nWarning! Not enough space for all students"

        if desired_number * desired_size > no_students:
            warning += "\n\nWarning! Not enough students to fill all groups"

        if no_students % desired_size != 0:
            warning += "\n\nWarning! Groups will not be of equal size"

        create = tkinter.messagebox.askquestion("Create Groups", warning)

        if create == 'yes':
            student_groups = sort_alg.sort_students(stu_dict, desired_number, desired_size)
            grp_dict = {}
            for item in student_groups:
                grp_dict[item.number] = item

            with open ("group_dict.pkl", "wb") as db:
                pickle.dump(grp_dict, db)

            self.destroy()
            viewer_window = group_viewer.Group_Viewer(self.master, student_groups)

            
        else:
            return
        """tkinter.messagebox.showinfo("Group Calculator", "Calculating...")
        self.clearSelection()
        data = {}
        with open("stu_dict.pkl", "rb") as f:
            try:
                while True:
                    event = pickle.load(f)
                    data.append(line)
            except (EOFError):
                pass

        print (data)
            
        if self.listSize.get() is not None:
            print(self.listSize.get())
        elif self.listGroup.get() is not None:
            print(self.listGroup.get())
        else:
            tkinter.messagebox.showwarning("Group Calculator", "You must select from one of the options available")
            print ("Error")"""
#Main
if __name__ =='__main__':
    root = Tk()
    root.title("Group Calculator")
    app = createGroups(root)
    root.mainloop()
