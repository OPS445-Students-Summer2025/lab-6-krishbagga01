#!/usr/bin/env python3
# Author ID: 148191232

class Student:

    # Define the name and number when a student object is created
    def __init__(self, name, number):
        self.name = str(name)           # Ensure name is a string
        self.number = str(number)       # Convert number to string if it's passed as int
        self.courses = {}               # Dictionary to hold courses and grades

    # Return student name and number
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # Add a new course and grade to student record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the GPA and return a formatted string
    def displayGPA(self):
        if not self.courses:  # Avoid division by zero
            return 'GPA of student ' + self.name + ' is 0.0'
        total = sum(self.courses.values())
        gpa = total / len(self.courses)
        return 'GPA of student ' + self.name + ' is ' + str(gpa)

    # Return list of passed courses (grade > 0.0)
    def displayCourses(self):
        passed = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)  # Int passed for student number
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
