Student register program
Description

This program allows users to register for an exam venue. Students are prompted to enter their student ID, and the program records the information in a text file (reg_form.txt).
Getting Started

    Clone the Repository:

    bash

git clone https://github.com/PCleaver/student_register.git
cd student_register

Run the Program:

bash

    python registration_program.py

    Follow the prompts to enter the number of students and their respective IDs.

    Check Registration Details:
    Open the reg_form.txt file to view the recorded registration details.

File Structure

    registration_program.py: The main Python script for student registration.
    reg_form.txt: The text file where registration details are recorded.

Usage

    When prompted, enter the number of students who are registering for the exam.
    For each student, enter their student ID as prompted.
    The program will record the registration details in the reg_form.txt file.

Closing the Program

The program automatically closes the registration file after completion.
Important Notes

    Ensure that Python is installed on your system.
    The program appends new registrations to the existing file (reg_form.txt).

Contributing

Feel free to contribute to the project by opening issues or submitting pull requests.
License

This project is licensed under the MIT License.
