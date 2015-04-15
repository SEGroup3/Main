from tkinter import *
import students
import pickle

class Student_Manager(Frame):

    def __init__(self, master):

        super(Student_Manager, self).__init__(master)
        self.master = master

        self.grid()

        with open("stu_dict.pkl", "rb") as db:
            stu_dict = pickle.load(db)

        

if __name__ == "__main__":
    root = Tk()
    Student_Manager(root)
