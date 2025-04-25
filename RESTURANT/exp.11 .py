# 1
# # print("Hello world!")


# # 2 Variables and data types 
# name="Alice"
# age=25
# height=5.6
# is_student =True

# print(name,age,height,is_student)


# # 3 taking user input 
# name=input("Enter your name: ")
# print ("hello, "+ name+ "!")


# # 4 Conditional statements 
# num=int(input("Enter a number: "))
# if num>0:
#     print("positive number")
# elif num<0:
#     print("negative number")
# else:
#     print("zero")


# # 5  loops 
# for i in range(5):
#     print(i)

# count=0
# while count<5:
#     print(count)
#     count+=1 

# #6 Functions 
# def greet(name):
#     return "hello, "+ name +"!"
# print (greet("vaibhav"))

# # 7 lists 
# fruits =["apple","banana","cherry "]
# fruits.append("orange")
# print(fruits)


# # 8 Dictionaries
# person={"name": "vaibhav", "age": 25, "city": "New York"}
# print(person["name"])

# # 9 classes and objects 
# class Person:
#     def __init__(self,name,age):
#         self.name =name
#         self.age =age

#     def greet(self):
#         return f"hello, my name is {self.name} and i am {self.age} years old."
# p = Person("vaibhav",21)
# print (p.greet())

# # 10 calculator 
# def calculator(): 
#     num1 = float(input("Enter first number: ")) 
#     operator = input("Enter operator (+, -, *, /): ") 
#     num2 = float(input("Enter second number: ")) 
 
#     if operator == '+': 
#         print("Result:", num1 + num2) 
#     elif operator == '-': 
#         print("Result:", num1 - num2) 
#     elif operator == '*': 
#         print("Result:", num1 * num2) 
#     elif operator == '/': 
#         if num2 != 0: 
#             print("Result:", num1 / num2) 
#         else: 
#             print("Cannot divide by zero!") 
#     else: 
#         print("Invalid operator!") 
 
# calculator()

# # 11 to do list 
# def add_task(task): 
#     tasks.append(task) 
 
# def remove_task(task): 
#     if task in tasks: 
#         tasks.remove(task) 
 
# def show_tasks(): 
#     print("To-Do List:") 
#     for i, task in enumerate(tasks, start=1): 
#         print (f"{i
#                  }. {task}" )
# while True: 
#     choice = input("Choose: add/remove/show/quit: ").lower() 
#     if choice == "add": 
#         task = input("Enter task: ") 
#         add_task(task) 
#     elif choice == "remove": 
#         task = input("Enter task to remove: ") 
#         remove_task(task) 
#     elif choice == "show": 
#         show_tasks() 
#     elif choice == "quit": 
#         break 
#     else: 
#         print("Invalid choice!")

# # 12 to print area of a circle ,square, and rectangle 
# import math

# # Function to calculate area of a circle
# def circle_area(radius):
#     return math.pi * radius ** 2

# # Function to calculate area of a square
# def square_area(side):
#     return side ** 2

# # Function to calculate area of a rectangle
# def rectangle_area(length, width):
#     return length * width

# # Taking user inputs
# radius = float(input("Enter the radius of the circle: "))
# side = float(input("Enter the side of the square: "))
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))

# # Printing the areas
# print(f"Area of the circle: {circle_area(radius):.2f}")
# print(f"Area of the square: {square_area(side):.2f}")
# print(f"Area of the rectangle: {rectangle_area(length, width):.2f}")


#13 wap to print fibonacci 
#Function to print Fibonacci series
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# # Taking user input
# n = int(input("Enter the number of terms: "))

# # Printing Fibonacci series
# print("Fibonacci Series:")
# fibonacci(n)


# # 14 wap to reverse a string and print palindrome or not 
# # Function to reverse a string
# def reverse_string(s):
#     return s[::-1]

# # Function to check palindrome
# def is_palindrome(s):
#     return s == s[::-1]

# # Taking user input
# string = input("Enter a string: ")

# # Reversing the string
# reversed_string = reverse_string(string)

# # Checking if palindrome
# if is_palindrome(string):
#     print(f"The string '{string}' is a palindrome.")
# else:
#     print(f"The string '{string}' is NOT a palindrome.")

# # Printing reversed string
# print(f"Reversed string: {reversed_string}")


# # 15 wap to print patterns 
# # a Taking user input for number of rows
# n = int(input("Enter the number of rows: "))

# # Printing the pattern
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()  # Move to the next line


# # b # Taking user input for number of rows
# n = int(input("Enter the number of rows: "))

# # Printing the pattern
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()  # Move to the next line
