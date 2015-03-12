from tkinter import *
import Questionnaire
import Python_questions

root = Tk()
root.title("Define Student")
intro = Questionnaire.Questionnaire(root)
intro.mainloop()

root = Tk()
root.title("Programming Questions")
questions = Python_questions.prog_questions(root)
questions.mainloop()

