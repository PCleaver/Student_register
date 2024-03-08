# Create a program that allows users to register for an exam venue.

# Open the file in 'a' mode to append to the existing file or create a new one if it doesn't exist
with open("reg_form.txt", "a") as file:
    i = 0
    no_students = int(input("How many students are registering? "))  # Enter number of students registering

    for students in range(i, no_students):
        if no_students > i:
            student_id = input("Enter your student ID: ")  # Student enters their ID number.
            i += 1  # Increment i by 1 for each student

            # Writes out student id in a txt file.
            file.write(f"student ID: {student_id} ................\n")

# Close the file to free up system resources
file.close()

