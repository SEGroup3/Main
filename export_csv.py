'''
Contains code for exporting Group() objects from groups.py into CSV format.
In my code I am manually constructing a csv file as a string, but I think that's
probably an awful hack and the csv module would be a more elegant solution.
'''

import groups
import students

def convert_to_CSV(list_of_groups, more = False):
	
	'''
	Accepts a list of group objects and returns a csv compatible string.
	By default it only outputs group names, but by setting the 'more' flag to True,
	it will also display Belbin Role and grades for the student if they are available.
	'''

	output = ''
	largest_group_size = 0

	for item in list_of_groups:
		# Goes through each group object and creates headers for the csv file.
		# Also records the largest group size within the list of groups.

		if more:
			output += 'Group {}, Belbin Role, Grades, , '.format(item.number)
		else:
			output += 'Group {}, , '.format(item.number)
		
		if item.size > largest_group_size:
			largest_group_size = item.size

	# Now we construct the data-containing csv rows.
	row = 0

	while row <= largest_group_size - 1:
		# Adds each row of the csv file one at a time.

		output += '\n'
		for item in list_of_groups:
			try:
				output += '{}, '.format(item.contents[row].name)
				# Digs up the student.name attribute.

				if more:
					# Digs up the remaining attributes.

					if item.contents[row].role:
						output += '{}, '.format(item.contents[row].role)
					else:
						output += ', '
					if item.contents[row].grades:
						output += '{}, '.format(item.contents[row].grades)
					else:
						output += ', '

				output += ', '

			except IndexError:
				# If this group object contains no student for this row,
				# create a blank row.

				if more:
					output += ', , , , '
				else:
					output += ', , '
		row += 1

	return output

if __name__ == "__main__":

	student1 = students.Student("Liam", 1, "email")
	student2 = students.Student("Sam", 2, "email", 75, "Co-ordinator")
	student3 = students.Student("Vera", 3, "email", 70, "Plant")
	student4 = students.Student("Callum", 4, "email", 72)
	student5 = students.Student("Andrew", 5, "email", 79)
	student6 = students.Student("Random", 6, "email")

	test_group = groups.Group(1)
	test_group.add_student(student1)
	test_group.add_student(student2)
	test_group.add_student(student3)
	test_group.add_student(student4)
	test_group.add_student(student5)

	test_group2 = groups.Group(2)
	test_group2.add_student(student6)

	group_list = [test_group, test_group2]

	output = convert_to_CSV(group_list)
	output_more = convert_to_CSV(group_list, more = True)

	print(output)
	print(output_more)
	
	with open('test.csv', 'w', newline='') as csvfile:
		csvfile.write(output)

	with open('test_more.csv', 'w', newline='') as csvfile:
		csvfile.write(output_more)


