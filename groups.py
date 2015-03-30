'''
This module defines behaviour of group objects. It differs from the class diagram in a
couple of ways. Firstly, add_student and remove_student methods have been added.
Secondly, group size is accessed as an attribute (self.size) and NOT through a method
(get_group_size()).
'''

import students
import auto_test

class Group():

        def __init__(self, number):
                self.number = number
                self.contents = []
                return

        def get_group_size(self):

                return len(self.contents)

        def add_student(self, student):
                
                self.contents.append(student)
                return

        def remove_student(self, student):

                if student in self.contents:
                        self.contents.remove(student)

                return

        def get_members(self):
                
                if len(self.contents) == 0:
                        print("Group {} has no members.".format(self.number))
                        return

                print("The members of Group {} are:".format(self.number))
                for item in self.contents:
                        print(item)
                return

        def get_group_results(self):
                
                total_grades = 0 # Total grades of group
                ignore = 0 # Number of students with no grade saved

                for item in self.contents:
                        if item.grades:
                                total_grades += item.grades
                        else:
                                ignore += 1

                if total_grades == 0:
                        print("No grade information for Group {}.".format(self.number))
                        return False

                students_with_grades = self.get_group_size() - ignore
                avg_grade = total_grades / students_with_grades

                print("Average grade for Group {} is {}.".format(self.number, avg_grade))
                return avg_grade

if __name__ == "__main__":
        
        # Test code

        test_group = auto_test.list_of_groups(1)[0]

        test_group.get_members()
        print("Group size is:")
        print(test_group.get_group_size())
        test_group.get_group_results()
        print()

        test_student = auto_test.list_of_students(1)[0]
        print("New student: ")
        print(test_student, end = "\n")
        test_group.add_student(test_student)
        test_group.get_members()
        print("Group size is:")
        print(test_group.get_group_size())
        test_group.get_group_results()
        print()
        
        test_group.remove_student(test_student)
        test_group.get_members()
        print("Group size is:")
        print(test_group.get_group_size())
        test_group.get_group_results()
        print()
