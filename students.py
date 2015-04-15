class Student ():

    def __init__(self, firstname, surname, number, email, grades = None, role = None, competency = False):
        # Students must have a name, number, and email.
        # Optionally, you can also define grades and role at this point.

        self.firstname = firstname
        self.surname = surname
        self.number = number
        self.email = email
        self.grades = grades
        self.role = role
        self.competency = competency


    def __str__(self):
        # Returns a one-line string containing a Student's attributes.
        # May be useful for debugging.

        output = "(Firstname: {}, Surname: {}, Number: {}, Email: {}, Competency: {}".format(self.firstname, self.surname, self.number, self.email, self.competency)
        
        if self.grades:
            output += ", Grades: {}".format(self.grades)
        if self.role:
            output += ", Role: {}".format(self.role)
        output += ")"
        
        return output

    def addRole (self, role):
        self.role = role

    def addGrade (self, grade):
        self.grades = grade      

    def changeCompetency (self, competency):
        self.competency = competency

    def getStudentInfo (self):
        # Prints student attributes to the console over several lines.
        # This will have to be rewritten for the GUI.

        print("Name:", self.firstname, self.surname)
        print("Student Number:", self.number)
        print("Email:", self.email)
        print("Competency:", self.competency)

        if self.grades:
            print("Grades:", self.grades)
        if self.role:   
            print("Team Role:", self.role)
        
        print()

if __name__ == "__main__":

    # Test/Debug code
    # Delete before submission

    aStudent = Student("Liam", "Hammill", 1, "email", competency = True)
    aStudent2 = Student("Test","Tester",  2, "email", 70, "role")

    aStudent.getStudentInfo()
    aStudent2.getStudentInfo()
    print(aStudent)
    print(aStudent2)
