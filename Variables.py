#Variable is a container that stores data
name = "Shrikant"
#Python detect the dataTypes automatically

#datatypes in python

'''
integer,
Float,
String,
Boolean
'''
# type()-> It is used to check the datatype of the variable
# input()-> By default it returns the string

#Que 1) create variables and print 

name = "Shreyash"
age =  22
city = "Bramhapuri"

print(name)
print(age)
print(city)

#Que 2) Take user Input

name = input("Enter your name : ")
colour = input("Enter your favourite clour : ")
print("Your name is : ",name)
print(name,"your favourite clour is ",colour)

#Que 3) Storing moblie price

mobile_Price = 28500
discount_Price = 28500 * (10/100)
final_Price = mobile_Price - discount_Price
print(final_Price)

#Que 4) Check the datatye

age = 22
salary = 46879.65
name = "Eren"
is_loggedIn = True

print(type(age))
print(type(salary))
print(type(name))
print(type(is_loggedIn))

#Que 5) print age

print("your age after 5 years will be ", age + 5)

#Que 6) Taking input from user

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print("The addition of two numbers is ", a + b)
print("The subtraction of two numbers is ", a - b)

#Que 7)Creating Variables

college = "GECA"
branch = "CSE"
CGPA = 8.29

#Que 8) Converting the datatype

a = 100
a = str(a)
print(type(a))

#Que 9) Taking the decimal values as input

a = float(input("Enter any decimal number : "))
print(a)


#Que 10) Creating the mini Bio-Data
name = input("Enter your name : ")
age = int(input("Enter your age : "))
salary = float(input("Enter your salary : "))
skils = input("Mentioned your skills : ")

#Que 11) Why does Python not require datatype declaration?

'''
Python does not require datatype declarations because it is a dynamically typed and strongly typed language that uses duck typing. 
1. Dynamic Typing
In Python, types are associated with the value, not the variable name. 
How it works: A variable is just a pointer or label that references an object in memory.
Example: When you write x = 5, 
Python creates an integer object with the value 5 in memory and points x to it. 
If you later write x = "Hello", Python creates a string object and points x to the new object. 
The variable x itself has no fixed type.

'''

#Que 12) Why input() always return String

'''
1. Type Safety
If input() tried to guess the data type, typing something like admin could be mistaken for a 
variable named admin. In older versions of Python (Python 2), a function called input() 
actually evaluated the user's input as live code, which created massive security vulnerabilities. 
Returning a string ensures that user input is always treated as harmless text data. 
2. Predictability and Consistency
A program needs to know exactly what data type it is receiving to avoid crashing. 
If input() changed its return type based on what you typed, 
a single function would return an integer sometimes, a float other times, or a list. 
By always returning a string, Python ensures the function behavior is completely predictable. 
'''
#Que 13) Student Profile Generator

name = input("Enter your name : ")
age = int(input("Enter your age : "))
course = input("Enter the course that u pursuing : ")
skills = input("Enter the skills that u have : ")
goal = input("What are your goal in life : ")

print(f"Hey bro your name is {name} and your age is {age} you are pursuing the course{course}, btw you \n are expert in {skills} and your goal is {goal}")