from tkinter import *
import lecturer
import pickle
import Main_Menu

class Lecturer_Credentials(Frame):

    ''' Creates a prompt for the user to supply a username and password. '''

    def __init__(self, master):

        super(Lecturer_Credentials, self).__init__(master)

        self.master = master
        self.grid()

        self.message = "Welcome to the Sorting Hat.\n\nYou need to create a username and password for the main lecturer."
        self.create_gui()
        
    def create_gui(self):

        intro = Label(self, text = self.message)
        intro.grid()

        entry = Frame(self)
        entry.grid()

        self.login_label = Label(entry, text = 'Username')
        self.login = Entry(entry, width = 30)

        self.login_label.grid(pady = 10, padx = 5)
        self.login.grid(row = 0, column = 1)

        self.password_label = Label(entry, text = 'Password')
        self.password = Entry(entry, width = 30, show = "*")


        self.password_label.grid(row = 1, column = 0, pady = 10, padx = 5)
        self.password.grid(row = 1, column = 1)

        submit = Button(self, text = "Submit", command = self.make_lecturer)
        submit.grid(row = 3, column = 0)

    def make_lecturer(self):

        if not self.login.get() or not self.password.get():

            # Prompt the user to enter a username + p/w and return
            
            new_window = Tk()
            new_window.title("Warning")
            warning = Label(new_window, text = "Please enter username and password.")
            warn_btn = Button(new_window, text = "OK", command = new_window.destroy)
            warning.grid()
            warn_btn.grid()

            return

        user = self.login.get()
        password = self.password.get()


        credentials = { user : password }

        with open("credentials.pkl", mode = "wb") as file:
            pickle.dump(credentials, file)

        # Debug code, delete before release
        with open("credentials.pkl", mode = "rb") as file:
            credentials = pickle.load(file)

        print(credentials)
        # Debug ends


        self.grid_forget()
        self.destroy()
        Main_Menu.Main_Menu(self.master)

if __name__ == "__main__":
    window = Tk()
    window.title("The Sorting Hat")
    Lecturer_Credentials(window)

