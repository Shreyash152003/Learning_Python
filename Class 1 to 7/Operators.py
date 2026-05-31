#Operators 
'''
Operators perform operations on values

Types Of Operators
| Type       | Example    |
| ---------- | ---------- |
| Arithmetic | + - * /    |
| Comparison | == != >    |
| Logical    | and or not |
| Assignment | = += -=    |
| Membership | in         |
| Identity   | is         |


###Airthematic Operators###
| Operator | Meaning        |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraction    |
| *        | Multiplication |
| /        | Division       |
| %        | Modulus        |
| //       | Floor division |
| **       | Power          |

Division Always gives float
// -> called as floor division it removes the decimal
** -> power 

### Comparision Operator
gives boolean result
| Operator | Meaning          |
| -------- | ---------------- |
| ==       | Equal            |
| !=       | Not equal        |
| >        | Greater          |
| <        | Smaller          |
| >=       | Greater or equal |
| <=       | Smaller or equal |

= -> Assignment
== -> Comparision

### Logical Operator
| Operator | Meaning              |
| -------- | -------------------- |
| and      | Both conditions true |
| or       | Any one true         |
| not      | Reverse result       |

### Assignment Operator

| Operator | Example |
| -------- | ------- |
| +=       | x += 5  |
| -=       | x -= 5  |
| *=       | x *= 5  |
| /=       | x /= 5  |

### Memembership Operator
| Operator | Meaning     |
| -------- | ----------- |
| in       | Present     |
| not in   | Not present |

### Identity Operator
| Operator | Meaning          |
| -------- | ---------------- |
| is       | Same object      |
| is not   | Different object |

a = 10
b = 10

print(a is b)
true


### Operator Precedence
BODAMAS
'''

# Que 1) Take two intergers and perform Airthematic Operations

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print("Addition is  : ", a + b);
print("Subtraction is  : ", a - b);
print("Multiplication is  : ", a * b);
print("Division is  : ", a  // b);

# Que 2) Find the remainder

print("The remainder of 25 divide by 4 is : ", 25 % 4)

# Que 3) find suare
print("The square of 6 is : ", 6**2)

# Que 4) 
print(10 > 5)
print(20 != 20)

# Que 5)
age = int (input("Enter your age : "))
print(age>=18)

# Que 6) Check the number is even or odd
num = int(input("Enter the number of your choice : "))
if num%2 == 0 :
    print("Even number")
else:
    print("Odd number")

# Que 7) Compare two numbers
p = int(input("Enter the first number : "))
q = int(input("Enter the second number : "))
if(p>q):
    print(p,"is greater than",q)
elif(q>p):
    print(q,"is greater than",p)
else:
    print("Both are equal")

# Que 8) Using And Operator
print(age>18 and age < 60)

# Que 9) Memembership Operator
name = "Shreyash"
print('h' in name)

#Que 10) Why is % important in programming?
#Without the modulo operator, programmers would have to write complex, 
# multi-line math formulas involving decimals and rounding just to find a simple remainder. 
# Modulo makes code faster, cleaner, and much easier to read.

# Que 11) Where are logical operators used in real projects?
'''
In real-world projects, 
logical operators (AND, OR, NOT—or &&, ||, ! in 
languages like JavaScript, Java, and C++) 
are the brain cells of an application. 
They are rarely used for simple math homework; 
instead, they control security, user experience, 
data filtering, and business logic.

'''


