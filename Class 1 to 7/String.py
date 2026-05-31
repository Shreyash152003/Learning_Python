#************************STRINGS IN PYTHON********************
#1)A string is a sequence of characters.
#2) String Indexing -> Every character has an index
#3) Negative indexing -> print(name[-1]) -> n if the string is "python"
#4) String Slicing -> string[start:end] ex: name = "Shreyash",print(name[0:4]) -> Shre

name = "Shreyash"
print(name[:])
print(name[2:4])
print(name[-1])
print(name[2:])
print(name[:5])
print(name[::2])

#5)Strings are Immutable->name = "Python" -> name[0] = "J" -> not allowed

'''
***************CORRECT****************
name = "Python"

name = "J" + name[1:]

Jython
'''

'''
***************************STRING METHODS******************************
1)upper()
2)lower()
3)title()
4)capitalize()

5)strip() -> Remove spaces

6)replace()
ex: text = "I like Java" -> print(text.replace("Java", "Python"))

7)find() -> Returns index.
ex:
text = "Machine Learning"
print(text.find("Learning")) -> 8

8)count()
ex: text = "banana"
print(text.count("a")) -> 3

9)startswith()
ex: email = "admin@gmail.com"
print(email.startswith("admin")) -> True

10)endswith()
rint(email.endswith(".com")) -> True

11)String Concatenation
ex:first = "Shreyash"
last = "Janbandhu"
print(first + " " + last)

12)String Repetition
print("python ",*3)

13)Memembership Operators
text = "Machine Learning"
print("Learning" in text) -> True

14)f-Strings
name = "Shreyash"
age = 22
print(f"My name is {name} and I am {age} years old")

15)Looping Through Strings
name = "Python"
for ch in name:
    print(ch)

16)Reverse String
text = "Python"
print(text[::-1]) -> nohtyP

17)split()
Removes leading spaces
Removes trailing spaces
Handles multiple spaces between words
'''

#**********************PRATICE QUESTIONS********************

#Q1)Print first character of your name.
name = "Shreyash"
print(name[0])

#Q2)Print last character.
print(name[-1])

#Q3)Convert string to uppercase.
print(name.upper())

#Q4)Replace one word with another.
text = "I love my country and the name of country is India"
print(text.replace("country","nation"))

#Q5)Count vowels in a string.
sentence = "The Quick Brown fox jump over the lazy dog"
sentence=sentence.strip().lower()
count = 0
for ch in sentence:
    if ch in "aeiou":
        count = count + 1
print(count)

#Q6)Reverse a string.
task = "complete the submssion"
print(task[::-1])

#Q7)Check palindrome.
word = "radar"
word = word.strip().lower()
if word[::-1] == word:
    print(f"{word} is a pallindrome")
else:
    print(f"{word} is not pallindrome")

#8)Count words in a sentence.
que = "     I am a stusent of gov          clg of          engg Aurangabad   "
print(que.strip().count(" ")+1)
print(len(que.split())) #always use split() to count the number of words

#9)Check whether email ends with ".com".
email = "arvinjambulkhar11@gmail.com"
print(email.endswith(".com"))

#10)Find frequency of a character.
title = "Education is the key to success"
title = title.strip().lower()
print(title.count('e'))

#11)Password validator:
password = input("Enter your password : ")
if len(password) <8:
    print("password length should be of 8 characters")

else:
    has_upper = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper=True
        if ch.isdigit():
            has_digit=True
    if not has_upper:
        print("Password should contains atleast one uppercase letter")
    elif not has_digit:
        print("Password should contain atleat one digit")
    else:
        print(f"{password} is valid")

#Q12)Username generator
f_name = input("Enter your First Name : ")
l_name = input("Enter your Last Name : ")
print("*****************Your username is generated as follows**************")
f_name = f_name[0].lower() + f_name[1:]
l_name = l_name[0].lower() + l_name[1:]
print(f"{f_name}_{l_name}")

#Q13)Text Analyzer
def noOF_words(word):
    count = len(word.split())
    return count
def total_characters(word):
    word = word.strip().lower()
    count = 0
    for ch in  word:
        count = count + 1
    return count
def vowel_count(word):
    word = word.strip().lower()
    count = 0
    for ch in  word:
        if ch in "aeiou":
            count = count + 1
    return count
def consonants_count(word):
    word = word.strip().lower()
    count = 0
    for ch in  word:
        if ch not in "aeiou":
            count = count + 1
    return count

word = input("Enter the text you want to analyze : ")
print(f"The numbe of words in the given string : {noOF_words(word)}")
print(f"The numbe of Characters in the given string : {total_characters(word)}")
print(f"The numbe of vowels in the given string : {vowel_count(word)}")
print(f"The numbe of consonants in the given string : {consonants_count(word)}")


#Q14)Simple Chatbot
print("Whats in your mind : ")
message = input("Type your message : ")
if message.strip().lower() == "hi":
    print("Hi there How can I help you today.....")
if message.strip().lower() == "good morning":
    print("Hey Good Morning what are u thinking about just tell me : ")
    newmessage = input("Tell me bro : ")
    if newmessage.strip().lower()=="i am depressed":
         print("Don't panic I am here for you take deep breath and calm dowm..... it's just a situation we will handle it.")

#Email Validator
mail =   input("Enter your email : ")
hasa = False
hasc = False
for ch in mail:
    if ch == '@':
        hasa = True
    
if mail.endswith('.com'):
    hasc=True
if not hasa:
    print("The email does not conatain @ ")
elif not hasc:
    print("The email  .com so this email is invalid...")
else:
    print("It is a valid mail")

    
#**************************Contact Management System***************************
contacts = []
def Add_contact():
    id = int(input("Enter your id : "))
    name = input("Enter your name : ")
    phone = input("Enter your phone number : ")
    email = input("Enter your email : ")
    contact = {
        "name" : name,
        "phone" : phone,
        "email":email,
        "id":id
     }
    contacts.append(contact)
def View_Contacts():
    for contact in contacts:
        print("*************************")
        for key,value in contact.items():
            print(f"{key} : {value}")
        print("***************************")

def Search_By_Id(target_id):
    found = False
    for contact in contacts:
        if contact["id"]==target_id:
            found = True
            for key,value in contact.items():
                print(f"{key} : {value}")
    if not found:
        print("Sorry, but the contact is not found in database....")
def main_menu():
    while True:
        print("**************CONTACT MANAGEMENT SYSTEM*******************")
        print("1.Add Contact")
        print("2.Search contact by id : ")
        print("3.Show contacts in database")
        print("4.Exit")

        choice=int(input("Enter your choice from 1 to 4 :"))
        if choice==1:
            Add_contact()
        if choice==2:
            identity = int(input("Enter the ID : "))
            Search_By_Id(identity)
        if choice==3:
            View_Contacts()
        if choice==4:
            print("..............We are successfully exting from the database..........")
            break
main_menu()

