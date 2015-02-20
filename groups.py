'''
This module defines behaviour of group objects. It differs from the class diagram in a
couple of ways. Firstly, add_student and remove_student methods have been added.
Secondly, group size is accessed as an attribute (self.size) and NOT through a method
(getGroupSize()).
'''

import students

class Group():

	def __init__(self, number):
		self.number = number
		self.contents = []
		self.size = 0

	def add_student(self, student):
		self.contents.append(student)
		self.size += 1

	def remove_student(self, student):
		'''
		We might have to rewrite this to remove people based on their unique student number.
		e.g.:
		for item in self.contents:
			if item.number == target:
				self.contents.remove(item)
				return

		print("Student not found.")
		'''

		if student in self.contents:
			self.contents.remove(student)
			print("{} has been removed successfully.".format(student.name))
			self.size -= 1
		
		else:
			print("Student not found.")

	def get_members(self):
		if len(self.contents) == 0:
			print("Group {} has no members.".format(self.number))
			return

		print("The members of Group {} are:".format(self.number))
		for item in self.contents:
			print(item)

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
			return

		students_with_grades = self.size - ignore
		avg_grade = total_grades / students_with_grades

		print("Average grade for Group {} is {}.".format(self.number, avg_grade))

	def save_group(self):
		# To-do
		pass


if __name__ == "__main__":
	# Test code

	student1 = students.Student("Liam", 1, "email")
	student2 = students.Student("Sam", 2, "email", 75, "Co-ordinator")
	student3 = students.Student("Vera", 3, "email", 70, "Plant")
	student4 = students.Student("Callum", 4, "email", 72)
	student5 = students.Student("Andrew", 5, "email", 79)

	test_group = Group(1)
	test_group.add_student(student1)
	test_group.add_student(student2)
	test_group.add_student(student3)
	test_group.add_student(student4)
	test_group.add_student(student5)

	test_group2 = Group(2)

	test_group.get_members()
	print("Group size is:", test_group.size)
	test_group.get_group_results()
	test_group.remove_student(student1)
	test_group.get_members()
	print("Group size is:", test_group.size)
	print()

	test_group2.get_members()
	print("Group size is:", test_group2.size)
	test_group2.get_group_results()
	test_group2.remove_student(student1)
