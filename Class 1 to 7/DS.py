#*********************Everything in programming revolves around DATA**********************************
#1)1. What are Data Structures?
#->Data structures are ways to store and organize data efficiently.
'''
Python provides:
Lists
Tuples
Sets
Dictionaries
'''
# Real-Life Analogy
'''
| Data Structure | Real-Life Example    |
| -------------- | -------------------- |
| List           | Shopping list        |
| Tuple          | Aadhaar data (fixed) |
| Set            | Unique roll numbers  |
| Dictionary     | Student record       |
'''

#2)Lists in Python
#Multiple values
# Ordered data
# Mutable data (can change)
'''
Creating a List
numbers = [10, 20, 30, 40]
List index starts from 0

Example:
fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[2])

#NEGATIVE INDEXING
print(fruits[-1]) -> MANGO

#UPDATING
fruits[1] = "orange"

*************************List Methods***************************
append()
Adds element at end.

fruits.append("grapes")

insert()
fruits.insert(1, "kiwi")

remove()
fruits.remove("apple")

pop()
Removes by index.
fruits.pop(1)

sort()
numbers.sort()

reverse()
numbers.reverse()

*************************************Looping Through List***********************************
for item in fruits:
    print(item)

*************************************List Slicing*******************************************
numbers = [1,2,3,4,5]
print(numbers[1:4])

'''

#3)Tuples
#Ordered
#Immutable (cannot change)
'''
*********************Creating Tuple**************************
data = (10, 20, 30)

********************Why Tuples?*******************
Used when data should NOT change.
Example:
coordinates
dates
fixed records
'''

#4)SETS
#Unique values
#No duplicates
#No indexing
'''
****************Creating Set***************
nums = {1,2,3,4}

***************Duplicate Removal***********
nums = {1,1,2,2,3}
print(nums)
{1,2,3}

**************Set Methods*****************
add()
nums.add(10)

remove()
nums.remove(2)

'''
#5)Dictionaries
#key : value
'''
***************Creating Dictionary***********************
student = {
    "name": "Shreyash",
    "age": 21,
    "marks": 95
}

************Accessing Value*****************************
print(student["name"])

************Updating Dictionary************************
student["marks"] = 99

************Adding New Key*****************************
student["city"] = "Pune"

************Dictionary Methods************************
keys()
print(student.keys())

values()
print(student.values())

items()
print(student.items())

*******************Looping Through Dictionary**************
for key, value in student.items():
    print(key, value)
'''

#6)Nested Data Structures
'''
Very important for:
APIs
JSON
ML data
Real projects

Example:
students = [

    {
        "name": "Shreyash",
        "marks": 90
    },

    {
        "name": "Rahul",
        "marks": 80
    }

]
'''
#7)List Comprehension
'''
**********Normal Way************
squares = []

for i in range(5):
    squares.append(i*i)

*************List Comprehension Way*******
squares = [i*i for i in range(5)]

*************Conditional List Comprehension**********
even = [i for i in range(10) if i % 2 == 0]

*******TRICKS***********
| Structure  | Shortcut Memory    |
| ---------- | ------------------ |
| List       | Mutable collection |
| Tuple      | Fixed data         |
| Set        | Unique values      |
| Dictionary | Key-value storage  |

'''
#------------------_____________________--------------------____________________________------------
#Qusetions for pratice
#Q1)Create list of 5 fruits.
fruits = ["apple","orange","grapes","watermelon","Banana"]

#Q2)Print first and last element.
print(fruits[0])
print(fruits[-1])

#Q3)Add new element using append().
fruits.append("Mango")
print(fruits)

#Q4)Remove element from list.
fruits.remove("apple")
print(fruits)

#Q5)Create tuple of 5 numbers.
nums = (26,15,11,17,29)
print(nums)

#Q6)Create set and remove duplicates.
value = {1,2,2,3,1,"shreyash","channu","70","marri",94,"shreyash"}
print(value)

#Q7)Create dictionary for student details.

student_Details = {
    "name" : "Shreyash",
    "age"  : 22,
    "gender": "Male",
    "DOB": "15 Aug 2003",
    "Address":"Bramhapuri",
    "Mobile No." : 7028545283
}

#Q8)Loop through dictionary.
for  key,value in student_Details.items():
    print(f" {key} : {value}")

#Q9)Create nested list of students.
students = [
    {
        "name" : "Rohan",
        "age"  : 22,
        "Education" : "B.tech"
    },
    
    {
        "name" : "Mrunal",
        "age"  : 22,
        "Education" : "B.tech"
    },
    {
        "name" : "Samyak",
        "age"  : 22,
        "Education" : "Pursuing BSC Agri"
    },

]
for item in students:
    for key,value in item.items():
        print(f"{key} : {value}")
    print()

#Q10)Create even number list using list comprehension.
even = [i for i in range (1,21) if i%2==0 ]
print(even)


#***********************MOVIE RECOMMENDATION SYSTEM****************************
movies = [
    {
        "name": "Dhurandhar: The Revenge",
        "Industry": "Bollywood",
        "Director": "Jaskirat Singh Rang",
        "Genre":" Action / Crime / Thriller",
        "Duration": "3h 55m",
        "Actors": "Hamza Ali Mazari",
        "Actresses": "Yasmin",
        "Rating": "8.3/10",
        "Collection": "₹1,374.68 crore" 
        
    },

     {
        "name": "Border 2",
        "Industry": "Bollywood",
        "Director": "Anurag Singh",
        "Genre":"War / Action / Historical",
        "Duration": "3h 20m",
        "Actors": "Sunny Deol, Varun Dhawan, Diljit Dosanjhi",
        "Actresses": "N/A ",
        "Rating": "5.9/10",
        "Collection": "₹424.05 crore " 
        
    },
    {
        "name": "Bhooth Bangla",
        "Industry": "Bollywood",
        "Director": "Priyadarshan",
        "Genre":"Comedy / Horror",
        "Duration": "2h 53m",
        "Actors": "Akshay Kumar, Paresh Rawal",
        "Actresses": "Tabu ",
        "Rating": "6.0/10",
        "Collection": "₹203 crore" 
    }
]
def main_menu():
    while True:
        print("*********MOVIE RECOMMENDATION SYSTEM****************")
        print()
        print("Which type of movie do u like to watch : ")
        print("I will ask some questions please provide me answers :  ")
        print("1.Name of the movie ?")
        print("2.Which Industry Bollywood or Hollywood ?")
        print("3.Which Director ?")
        print("4.Which type of movie ? ")
        print("5.Movie Duration ? ")
        print("6. which Actor ? ")
        print("7. Whic actress ? ")
        print("8. Range of Rating ? ")
        print("Select any one of the choice from 1 to 8")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            found = False
            name = input("Enter the name of the movie : ")
            for movie in movies:
                 if name == movie["name"]:
                    for key,value in movie.items():
                        print(f"{key} : {value}")
                    found = True
                    break
            if not found:
                print("Movie not present in database")
        
        elif choice == 2 :
            found = False
            industry = input("Enter the type of Industry : ")
            for movie in movies:
                if industry.lower() == movie["Industry"].lower():
                    for key,value in movie.items():
                        print(f"{key} : {value}")
                    found = True
                 
            if not found:
                print("Sorry Brother better luck next time")
'''
Similarily we can add functionality to the rest of the numbers 

'''

                        
       
        




main_menu()