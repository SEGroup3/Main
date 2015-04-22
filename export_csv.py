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

        if more:
                output += 'Name, Group, Belbin Role, Grades, Average Grade, Prior Experience, , \n'
        else:
                output += 'Name, Group, \n'

        for item in list_of_groups:

        # Now we construct the data-containing csv rows.
        # Adds each row of the csv file one at a time.

            for entry in item.contents:

                output += '{}, '.format(entry.firstname + ' ' + entry.surname)
                # Digs up the student.name attributes.

                output += '{}, '.format(item.number)
                # Group number
                
                if more:
                        # Digs up the remaining attributes.

                        if entry.role:
                                output += '{}, '.format(entry.role)
                        else:
                                output += ', '
                        if entry.grades:
                                output += '{}, '.format(entry.grades)
                        else:
                                output += ', '
                        if item.get_group_average():
                                output += '{}, '.format(item.get_group_average())
                        else:
                                output += ', '

                        if entry.competency:
                                output += 'Yes, '
                        else:
                                output += 'No, '
                                

                output += '\n'

        return output
