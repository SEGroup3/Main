import students
import groups
import pickle
import auto_test

def sort_students(stu_dict, group_count, group_size):

    '''Sorts students into the number of groups of the given size.

    Takes a student dictionary and returns a list of group objects.

    If you don't give it enough students, the function will fill groups until
    it runs out.

    If you give it too few groups it will add students until the groups are
    full.

    The algorithm will try to put the student into a group with no other
    students who share that Belbin role. If that is impossible, the student will
    be placed into the first available group.
    '''

    # Create the required number of groups.
    group_list = []
    i = 1
    while i <= group_count:
        group_list.append(groups.Group(i))
        i += 1

    # Extract the students from the dict
    stu_list = list(stu_dict.values())

    # Iterate over all the students and place them in a group with no shared Belbin roles
    for a_student in stu_list:
        stu_index = stu_list.index(a_student)
        for item in group_list:
            
            if item.get_group_size() < group_size:

                for entry in item.contents:
                    
                    if entry.role == a_student.role:
                        
                        break # skip to next group
                    
                else: # runs if no shared roles are found

                    student_to_add = stu_list.pop(stu_index)
                    item.add_student(student_to_add)

                    if len(stu_list) == 0:
                        # Remove empty groups
                        return remove_empty_groups(group_list)
                    else:
                        break # move to next student
            else:
                pass # move to next student


    else: # If for loop completes with a return, fill groups without checking Belbin role
        while len(stu_list) > 0 and not test_group_sizes(group_list, group_size):
            # This loop will run until it runs out of students or group space.
            for a_student in stu_list:
                stu_index = stu_list.index(a_student)

                for a_group in group_list:
                    if a_group.get_group_size() < group_size:
                        student_to_add = stu_list.pop(stu_index)
                        a_group.add_student(student_to_add)
                        break

        # Remove empty groups
        return remove_empty_groups(group_list)

def remove_empty_groups(group_list):

        for each_group in list(group_list):
            if each_group.get_group_size() == 0:
                group_list = [item for item in group_list if item != each_group]

        for each_group in group_list:
            print(each_group)
            print(each_group.get_group_size())
        
        return group_list
    
                    
def test_group_sizes(group_list, group_size):
    '''Returns True if all group sizes in group_list match group_size, otherwise returns False.'''

    for item in group_list:
        if item.get_group_size() < group_size:
            return False
    else:
        return True
        



if __name__ == "__main__":

    all_students = auto_test.list_of_students(15)
    all_dict = {}

    for item in all_students:
        all_dict[item.number] = item

    with open("stu_dict.pkl", "wb") as db:
        pickle.dump(all_dict, db)

    with open("stu_dict.pkl", "rb") as db:
        stu_dict = pickle.load(db)

    grp_list = sort_students(stu_dict, group_count = 3, group_size = 5)
    for item in grp_list:
        print(item)

    
