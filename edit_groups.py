from tkinter import *
import pickle
import os.path
import re
import students
import groups
import auto_test

''' This is an interface for directly manipulating the groups. '''        
        

class Group_Editor():

    def __init__(self, group_size):

        # The group editor must be initialised with the desired group size as decided by the lecturer
        
        self.group_size = group_size # Will check that groups match the correct size at the end
        self.window = Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.handler)
        self.window.title("Group Editor")
        self.header()
        self.group_dict = self.open_groups()
        self.group_selector()
        self.has_changed = False # Tracks whether user has unsaved changes

    def handler(self):

        ''' An exit event handler. '''

        # Always displays
        quit_msg = "Are you sure you want to quit?"
        
        # Displays if there are unsaved changes
        if self.has_changed:
            quit_msg += "\n\nYou have unsaved changes."
            
        # Checks that the groups are the correct size
        size_ok = True
        for item in self.group_dict:
            if self.group_dict[item].get_group_size() != self.group_size:
                size_ok = False
                break

        if not size_ok:
            quit_msg += "\n\nOne or more of your groups has changed size."

        # Quit
        if messagebox.askokcancel("Quit?", quit_msg):
            self.window.destroy()

    def header(self):
				
	# This code is supposed to create a centred Header frame.
                
##        header_frame = Frame(self.window)
        header = Label(self.window, text = "Group Editor", font = ('MS', 20, 'bold'), anchor = CENTER)
##        header_frame.grid(row = 0, column = 0, columnspan = 3, sticky = "NSWE")
        header.grid(row = 0, column = 0, columnspan = 3, sticky = "NSWE")

    def open_groups(self):

        ''' Extracts groups from the hard drive. '''

        try:
            fileObject = open("group_dict.pkl", "rb")
            unpickled = pickle.load(fileObject)
            fileObject.close()
            return unpickled

        # I created a whole Error Window class for this event... probably overkill
        except IOError:
            err = Error_Window(self)

    def group_selector(self):

        # Create a list containing group names

        list_of_group_names = ["Group {}".format(i) for i in self.group_dict]

        # Assign StringVars for the OptionMenus
        
        self.op1 = StringVar(self.window)
        self.op1.set(list_of_group_names[0])
        self.op2 = StringVar(self.window)
        self.op2.set(list_of_group_names[1])

        option1 = OptionMenu(self.window, self.op1, *list_of_group_names, command = self.listbox_1)
        option2 = OptionMenu(self.window, self.op2, *list_of_group_names, command = self.listbox_2)

        option1.grid(row = 1, column = 0)
        option2.grid(row = 1, column = 2)

        # Initialise the listboxes

        self.gen_left_listbox(int(re.search('[0-9]+', self.op1.get()).group()))
        self.gen_right_listbox(int(re.search('[0-9]+', self.op2.get()).group()))

        # Create movement buttons

        move_right_btn = Button(self.window, text = "Move >>", command = self.move_right)
        move_right_btn.grid(row = 2, column = 1)

        move_left_btn = Button(self.window, text = "<< Move", command = self.move_left)
        move_left_btn.grid(row = 3, column = 1)

        # Create a save button

        save_btn = Button(self.window, text = "Save Groups", command = self.save_groups_confirm)
        save_btn.grid(row = 4, column = 1)
        
    def save_groups_confirm(self):

        ''' Save group dialog. '''

        confirm = Tk()
        confirm.title("Are you sure?")
        confirm_text = Label(confirm, text = "Are you sure you want to save the current groups? This will overwrite existing groups.")
        confirm_text.grid(columnspan = 2)

        no_btn = Button(confirm, text = "No", command = lambda: self.close(confirm))
        no_btn.grid(row = 1, column = 1)

        yes_btn = Button(confirm, text = "Yes", command = lambda: self.save(confirm))
        yes_btn.grid(row = 1, column = 0)

    def save(self, window):

        ''' The code for saving groups to disk and closing the save group dialog. '''
        
        with open("group_dict.pkl", "wb") as pickle_file:
            pickle.dump(self.group_dict, pickle_file)
            self.has_changed = False

        self.close(window)
        success = Tk()
        success_text = Label(success, text = "Success!")
        success_text.grid()

        success_btn = Button(success, text = "OK", command = lambda: self.close(success))
        success_btn.grid(row = 1)

    def close(self, window):
        window.destroy()

    def move_right(self):

        ''' Moves students between groups and updates the listbox. '''

        if self.left_listbox.curselection():
            
            '''
            This is kind of gross but it works.
            It extracts the group_dict key from the selected listbox item
            using regex.
            '''
            left_group_no = int(re.search('[0-9]+', self.op1.get()).group())
            right_group_no = int(re.search('[0-9]+', self.op2.get()).group())

            selected_student = self.group_dict[left_group_no].contents[int(self.left_listbox.curselection()[0])]
            new_group = self.group_dict[right_group_no]
            old_group = self.group_dict[left_group_no]

            new_group.add_student(selected_student)
            old_group.remove_student(selected_student)

            self.gen_left_listbox(int(re.search('[0-9]+', self.op1.get()).group()))
            self.gen_right_listbox(int(re.search('[0-9]+', self.op2.get()).group()))

            self.has_changed = True

        return           


    def move_left(self):

        ''' Moves students between groups and updates the listbox. '''
        
        if self.right_listbox.curselection():
            left_group_no = int(re.search('[0-9]+', self.op1.get()).group())
            right_group_no = int(re.search('[0-9]+', self.op2.get()).group())

            selected_student = self.group_dict[right_group_no].contents[int(self.right_listbox.curselection()[0])]
            new_group = self.group_dict[left_group_no]
            old_group = self.group_dict[right_group_no]

            new_group.add_student(selected_student)
            old_group.remove_student(selected_student)

            self.gen_left_listbox(int(re.search('[0-9]+', self.op1.get()).group()))
            self.gen_right_listbox(int(re.search('[0-9]+', self.op2.get()).group()))

            self.has_changed = True

        return
        

    def listbox_1(self, arg):

        ''' Figures out what the initial state of the LEFT listbox ought to be. '''
        
        grp_as_int = int(re.search('[0-9]+', arg).group())
        self.gen_left_listbox(grp_as_int)

    def listbox_2(self, arg):

        ''' Figures out what the initial state of the RIGHT listbox ought to be. '''
        
        grp_as_int = int(re.search('[0-9]+', arg).group())
        self.gen_right_listbox(grp_as_int)

    def gen_left_listbox(self, grp_no):

        '''
        Generates the left listbox.
        Happens every time the user makes a change to group_dict.    
        '''

        list_frame = Frame(self.window)
        list_frame.grid(row = 2, column = 0, rowspan = 2)

        self.left_listbox = Listbox(list_frame)
        for student in self.group_dict[grp_no].contents:
            self.left_listbox.insert(END, student.firstname + ' ' + student.surname)

        self.left_listbox.grid()

        scrollbar = Scrollbar(list_frame)
        scrollbar.grid(row = 0, column = 1, sticky = "NSWE")
        yscrollcommand = scrollbar.set

        self.left_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.left_listbox.yview)

    def gen_right_listbox(self, grp_no):

        '''
        Generates the right listbox.
        Happens every time the user makes a change to group_dict.    
        '''

        list_frame = Frame(self.window)
        list_frame.grid(row = 2, column = 2, rowspan = 2)

        self.right_listbox = Listbox(list_frame)
        for student in self.group_dict[grp_no].contents:
            self.right_listbox.insert(END, student.firstname + ' ' + student.surname)

        self.right_listbox.grid()

        scrollbar = Scrollbar(list_frame)
        scrollbar.grid(row = 0, column = 1, sticky = "NSWE")
        yscrollcommand = scrollbar.set

        self.right_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.right_listbox.yview)

        

class Error_Window():

    def __init__(self, master):

        self.master = master
        self.window = Tk()
        self.window.title("File not found")

        err_msg = Label(self.window, text = "Unable to find saved groups. Click \"OK\" to return to the main menu.")
        err_msg.grid()

        err_btn = Button(self.window, text = "OK", command = self.shut_it_down)
        err_btn.grid(row=1)

        self.master.window.destroy()

    def shut_it_down(self):
        self.window.destroy()
        

if __name__ == "__main__":

    # Create auto generated test groups if no groups are saved
    
    if not os.path.isfile("group_dict.pkl"):
        test_groups = auto_test.list_of_groups(8)
        groups_dict = {}

        for item in test_groups:
            groups_dict[item.number] = item

        with open("group_dict.pkl", "wb") as pickle_file:
            pickle.dump(groups_dict, pickle_file)

    # Open saved groups
    
    with open("group_dict.pkl", "rb") as pickle_file:
            loaded_groups = pickle.load(pickle_file)
            print(loaded_groups)

    Group_Editor(loaded_groups[1].get_group_size())
