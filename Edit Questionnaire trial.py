from tkinter import *
import tkinter.messagebox as box
class Edit_Questionnaire (Frame):
    window = Tk()

#The title of the program
    window.title('Edit Questionnaire')

#Welcome message or question on which question that the user wanted to edit    
    label = Label(window, text = 'Which question within the Questionnaire you wish to edit?')

#GUI for user to enter which question that they wanted to change
    frame=Frame(window)
    entry=Entry(frame)
    def dialog():
        box.showinfo('Question chosen for editing', 'Question' +entry.get())
    btn= Button(frame,text='Enter',command=dialog)

    label.pack()
    btn.pack(side = RIGHT)
    entry.pack(side = LEFT)
    frame.pack()
    window.mainloop()
