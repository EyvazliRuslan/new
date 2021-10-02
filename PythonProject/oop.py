# class Human:
#     human_count = 0
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         Human.human_count += 1

# human = Human('Ruslan','1999-10-24','Man')
# demo = 'hello'
# print('The are %d human' % (Human.human_count))
# del human.name
# human.name = 'Ad'
# print(hasattr(human,'name'))
# print(human.name)
# print(Human.__module__)
#--------------------------------------
# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y        
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print(class_name, ' destroyed')

# point1 =  Point(10,12)
# point1.__del__()
# print(point1.x)
# print(point1.y)
#--------------------------------------

# class Student:
#     stuCount = 0

#     def __init__(self, fname, lname, subject, grade):
#         self.fname = fname
#         self.lname = lname 
#         self.subject = subject
#         self.grade = grade
#         Student.stuCount += 1

#     def display_students_count(self):
#         print(f'Total Amount of Students is {Student.stuCount}')
    
#     def display_student_information(self):
#         print(f' First Name: {self.fname}\n Last Name: {self.lname}\n Subject: {self.subject}\n Grade: {self.grade}')

# print('Usage...\nq -- Quit The Program\nAdd -- Add Student\nDisplay -- Display Student Information')
# def add_student():
#     student_first_name = input('Enter Student First Name: ')
#     student_last_name = input('Enter Student Last Name: ')
#     student_subject = input('Enter Student Subject: ')
#     student_grade = input('Enter Student grade')
#     Student(student_first_name,student_last_name,student_subject,student_grade)

# def switch_demo():
#     switcher = {
#         'Q':'Quit The Program',
#         'Add':'Add Student',
#         'Display':'Display Student Information'
#     }
#     for key,value in switcher.items():
#         print(key + ' - ' + value)

#     input_key = input('Enter your option: ')
    
#     while True:
#         default_message = 'Invalid Option'
#         key = switcher.get(input_key.capitalize(), default_message)
#         if key == default_message or input_key.lower() == 'q':
#             exit()
#         if input_key.lower() == 'display':
#             input_name = input('Enter Student Name: ')
#             Student.display_student_information(exec(input_name))
#         if input_key.lower() == 'add':
#             add_student()
#             break

# student_one = Student('Ruslan','Eyvazli','Applied Software',95)
# input_name = input('Enter Student Name: ')
# Student.display_student_information(Student(input_name))
# print(type(exec(input_name)))
# switch_demo
#---------------------------------------
# m = 'Ruslan'
# m = iter(m)

# print(next(m))

# class Person:
#     person_count = 0
#     def __init__(self):
#         Person.person_count += 1

#     def info(self,pname):
#         print(pname)
# class Student(Person):
#     def info(self, pname):
#         print(pname,str(self.person_count))
#     def info(self, pname,cname = "default"):
#         print(pname,str(self.person_count),cname)
# #        return super().info(pname)

# class Employee(Person):
#     emp_count = 0
#     def __init__(self,name):
#         Employee.emp_count += 1

# class Tech(Student):
#     def __init_subclass__(cls) -> None:
#         return super().__init_subclass__()
#     def info(self, pname, cname):
#         return super().info(pname, cname)
# class EmpJun(Employee):
#     def __init__(self, name):
#         print('created')
# person = Person()
# person.info('adsdsagdsa')
# student = Student()
# student.info('sasagdgsaf')
# employee = Employee('name')
# employee.info('adsaf')
# tech = Tech()
# tech.info('jfsdk','hafhsjh')
# emp_jun = EmpJun('HI')
# emp_jun.info("demo")
# class Student(Person):
#     def info():


    

# student = Student()
# student.info('string')
#---------------------------------


class Car:
    pass

bmw1 = Car()
bmw1.name = 'bmw'
bmw1.category = 'M3'
bmw1.topspeed = 250

class Carv:
    name = ''
    speed = ''
    def __init__(self) -> None:
        pass

carv1 = Carv()
carv1.name = 'rr'
carv1.email = 'hello'
print(type(carv1.name))