from tkinter import *
import students
import groups
from export_csv import convert_to_CSV
from auto_test import *

class More_Information():
		
        def __init__(self, group):

							       
                self.group = group
                self.window = Tk()
                self.window.title("More Information: Group {}".format(group.number))
				
                window_frame = Frame(self.window)
                window_frame.grid()
                self.display_group_details(window_frame)

        def combo_scroll(self, *args):
                self.names.yview(*args)
                self.belbin.yview(*args)
                self.grades.yview(*args)

        def mouse_wheel(self, event):
                self.names.yview("scroll", event.delta,"units")
                self.belbin.yview("scroll", event.delta,"units")
                self.grades.yview("scroll", event.delta,"units")
                
        def display_group_details(self, window_frame):

                display_frame = Frame(window_frame)
                display_frame.grid()
                self.names = Listbox(display_frame)
                self.belbin = Listbox(display_frame)
                self.grades = Listbox(display_frame)

                for student in self.group.contents:
                	
                    self.names.insert(END, student.firstname + ' ' + student.surname)
                    if student.role:
                        self.belbin.insert(END, student.role)
                    else:
                        self.belbin.insert(END, ' ')

                    if student.grades:
                        self.grades.insert(END, student.grades)
                    else:
                        self.grades.insert(END, ' ')

                name_label = Label(display_frame, text = "Name")
                belbin_label = Label(display_frame, text = "Belbin Role")
                grades_label = Label(display_frame, text = "Grades")

                name_label.grid(row = 0, column = 0)
                belbin_label.grid(row = 0, column = 1)
                grades_label.grid(row = 0, column = 2)

                self.names.grid(row = 1, column = 0)
                self.belbin.grid(row = 1, column = 1)
                self.grades.grid(row = 1, column = 2)

                scrollbar = Scrollbar(display_frame, command = self.combo_scroll) 
                scrollbar.grid(row = 1, column = 3, sticky = "NSWE")

                self.names.config(yscrollcommand=scrollbar.set)
                self.belbin.config(yscrollcommand=scrollbar.set)
                self.grades.config(yscrollcommand=scrollbar.set)

                self.names.bind("<MouseWheel>", self.mouse_wheel)
                self.belbin.bind("<MouseWheel>", self.mouse_wheel)
                self.grades.bind("<MouseWheel>", self.mouse_wheel)


class Group_Viewer(Frame):

        def __init__(self, master, group_list):

                Frame.__init__(self, master)
                self.master = master
                self.group_list = group_list
                self.grid()
                
		# Create a frame to store group listboxes
                self.group_frame = Frame(self.master)
                self.group_frame.grid(row = 1, column = 0)
                
		# Saves position inside group_frame
                self.position = 0
                
                for group in group_list:
                        self.display_group(group)
                        self.position += 1

                self.save_button()
                
                self.header()

        def save_button(self):

                save_button = Button(self.master, text = "Save Groups", command = self.save_groups)
                save_button.grid(row = 2, column = 0, sticky = "W")
                

        def header(self):
				
		# This code is supposed to create a centred Header frame.
                
                header_frame = Frame(self.master)
                header = Label(header_frame, text = "Group Viewer", font = ('MS', 20, 'bold'), justify = "right", anchor = CENTER)
                header_frame.grid(row = 0, column = 0, sticky = "NSWE")
                header.grid(sticky = "NSWE")

        def create_more_info(self, group):
                
                info_window = More_Information(group)

        def display_group(self, group):

		# Positions a listbox, scrollbar, and more info button for a group

                list_frame = Frame(self.group_frame)
                list_frame.grid(row = 1,column = self.position, padx = 3)

                scrollbar = Scrollbar(list_frame) 
                scrollbar.grid(row = 0, column = 1, sticky="NSWE")

                yscrollcommand=scrollbar.set
                
                listbox = Listbox(list_frame)
                for student in group.contents:
                        listbox.insert(END, student.firstname + ' ' + student.surname)

                listbox.grid(row = 0, column = 0)
                listbox.config(yscrollcommand=scrollbar.set)
                scrollbar.config(command=listbox.yview)

                more_info = Button(list_frame, text = "More Info >>", command = lambda: self.create_more_info(group))
                more_info.grid(row=2, column = 0)

        def save_groups(self):

                try:
                        filename = filedialog.asksaveasfile(defaultextension = ".csv", filetypes = [("CSV", ".csv")])
                
                        output = convert_to_CSV(self.group_list)
                        with filename as csvfile:
                                csvfile.write(output)

                except AttributeError:

                        #If no file name is provided, return
                        
                        return

                confirm_window = Tk()
                confirm_window.title("Success!")

                confirmation_frame = Frame(confirm_window)
                confirmation_frame.grid()

                success = Label(confirmation_frame, text = "Groups saved.", anchor = CENTER)
                success.grid(row = 0, column = 0)

                ok_confirm = Button(confirmation_frame, text = "OK", command = confirm_window.destroy, anchor = CENTER)
                ok_confirm.grid(row = 1, column = 0)

                confirm_window.mainloop()
              
                    

if __name__ == "__main__":
        root = Tk()
        root.title("Group Viewer")
        
        test_groups = list_of_groups(5)
        window = Group_Viewer(root, test_groups)

        window.mainloop()
