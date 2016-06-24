# A class of students

## Overview
We need an application for teachers to keep track of students and their grades.

## Details
Assume for now, there is a single teacher and a single class. Here's what you need to do.

1. Think of a way to store the student data in a file (say students.txt). An example format can be:

	    StudentName StudentPhoneNumber Marks1 Marks2 Marks3 Marks4

	Read up on JSON and try to store data in JSON format.
2. Create a Python class, Student. It'll have all the attributes of the student (StudentName, StudentPhoneNumber, etc.)
3. Make a function to read student data from file
4. Make a function to add a new student to the file and remove a student from the file
5. Make a function to edit student data
6. Try making the above functions members of the Student class (python class)
7. Make a command line interface that asks me (teacher) what I want to do (add a student, remove a student, edit) and then calls the appropriate function