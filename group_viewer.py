from tkinter import *
import students
import groups

class group_viewer(Frame):

        def __init__(self, master, group_list):

                Frame.__init__(self, master)
                self.master = master
                self.grid()
                
                self.position = 0
                
                for group in group_list:
                        self.display_group(group)
                        self.position += 2

                self.position -= 2
                self.header()

        def header(self):

                header_frame = Frame(self.master)
                header = Label(self, text = "Group Viewer", font = ('MS', 20, 'bold'), justify = "center")
                header_frame.grid(sticky = "NSWE")
                header.grid(sticky = "NSWE")

        def display_group(self, group):

                list_frame = Frame(self.master)
                list_frame.grid(row = 1,column = self.position)

                scrollbar = Scrollbar(list_frame) 
                scrollbar.grid(row = 0, column = 1, sticky="NSWE")

                yscrollcommand=scrollbar.set
                
                listbox = Listbox(list_frame)
                for student in group.contents:
                        listbox.insert(END, student.firstname + ' ' + student.surname)

                listbox.grid(row = 0, column = 0)
                listbox.config(yscrollcommand=scrollbar.set)
                scrollbar.config(command=listbox.yview)

        


if __name__ == "__main__":
        root = Tk()
        root.title("Group Viewer")

        student_list = [students.Student("Liam", "Hamill", 1, "email")] * 50
        
        test_group = groups.Group(1)
        for item in student_list:
                test_group.add_student(item)

        window = group_viewer(root, [test_group]*5)


        window.mainloop()
