from tkinter import *
import students
import groups

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


class group_viewer(Frame):

        def __init__(self, master, group_list):

                Frame.__init__(self, master)
                self.master = master
                self.grid()
                
				# Create a frame to store group listboxes
                self.group_frame = Frame(self.master)
                self.group_frame.grid(row = 1, column = 0)
                
				# Saves position inside group_frame
                self.position = 0
                
                for group in group_list:
                        self.display_group(group)
                        self.position += 1

                self.header()

        def header(self):
				
				# This code is supposed to create a centred Header frame.
                
                header_frame = Frame(self.master)
                header = Label(header_frame, text = "Group Viewer", font = ('MS', 20, 'bold'), justify = "right")
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
              
                    

if __name__ == "__main__":
        root = Tk()
        root.title("Group Viewer")

        student_list = [students.Student("Liam", "Hamill", 1, "email", grades = 75, role = "Plant")] * 50
        
        test_group = groups.Group(1)
        for item in student_list:
                test_group.add_student(item)

        window = group_viewer(root, [test_group]*5)


        window.mainloop()
