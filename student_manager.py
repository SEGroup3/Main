from tkinter import *
import students
import pickle
import Lecturer_Menu
import auto_test

class Student_Manager(Frame):

    def __init__(self, master):

        super(Student_Manager, self).__init__(master)
        self.master = master

        self.grid()
        self.header()

        with open("stu_dict.pkl", "rb") as db:
            self.stu_dict = pickle.load(db)

        self.stu_list = []

        for item in self.stu_dict.keys():
            self.stu_list.append(self.stu_dict[item])

        self.create_listbox()
        self.create_buttons()
            

    def header(self):
				
	# This code is supposed to create a centred Header frame.
        self.grid(pady = 80, padx = 80)        
        header = Label(self, text = "Student Management\n ______________", font = ('MS', 10, 'bold'), anchor = CENTER)
        header.grid(row = 0, column = 0, columnspan =3, sticky = "NSWE", pady= 10)

    def create_listbox(self):
        self.listbox_frame = Frame(self)
        self.stu_listbox = Listbox(self.listbox_frame)

        for item in self.stu_list:
            self.stu_listbox.insert(END, item.firstname + ' ' + item.surname)

        self.stu_listbox.grid(row = 0, column = 0)
        scrollbar = Scrollbar(self.listbox_frame) 
        scrollbar.grid(row = 0, column = 1, sticky = "NSWE")

        yscrollcommand=scrollbar.set
        self.stu_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.stu_listbox.yview)

        self.listbox_frame.grid(row = 1, column = 0)

    def create_buttons(self):

        btn_frame = Frame(self)
        btn_frame.grid(row = 1, column = 2)

        grade_label = Label(btn_frame, text = "Enter student grade:", anchor = W)
        grade_label.grid(row = 0, column = 2, pady=7, padx=5)

        self.grade_entry = Entry(btn_frame, width=4)
        self.grade_entry.grid(row = 0, column = 3, sticky='W')

        grade_btn = Button(btn_frame, text = "Add or overwrite grades", command = self.new_grade)
        grade_btn.grid(row = 1, column = 2, pady = 7, padx=10)

        del_btn = Button(btn_frame, text = "Delete student", command = self.del_stu)
        del_btn.grid(row = 2, column = 2, pady = 7, padx=10)

        save_btn = Button(btn_frame, text = "Save changes & exit", command = self.save_exit)
        save_btn.grid(row = 3, column = 2, pady = 7, padx=10)

        back_btn = Button(btn_frame, text = "Exit without saving", command = self.go_back)
        back_btn.grid(row = 4, column = 2, pady = 7, padx=10)
        
    def del_stu(self):
        
        student_to_delete = self.stu_list.pop(self.stu_listbox.curselection()[0])

        self.stu_dict = {stu_number: student_inst for stu_number, student_inst in self.stu_dict.items() if student_inst != student_to_delete}
        
        self.create_listbox()
        

    def new_grade(self):

        try:
            grade = int(self.grade_entry.get())
            if grade < 0 or grade > 100:
                messagebox.showerror("Invalid", "Please input a number between 0 and 100.")
                return
            try:
                student_to_amend = self.stu_list[self.stu_listbox.curselection()[0]]
                student_to_amend.addGrade(grade)

                self.stu_dict[student_to_amend.number] = student_to_amend
                messagebox.showinfo("Success", "Grades updated.")

                return
            
            except IndexError:
                messagebox.showerror("Invalid", "Please select a student.")
                return

        except ValueError:
            messagebox.showerror("Invalid", "Please input a number between 0 and 100.")
            return
        

    def save_exit(self):

        ''' Save group dialog. '''
        if messagebox.askokcancel("Are you sure?", "Are you sure you want to save changes? This will overwrite existing student data."):
            self.save()

    def go_back(self):

        if messagebox.askokcancel("Quit?", "Are you sure you want to quit? Unsaved changes will be lost."):
            self.grid_forget()
            self.destroy()
            Lecturer_Menu.Lecturer_Menu(self.master)

    def save(self):
        
        # Save stu_dict
        with open("stu_dict.pkl", "wb") as pickle_file:
            pickle.dump(self.stu_dict, pickle_file)

        # Update & save group_dict
        with open("group_dict.pkl", "rb") as pickle_file:
            grp_dict = pickle.load(pickle_file)

        for item in self.stu_list:
            found = False
            for grp in grp_dict.keys():
                for stu in grp_dict[grp].contents:
                    if stu.number == item.number:
                        stu = item
                        found = true
                        break
                if found:
                    break
        
        with open("group_dict.pkl", "wb") as pickle_file:
            pickle.dump(grp_dict, pickle_file)   

        messagebox.showinfo("Success", "Changes have been saved to disk.")

        self.grid_forget()
        self.destroy()
        Lecturer_Menu.Lecturer_Menu(self.master)
        
        

if __name__ == "__main__":

    students_to_save = auto_test.list_of_students(15)
    stu_dict = {}
    for item in students_to_save:
        stu_dict[item.number] = item

    with open("stu_dict.pkl", "wb") as db:
        pickle.dump(stu_dict, db)
    
    root = Tk()
    root.title("Student Management")
    Student_Manager(root)
