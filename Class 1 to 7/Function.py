#1 What is function
'''
A function is a reusable block of code.
Instead of writing same code again and again,
we create a function once and reuse it.
'''
#2 Synatx for creating function and calling the function
'''
def function fun_name():
    code
greet()
'''
#3 Function with paramaters
'''
def greet(name):
    print("Hello", name)
greet("Shreyash")
'''

#4 Function with multiple paramaters
'''
def student(name, age):
    print(name, age)

student("Shreyash", 21)
'''

#5 Argument vs Parameter
'''
| Term      | Meaning                  |
| --------- | ------------------------ |
| Parameter | Variable inside function |
| Argument  | Actual value passed      |

def add(a, b): -> a,b are parmaters
    add(10,20) -> arguments
'''
#6Reurn Statement
'''
Used to return value from function.
def add(a, b):
    return a + b

result = add(10, 5)

print(result)
'''

#7 Difference Between print() and return
'''
print()
Displays output only.

return
Sends value back for reuse.

def square(num):
    return num * num

x = square(5)

print(x)
'''

#8 Default Paramater
'''
def country(name="India"):
    print(name)

country()
country("USA")
'''
#9 Keyword Argument
'''
def student(name, age):
    print(name, age)

student(age=21, name="Shreyash")
'''
#10 Local vs Global Variables
'''
Local Variable
Inside function only.
def test():
    x = 10

Global variable
Outside function.
x = 100

def test():
    print(x)
'''
#11 Lambda Function
'''
Small one-line anonymous functions.

Syntax
lambda arguments : expression

square = lambda x: x * x
print(square(5))

'''
#12 Recurrsion
'''
Function calling itself.
'''
#***************************QUESTIONS TO PRATICE**********************************
#Q1)Create function to print your name.
def name():
    print("My name is Shreyash")
name()

#Q2)Create function to add two numbers.
def add(a,b):
    return a+b
result = add(15,18)
print(result)

#Q3)Create function to find square of number.
square = lambda x : x*x #lambda function
res = square(15)
print(res)

#Q4)Create function that takes age and prints eligibility.
def elligibility(age):
    if(age >= 18):
        print("You are elligible to vote...")
    else:
        print("You are not elligible to vote")

elligibility(25)

#Q5)Create greeting function using parameter.
def greeting (name):
    print("Good morning",name)
greeting("Botu")

#Q6)Create calculator using functions.
def Addition(a,b):
    return a+b
def Subtraction(a,b):
    return a-b
def Division(a,b):
    return a//b
def Multiplication(a,b):
    return a*b
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = input("Enter the operation that u want to perform +,-,*,/ : ")

if c=='+':
   ans= Addition(a,b)
   print(f"Addition of {a} and {b} is {ans}")
elif c=='-':
    ans = Subtraction(a,b)
    print(f" Subtraction of {a} and {b} is {ans}")
elif c=='*':
    ans = Multiplication(a,b)
    print(f" Multiplication of {a} and {b} is {ans}")
elif c=='/' :
   ans =  Division(a,b)
   print(f" Division of {a} and {b} is {ans}")
else:
    print("Invalid Operation")

#Q7)Create function to find maximum of two numbers.
def max_num (x,y):
    if x > y:
        return x
    elif x<y:
        return y
    else:
        print("Both are equal")

sol = max_num(7,8)
print(sol)

#Q8)Create function to count vowels in string.
def count_vowles(word):
    count = 0
    for i in range (len(word)):
        if(word[i]=='a'or word[i]=='e'or word[i]=='i' or word[i]=='o' or word[i]=='u'):
            count  = count + 1
    return count
sentence = input("Enter the string of your choice : ")
print(f" The number of vowles are : {count_vowles(sentence)}")

#Q9)Create function to check even/odd.
def even_odd(num):
    if num%2==0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
even_odd(25)

#Q10)Create recursive factorial program.
def factorial(n):
    if n==1 or n==0:
        return 1
    return n * factorial(n-1)
n = int(input("Enter the number of your choice : "))
solution = factorial(n)
print(f"The factorial of {n} is {solution}")

#Q11)Create recursive Fibonacci series.
'''
def fib(p):
    if p==0 :
        return 0
    if p==1 :
        return 1
    return fib(p-1) + fib(p-2)

print(f"{fib(5)}")

#Q12)Create lambda function for cube.

ele = int(input("Enter the number of which u want cube : "))
cube = lambda x : x*x*x
print(f"The cube of {ele} is {cube(ele)}")

#Q13)Create student management system using functions.

student_DB = []
def add_Student(id,name,score):
    student = {
        "id" : id,
        "name" : name,
        "score" : score,
    }
    student_DB.append(student)
    print("Student data has successfully added in the database")

def studen_data():
    if not student_DB:
        print("No student database has found.....")
    for student in student_DB:
       print("*******************************")
       print("ID : ",student["id"])
       print("Name: ",student["name"])
       print("Score: ",student["score"])

def get_Student_BY_Id(target_Id):
    found = False
    for student in student_DB:
        if student["id"] == target_Id:
            print("Id : ", student["id"])
            print("Name : ", student["name"])
            print("Score : ", student["score"])
            found = True
            break
    if not found:
        print("Student not found")

def main_menu():
    while True:
        print("\n-------Student management System-----------")
        print("1. Add student")
        print("2. View student details")
        print("3. Get the particular student")
        print("4. Exit")

        choice = input("Enter the choice from 1 to 4 : ")

        if choice=='1':
            id = int(input("Enter thr student Id : "))
            name = input("Enter the student name : ")
            score = int(input("Enter the score of the student : "))
            add_Student(id,name,score)
        elif choice=='2':
            studen_data()
        elif choice=='3':
            a = int(input("Enter the id of the student : "))
            get_Student_BY_Id(a)
        elif choice=='4':
            print("Exiting the program , GoodBye! have a nice day....")
            break;
        else:
            print("Invalid choice janeman")
main_menu()
'''
#Q14)Create menu-driven banking system.
Customer_DB = []
def Add_Customer(id,name,age,DOB,gender,balence):
    customer ={
        "id" : id,
        "name" : name,
        "age" : age,
        "DOB" : DOB,
        "gender":gender,
        "balence":balence
    }
    Customer_DB.append(customer)
    print("Customer has been successfully in the database")
 
def view_Customers():
    if not Customer_DB:
        print("No customer database has found........ ")
    for cust in Customer_DB:
        print("***************************************")
        print("ID : ",cust["id"])
        print("Name : ",cust["name"])
        print("Age : ",cust["age"])
        print("DOB : ",cust["DOB"])
        print("Gender : ",cust["gender"])
        print("Balence : ",cust["balence"])

def get_Customer_By_Id(target_Id):
    found = False
    for cust in Customer_DB:
        if cust["id"]==target_Id:
            print("ID : ",cust["id"])
            print("Name : ",cust["name"])
            print("Age : ",cust["age"])
            print("DOB : ",cust["DOB"])
            print("Gender : ",cust["gender"])
            print("Balence : ",cust["balence"])
            found = True
            break
    if not found:
        print("Customer not found bhai.......")

def check_balence (id):
    found = False
    choice = input("Enter 1 to withraw money or 2 to credit in your account")
    if choice == '1':
        amount = int(input("Enter the amount you want to withraw : "))
        for custo in Customer_DB:
            if custo["id"]==id:
                custo["balence"] = custo['balence']-amount
                print(f"you have successfully withrawn {amount} ₹ and your balence is {custo['balence']-amount}")
    
    if choice == '2':
        amount = int(input("Enter the amount you want to add in your account : "))
        for custo in Customer_DB:
            if custo["id"]==id:
                custo["balece"] = custo["balence"]+amount
                print(f"you have successfully added {amount} ₹ and your balence is {custo["balence"]+amount}")

def main_menu():
    while True:
        print("_____--------BANK MANAGEMENT SYSTEM--------__________")
        print("1.Add customer")
        print("2.View customer details")
        print("3.Get customer by ID")
        print("4.Check Balence")
        print("5. Exit")

        choice = input("Enter your choice from 1 to 5")
        if choice == '1':
            id = input("Enter the ID : ")
            name = input("Enter your name : ")
            age = int(input("Enter your age : "))
            dob = input("Enter your DOB : ")
            gender = input("Enter your gender M for male , F for female and X for others")
            balence = int(input("Enter your balence : "))
            Add_Customer(id,name,age,dob,gender,balence)
        elif choice == '2':
            view_Customers()
        elif choice == '3':
            n = int(input("Enter the id of the customer whose detaisl u want : "))
            get_Customer_By_Id(n)
        elif choice == '4':
            n = int(input("Enter the id of the customer whose balence u want to check: "))
            check_balence(n)
        elif choice == '5':
            print("Exiting thanks for visiting our bank, see you soon....., GoodBye!!!")
            break;
        else:
            print("Invalid choice janeman!!!!")

main_menu()
        


        




