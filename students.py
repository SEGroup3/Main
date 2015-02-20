class Student ():

    def __init__(self, name, number, email, grades = None, role = None):
        # Students must have a name, number, and email.
        # Optionally, you can also define grades and role at this point.

        self.name = name
        self.number = number
        self.email = email
        self.grades = grades
        self.role = role

    def __str__(self):
        # Returns a one-line string containing a Student's attributes.
        # May be useful for debugging.

	    output = "(Name: {}, Number: {}, Email: {}".format(self.name, self.number, self.email)
	    
	    if self.grades:
	    	output += ", Grades: {}".format(self.grades)
	    if self.role:
	    	output += ", Role: {}".format(self.role)
	    output += ")"
	    
	    return output

    def addRole (self, role):
        self.role = role

    def addGrade (self, grade):
        self.grade = grade		

    def getStudentInfo (self):
        # Prints student attributes to the console over several lines.
        # This will have to be rewritten for the GUI.

        print("Name:", self.name)
        print("Student Number:", self.number)
        print("Email:", self.email)

        if self.grades:
        	print("Grades:", self.grades)
        if self.role:	
       		print("Team Role:", self.role)
       	
       	print()

if __name__ == "__main__":

    # Test/Debug code
    # Delete before submission

	aStudent = Student("Liam", 1, "email")
	aStudent2 = Student("Test", 2, "email", 70, "role")

	aStudent.getStudentInfo()
	aStudent2.getStudentInfo()
	print(aStudent)
	print(aStudent2)
