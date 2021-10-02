# animals = ['python','cat','dog','elephant']
# for animal in animals:
#     print(animal)

# numbers = list((1,2,3,4,5))
# print(numbers[-1])
#----------------------------
#Creating Smaller list out of bigger one.
# import os 
# os.system('tracert 8.8.8.8')
# big_list = ['Jane','Mary','Tom',1,2,3]
# name_list = big_list[0:3]
# second_name_list = big_list[:3]
# number_list = big_list[3:6]
# second_number_list = big_list[3:6]
# print(name_list)
#----------------------------
# list = ['Jonh','Jack','Jane','Adam']
# list[3] = 'Jim'
# list1 = ['dog','cat','bird']
# list2 = [1,2,3,4,5,6]
# sum_list = list1+list2
# del sum_list[2:5]
# list.insert(3,'Hane')
# list.sort()
# print(list)
#-----------------------------
#Tuple
# animal = 'camel'
# for char in animal:
#     print(char)
# number_tuple = (1,2,3,4,5)
# list_from_string = list('Salam windows 11')
# list_from_string_copy = list_from_string.copy()
# number_list = list(number_tuple)
# print(list_from_string,list_from_string_copy)
#----------------------------------
#Dictionary
# kv_dict = {'one':1,'two':2,5:5,}
# print(kv_dict['one'])
# Python Program - Exam Marks
# exam_marks = {'Ruslan':'A','Qewem':'B','Neri':'F'}
# person_name = input('Enter A Name of A Person You Want to Check The Exam Mark: ')
# if person_name not in exam_marks:
#     print('Enter Correct Name')
# else:
#     print('Exam Mark For ' + person_name + ' is ' + exam_marks[person_name] )
#------------------------------------
# age_dict = {'Ruslan':21,'Qedim':22,'Qewem':25,'Neri':30}
# for value1, value2 in age_dict.items():
#     print(value1 + ' age is ' + str(value2))

# person_name = input('Enter Name: ')
# print('Age of '+ person_name + ' is ' + str(age_dict.get(person_name,-1)) + ' years')
#---------------------------------
# dictionary1 = {'a':1,'b':2,'c':3,'d':4,'e':5}
# double_dictionary1 = {k:v*5 for (k,v) in dictionary1.items()}
# num = range(15)
# num_dictionary = {n:n**2 for n in num if n%2 == 1}
# print(num_dictionary)
# dictionary1 = {'a':1,'b':2,'c':3,'d':4,'e':5}
# dictionary2 = {k:v for (k,v) in dictionary1.items() if v > 3 and v % 2 == 0 }
# print(dictionary2)
#-----------------------------------
# string1 = 'Hello \t world \n m\bay '
# print('hello'.capitalize()  in string1)
# print(''.join(('Rus','lan')))
#----------------------------------
# import os
# import subprocess

# os.chdir('c:\\Users\\rusey\\Desktop\\Demosss')
# os.mkdir('Demosss')
#print(os.getcwd())

#open('file.txt','x')
# path_tuple = os.path.split(os.path.abspath('file.txt'))
# path_string = 'This is file name  {0} and directory name {1}'
# print(path_string.format(path_tuple[1],path_tuple[0]))
# open(path_tuple[1],'w').write('This is file  (edited)')
# print(os.path.getsize(path_tuple[1]))
# print(os.path.realpath('file.txt'))
# subprocess.check_output('dir',shell=True)
# os.system('dir')
#-------------------------------
# import os
# # # print(os.getcwd())
# os.chdir('c:\\Users\\rusey\\Desktop\\Demosss')
# file = open('file.txt','r')
# # file.write(' \n Python3.93')
# # print(file.writable())
# dictionary = {1 : 'a', 2: 'b', 3:'c' }
# # for key,value  in dictionary.items():
# #     file.write(str(key) +'\t' + value +'\n' )
# # for line in file.readlines():
# #     print(line)
# file.close()
#-------------------------------
# import os
# print('File and Directory Creation Program')
# print('Your Working Path is: ' + os.getcwd())
# dir_path = input('Insert Directory Path (with \\\): ')
# try:
#     os.makedirs(dir_path, exist_ok = False)
# except FileExistsError as Argument:
#     print(Argument.strerror)
#     print('Directory Already Exists')
# finally:
#     print('Okey, Continue to Insert File')
#     os.chdir(dir_path)
#     file_name = input('Enter File Name: ')
#     if os.path.exists(file_name):
#         file = open(file_name,'a')
#     else:
#         file = open(file_name,'w')
#     file_text = input('Add Text For File: ')
#     file.write('\n'+ file_text[::-1])
#     file.close()
#------------------------------------
def main(*arg):
    pass
def mains(**kwarg):
    pass