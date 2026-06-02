########################## QUESTIONS FOR PRATICE ###############################
#Q1)Create a file and write your name.
with open ('data.txt','w') as file :
    file.write("Shreyash")

#Q2)Read data from file
with open('data.txt','r') as file:
    info = file.read()
    print(info)

#Q3)Append a new line.
with open('data.txt','a') as file:
    file.write("\nShrujan")

#Q4)Print file line by line.
with open('data.txt','r') as file:
    for row in file:
        print(row,end='')

#Q5)Count number of lines in a file.
count = 0
with open('data.txt','r') as file:
    for row in file:
        count = count + 1
print(f"\n{count}")

#Q6)Store 5 student names in a file.
with open ('data.txt','a') as file :
    file.write("\n Anuj")
    file.write("\nSamyak")
    file.write("\nManish")
    file.write("\nGaurav")
    file.write("\nChaitanya")

#Q7)Search a name inside a file.
found = False
with open ('data.txt','r') as file:
    for row in file :
        
        if row.strip() == "Anuj":
            found = True
            break
    if found:
        print("Anuj has been found")
    else:
        print("Sorry, Anuj not found")

#Q8) Copy contents from one file to another.
with open ('data.txt','r') as file:
    for row in file:
        with open('text.txt','a') as info:
            info.write(row)

#Q9) Create a simple notes app.
def add_note():
    count = 1
    content = input("Enter your note : ")
    with open('notes.txt','a') as file:
        file.write(f"{count}.{content}\n")
        count = count + 1

def search_note():
    search = input("Enter what do u want to search : ")
    search = search.strip().lower()
    found = False
    with open('notes.txt','r') as file:
        for row in file:
            if search in row.strip().lower() :
                print("Note Found:")
                print(row)
                found = True
                break
        if not found:
            print(f"Sorry the note regarding to {search} is not fouond.....")

def view_notes():
    with open('notes.txt','r') as file:
        for index, row in enumerate(file,start=1):
            print(f"{index}. {row}")

def delete_note():

    note = input("Enter the note that you want to delete : ")
    note = note.strip().lower()

    found = False

    with open('notes.txt', 'r') as file:
        lines = file.readlines()

    updated_notes = []

    for row in lines:

        if note in row.strip().lower():

            print(f"Deleting note: {row.strip()}")
            found = True

        else:

            updated_notes.append(row)

    with open('notes.txt', 'w') as file:
        file.writelines(updated_notes)

    if not found:
        print("Sorry, note not found...")
                







def main_menu():
    while True:
        print("*************SIMPLE NOTES APP********************")
        print("1.Add Note")
        print("2.Search note ")
        print("3.View Notes ")
        print("4.Delete note ")
        print("5.Exit")
        print("**************SIMPLE NOTES APP*********************")

        choice = int(input("Enter your choice from 1 to 4 : "))
        if choice == 1:
            add_note()
        elif choice == 2:
            search_note()
        elif choice == 3:
            view_notes()
        elif choice == 4:
            delete_note()
        elif choice == 5:
            print("Exting from the app see u soon ")
            break
        else:
            print("Invalid Choice")
main_menu()



