
def __init__(school, name, email, address):
    School.Schoolname = name_of_school
    School.name = name
    School.email = email
    School.address = address

    #creating 'school' class and giving it Values
class School:
    school_name = 'Rose city School'
    school_email = 'Rosecity@gmail.com'
    school_address = ' 123 se main st'

    #creating child classes and giving them value
class Student(School):
    name = 'Charles'
    subject = 'History'
    address = '234 NE MLK Blvd'
    grade = '10th'
    yearsAttended = 2

class Teacher(School):
    name = 'Mr. Thomas'
    subject = 'History'
    address = '534 Main St'
    number_of_students = 34
    yearsTeaching = 17
    
