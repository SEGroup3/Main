import groups
import students

class Lecturer():

	def __init__(self, name, email, username, password):

		self.lecturer_name = name
		self.lecturer_email = email
		self.username = username
		self.password = password

		self.groups = []

	def add_group(self, group):

		self.groups.append(group)

	def remove_group(self, group):

		if group in self.groups:
			self.groups.remove(group)
			print("Group {} has been removed successfully.".format(group.number))

		else:
			print("Group not found.")

	def get_info(self):

		return self.lecturer_name, self.lecturer_email, self.username

	def get_groups(self):

		return self.groups

	def get_grades(self):

		grades = 0
		valid_groups = 0

		for group in self.groups:
			if group.get_group_results:
				grades += group.get_group_results()
				valid_groups += 1

		if grades == 0:
			print("No grade information.")

		else:
			avg_grade = grades / valid_groups
			print("The average grade of all students is: {}".format(avg_grade))

	def __str__(self):

		output = "Name: {}, Email: {}, Username: {}. Contains:".format(self.lecturer_name, self.lecturer_email, self.username)

		if len(self.groups) == 0:
			output += " no groups."
			return output

		for item in self.groups:
			output += " Group {},".format(item.number)

		output = output[:1] # removes the last comma

		return output



if __name__ == "__main__":

	test = Lecturer("Test", "Email", "Username", "Password")
	print(test)
	test.get_grades()

	student1 = students.Student("Liam", "H", 1, "email")
	student2 = students.Student("Sam", "R", 2, "email", 75, "Co-ordinator")
	student3 = students.Student("Vera", "Y", 3, "email", 70, "Plant")
	student4 = students.Student("Callum", "X",  4, "email", 72)
	student5 = students.Student("Andrew", "Z", 5, "email", 79)

	test_group = groups.Group(1)
	test_group.add_student(student1)
	test_group.add_student(student2)
	test_group.add_student(student3)
	test_group.add_student(student4)
	test_group.add_student(student5)

	test_group2 = groups.Group(2)

	test.add_group(test_group)
	test.add_group(test_group2)

	print(test)
	test.get_grades()

	test.remove_group(test_group)

	print(test)
	test.get_grades()




