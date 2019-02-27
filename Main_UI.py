
import DB

# Welcome!
print('\n')
print("Welcome to the Student Database.")
print('\n')

# Create DB table, if it does not already exist
DB.create_table()

# UI
selection = 0
while (selection == 0):
    print("Please make a selection:")
    print("     [1] Display all students")
    print("     [2] Add a student")
    print("     [3] Update a student")
    print("     [4] Delete a student")
    print("     [5] Search for a student")
    print("     [6] To Exit")

    selection_try = input(">>")

    if selection_try <= 0 | selection_try > 6:
        selection = 0
    else:
        selection = selection_try

        if selection == 1:
            DB.list_all()
            selection = 0

        if selection == 2:
            add_id = input("Enter a unique Student ID:")
            add_fn = raw_input("Enter the Student's First Name:")
            add_ln = raw_input("Enter the Student's Last Name:")
            add_gpa = input("Enter the Student's GPA:")
            add_major = raw_input("Enter the Student's Major:")
            add_fa = raw_input("Enter the Student's Faculty Advisor:")

            DB.add_student(add_id, add_fn, add_ln, add_gpa, add_major, add_fa)
            print(add_fn + " " + add_ln + " added!")
            selection = 0

        if selection == 3:
            update_studentID = input("Enter Student's ID to Edit:")
            update_major = raw_input("Enter new Major:")
            update_fa = raw_input("Enter new Faculty Advisor:")

            DB.update_student(update_studentID, update_major, update_fa)
            print("Student is updated!")
            selection = 0

        if selection == 4:
            delete_studentID = input("Enter Student's ID to delete them from the database:")
            DB.delete_student(delete_studentID)
            print("Student deleted!")
            selection = 0

        if selection == 5:

            print("[1] Major")
            print("[2] GPA")
            print("[3] Advisor")
            search_by = input("Search by:")

            DB.search_by(search_by)

        if selection == 6:
            break

