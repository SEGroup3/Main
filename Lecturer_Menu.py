from tkinter import *
import tkinter.messagebox
from students import *
import group_viewer
import edit_groups
import createGroupsGUI
import student_manager
import os.path
import pickle

class Lecturer_Menu (Frame):

        def __init__(self, master):

            super(Lecturer_Menu, self).__init__(master)

            self.master = master
            self.grid()

            self.view_groups()

        def view_groups (self):
          
            self.grid(pady = 150, padx = 120)
            self.setup_group = Label (self, text = 'Set up Groups', font = ('MS',12, 'bold'))
            self.setup_group.grid (row =1, column =2, pady= 10)
            self.setup_button = Button (self, text = 'Set Group Size', command = self.launch_group_setup)
            self.setup_button.grid (row =2, column = 2, pady=10)
            self.stu_manager = Button (self, text = 'Student Management', command = self.launch_group_manager)
            self.stu_manager.grid (row = 3, column = 2, pady =10)

            if os.path.isfile("group_dict.pkl"):
                self.group_info = Label (self, text = 'Group Information', font = ('MS',12, 'bold'))
                self.group_info.grid (row =4, column =2, pady= 10)
                self.info_button = Button (self, text = 'View Groups', command = self.launch_group_info)
                self.info_button.grid (row = 5, column = 2, pady= 10)
                self.change_groups = Button (self, text = 'Change Groups', command = self.launch_change_group)
                self.change_groups.grid (row = 6, column = 2, pady= 10)
                
            else:
                self.group_info = Label (self, text = '______________\n\nNo group options available yet, \nPlease set up groups first')
                self.group_info.grid (row =3, column =2, pady= 10)


        def launch_group_info (self):
                

                try:

                    with open("group_dict.pkl", "rb") as db:
                            group_dict = pickle.load(db)

                    group_list = []
                    for item in group_dict.keys():
                            group_list.append(group_dict[item])

                    self.grid_forget()
                    self.destroy()        
                    group_viewer.Group_Viewer(self.master, group_list)


                except:
                    messagebox.showerror("Error", "Could not open the groups, or they were not saved to disk.")


        def launch_change_group (self):

            try:
                    with open("group_dict.pkl", "rb") as db:
                            biggest = 0
                            group_dict = pickle.load(db)
                            for item in group_dict.keys():
                                    if group_dict[item].get_group_size() > biggest:
                                            biggest = group_dict[item].get_group_size()

                    self.grid_forget()
                    self.destroy()
                    edit_groups.Group_Editor(master = self.master, group_size = biggest)

            except:
                    messagebox.showerror("Error", "Could not open the groups, or they were not saved to disk.")

        def launch_group_setup (self):
            if not os.path.isfile("stu_dict.pkl"):
                tkinter.messagebox.showinfo("No Students Added Yet")
                return
            else:
                self.grid_forget()
                self.destroy()
                createGroupsGUI.createGroups(self.master)

        def launch_group_manager (self):
                self.grid_forget()
                self.destroy()
                student_manager.Student_Manager(self.master)
                


if __name__ == '__main__':
    root = Tk()
    root.title("Lecturer Menu")
    app = Lecturer_Menu(root)
    root.mainloop()
