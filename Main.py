from tkinter import *
import lecturer_credentials
import Main_Menu
import os.path

root = Tk()

def check_exit():
        if messagebox.askokcancel("Exit", "Are you sure you want to quit?"):
                root.destroy()

root.protocol('WM_DELETE_WINDOW', check_exit)

if not os.path.isfile("credentials.pkl"):
	first_time_window = lecturer_credentials.Lecturer_Credentials(root)
else:
	main = Main_Menu.Main_Menu(root)
	

