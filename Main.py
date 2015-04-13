from tkinter import *
import lecturer_credentials
import Main_Menu
import os.path

root = Tk()
root.title("Welcome")
if not os.path.isfile("credentials.pkl"):
	first_time_window = lecturer_credentials.Lecturer_Credentials(root)
else:
	main = Main_Menu.Main_Menu(root)
	

