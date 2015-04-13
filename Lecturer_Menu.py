from tkinter import *
import tkinter.messagebox
from students import *
import group_viewer
import edit_groups
import createGroupsGUI
import os.path

class Lecturer_Menu (Frame):

        def __init__(self, master):

            super(Lecturer_Menu, self).__init__(master)

            self.master = master
            self.grid()

            self.view_groups()

        def view_groups (self):

            self.pack(pady = 150, padx = 120)
            self.setup_group = Label (self, text = 'Set up Groups', font = ('MS',12, 'bold'))
            self.setup_group.grid (row =1, column =2, pady= 10)
            self.setup_button = Button (self, text = 'Set Group Size', command = self.launch_group_setup)
            self.setup_button.grid (row =2, column = 2)
            self.group_info = Label (self, text = 'Group Information', font = ('MS',12, 'bold'))
            self.group_info.grid (row =3, column =2, pady= 10)
            self.info_button = Button (self, text = 'View Groups', command = self.launch_group_info)
            self.info_button.grid (row = 4, column = 2)
            self.change_groups = Button (self, text = 'Change Groups', command = self.launch_change_group)
            self.change_groups.grid (row = 5, column = 2, pady =10)


        def launch_group_info (self):
            self.grid_forget()
            self.destroy()
            group_viewer.Group_Viewer(self.master)

        def launch_change_group (self):
            self.grid_forget()
            self.destroy()
            edit_groups.Group_Editor(self.master)

        def launch_group_setup (self):
            if not os.path.isfile(stu.dict.pkl):
                tkinter.messagebox.showinfo("No Students Added Yet")
                return
            else:
                self.grid_forget()
                self.destroy()
                createGroupsGUI.createGroups(self.master)


if __name__ == '__main__':
    root = Tk()
    root.title("Lecturer Menu")
    app = Lecturer_Menu(root)
    root.mainloop()
