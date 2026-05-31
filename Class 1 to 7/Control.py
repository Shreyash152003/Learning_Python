#1 What is control flow
'''
➡️ Which code runs
➡️ When it runs
➡️ How many times it runs
'''
#2 If Statement
#Used for decision making.

#3 Tndentation (VERY IMPORTANT)
#Python uses spaces/tabs to define blocks.

#4 if-else Statement
#When condition is false.

#5 elif Statement
#Used for multiple conditions.

#6 Nested if
#if inside another if.

#7 Loops in Python
'''
Loops repeat code.
Two main loops:
for loop
while loop
'''
#8 For Loop
'''
Used when number of repetitions is known.
for i in range(5):
    print(i)

**range(start, stop)**
for i in range(1, 6):
    print(i)

***range(start, stop, step)***
for i in range(1, 10, 2):
    print(i)
'''

#9 While Loop
'''
Runs until condition becomes false.
while condition:
    code

Example:
count = 1

while count <= 5:
    print(count)
    count += 1

Infinite Loop
Dangerous if condition never becomes false.
while True:
    print("Hello")

'''

#10 break Statement
'''
Stops loop immediately.
for i in range(10):
    if i == 5:
        break
    print(i)
'''

#11 Continue Statement
'''
Skips current iteration.
for i in range(5):
    if i == 2:
        continue
    print(i)
'''

#12 pass Statement
'''
Placeholder statement.
if True:
    pass
'''
#13 Loop Inside Loop (Nested Loop)
'''
for i in range(3):
    for j in range(2):
        print(i, j)
'''
#Q1) Check if number is positive or negative.
a = int(input("Enter the number : "))
if a>0:
    print(a,"is postivie number")
else:
    print(a,"is negative number")

#Q2) Check if age is eligible for voting.
age = int(input("Enter your age : "))
if age>=18:
    print("You are elligible to vote")
else:
    print("You are not elligible to vote")

#Q3 Take marks and print Pass or Fail
marks = int(input("Enter your marks : "))
if marks>=35:
    print("Pass")
else:
    print("Fail")

#Q4 Print numbers from 1 to 10 using for loop.
for i in range (1,11):
    print(i)

#Q5 Print even numbers from 1 to 20.
for i in range (1,21):
    if i%2==0:
        print(i)

#Q6 Print multiplication table of a number.
num = int(input("Enter the number : "))
for i in range (1,11):
   print(f"{num} * {i} = {num * i}")

#Q7 Find sum of numbers from 1 to 100.
sum = 0
for i in range (1,101):
    sum += i
print(sum)

#Q8 Print all odd numbers between 1 to 25 using while loop.

j = 1
while(j<25):
    if j%2 !=0:
        print(j)
    j=j+1

#Q9 Check largest among three numbers.
p = int(input("Enter the first number : "))
q = int(input("Enter the second number : "))
r = int(input("Enter the third number : "))

if(p>q and p>r):
    print(f"{p} is greater than {q} and {r}")
elif(q>p and q>r):
    print(f"{q} is greater than {p} and {r}")
else:
    print(f"{r} is grater than {p} and {q}")

#Q10 Create login system using if-else.
username = input("Enter your username : ")
password = input("Enter your password : ")

if(username=="Admin"):
    if(password=="admin@123"):
        print("You are logged in as an admin")
    else:
        print("Wrong Password")
elif(username == "Shreyash"):
    if(password=="shrey@123"):
        print("You have successfully logged in to the system")
    else:
        print("Wrong password")
else:
    print("Username not found")

#Q11 Create ATM simulation:Check PIN Withdraw money Check balance

c_pin = 2428
balence = 10000

money = int(input("Enter the money that u want to withdraw: "))
if(money > balence):
    print("Invalid balence")
if money <= balence:
    pin = int(input("Enter the four digit pin : "))
    if(pin != c_pin):
        print("Invalid pin")
    else:
        withraw = balence - money
        print(f"You have successfully withdrawn {money} ₹ ")
        print("Your current balence is ",withraw)

#Q12 Create number guessing game.
number = int(input("Enter the number of your choice between 1 to 100 : "))
b = int(input("Enter the guessing number : "))
while number != b:
    if(number > b):
     print("Too Low")
    else:
        print("Too high")
    b = int(input("Enter the guessing number : "))

print("congratulations your  guess is correct")

#Q13) Print Fibonacci series using loop.
a = 0
b = 1
for i in range (10):
    c = a + b
    print(a)
    a = b
    b = c
    c = a

#Q14) Student grade system

score = int(input("Enter your Score : "))
if score > 90:
    print("Your grade is A ")
elif(score>75 and score <=90):
    print("Your grade is B")
elif(score>50 and score<=75):
    print("Your grade is C")
else:
    print("Sorry bro/sis better luck next time you are failed in exam")

#Q15) Password Checker
passkey = input("Enter your password : ")
if(passkey == "pytho123"):
    print("Password is correct ")
else:
    print("Wrong password")

#Q16)Countdown Timer
count = 10
while(count>=1):
    print(count)
    count = count - 1

#Q16) print numberd from 1 to 50 and skip multiples of 5
for i in range (1,51):
    if(i%5==0):
        continue
    else:
        print(i)