# number_one = input("Enter the first number: ")
# number_one = int(number_one)
# number_two = input('Enter the second number: ')
# number_two = int(number_two)
# print("Calculating Result: ")
# if number_one <= number_two:  
#     result = number_one * number_two
# else:
#     result = number_one ** number_two
# print("Result : " + str(result))
# print(5>3)

# password = input("Please write password: ")
# real_password = "Password123"
# if password == real_password:
#     print(True)
# else:
#     print(False)
# while True:
#     print("ldfnl")

# printed_password = input("Please write pass here: ")
# password = "pass123"
# while printed_password != password:
#     printed_password = input("Please write pass here: ")
    
# default_password = 'toor'
# password = ''
# new_password = ''
# repeated_password = ''
# while True:
#     if password != default_password:
#         password = input('Please, enter default password: ')
    
#     if password == default_password:
#         new_password = input('Please, chance default password: ')
#         repeated_password = input('Please, repeat password: ')
#         if repeated_password == new_password:
#             break
# i=0
# while True:
#     if i<100:
#         i += 10
#         continue
#     else:
#         print(i) 
#         break
# for i in range(10,-1,-1):
#     print('hello'+str(i)) 
# import os
# import subprocess

# def hello_world_print():
#     print('hello world!')



# def hello_world_print(string):
#     if string:
#         print(string)
#     else:
#         print('hello world!')
# hello_world_print('')
# hello_world_print('hello')        

#----------------------------------------
#random number
# import random

# random_number = random.randint(1,5)

# def getNumber(number):
#     if number == 1:
#         return 'The number is ' + str(number)
#     elif number == 2:
#         return 'The number is ' + str(number)
#     elif number == 3:
#         return 'The number is ' + str(number)
#     elif number == 4:
#         return 'The number is ' + str(number)
#     else:
#         return 'The number is ' + str(number)

# result = getNumber(random_number)
# print(result)

# def pr():
#     return print('jfn')
# pr()

#--------------------
#guess number
# import random

# def guess_number(secretNumber):
#     global guessNumber
#     for i in range(4):
#         print('Try to guess number!')
#         guessNumber = int(input('Enter Number between 1 and 20: '))
#         if guessNumber < secretNumber:
#             print('Your number a bit low')
#         elif guessNumber > secretNumber:
#             print('Your number a bit high')
#         else:
#             break
# def check_number(guessNumber,secretNumber):
#     if guessNumber == secretNumber:
#         print('Congratulations!, correct number is ' + str(secretNumber))
#     else:
#         print('Good luck next time, correct number is ' + str(secretNumber))

# secretNumber = random.randint(1,20)

# print(' I am thinking of a number ')

# guess_number(secretNumber)
# check_number(guessNumber,secretNumber)

#---------------------------

# string = input('Enter any string: ')
# def reverse_string(string):
#     print(string[::-1])
# number = int(input('Enter any number: '))
# def even_odd(number):
#     if number%2 == 0:
#         print('This number is even')
#     else:
#         print('This number is odd')
# even_odd(number)

#--------------------------
#Python Program - Calculate Area of Circle
# import math
# import sys
# pi = math.pi

# def calculate_radius(radius):
#     # if radius.upper() == 'Q':
#     #     sys.exit()
#     # else:
#     area = int(pi * (int(radius) ** 2))
#     print('Area of the Circle is ' + str(area))

# print('If you want to exit press \'Q\' ')
# while True:
#     radius = input('Enter radius of the Circle: ')

#     if radius.upper() == 'Q':
#         break
    
#     calculate_radius(radius)
#------------------------------
#Python program - Simple Python calculator
# print('1. Addition')
# print('2. Substraction')
# print('3. Multiplication')
# print('4. Division')
# print('5. Exit')
# def calc(char):
#     print(eval(number_one+char+number_two))
# def numbers():
#     global number_one,number_two
#     number_one = input('Enter Number One: ')
#     number_two = input('Enter Number Two: ')
# def calculate(choice):
#     if choice >=1 and choice<=4:
#         numbers()
#     else:
#         print('Please insert number between [1,5]')
        
#     if choice == 1:
#         calc('+')
#     elif choice == 2:
#         calc('-')
#     elif choice == 3:
#         calc('*')
#     else:
#         calc('/')
        

# while True:
#     choice = int(input('Enter Choice: '))
#     if choice == 5:
#         break
#     else:
#         calculate(choice)
# print(int('2 + 4'))
#---------------------------------------
#Python Program - Remove Vowels From Specified String
# def remove_vowels(string):
#     vowels = ('a','e','i','o','u')
#     for c in string.lower():
#         if c in vowels:
#             string = string.replace(c,'')
#     return string
# print('Enter x for exit')
# string = input('Enter Any String To Remove All Vowels From It: ')
# if string == 'x':
#     exit()
# newStr = remove_vowels(string)

# print(newStr)
#-------------------------------------
#Python Program - Find Largest Out Of Three Numbers

# print('Enter \'Q\' to quit program')
# print('Enter Numbers!')

# inputQ = input('Enter \'Q\'to quit or: \nEnter The First Number: ') 
# if inputQ.upper() == 'Q':
#     exit()

# num1 = int(inputQ)
# num2 = int(input('Enter The Second Number: '))
# num3 = int(input('Enter The Third Number: '))
# largest = num1
# if largest < num2 or largest < num3:
#     if num2 < num3: 
#         largest = num3
#     else:
#         largest = num2
# if num1 == num2 == num3:
#     print('All Numbers are equal')
# print(largest)
#----------------------