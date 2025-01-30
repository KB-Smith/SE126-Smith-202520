#--IMPORTS----------------------------------
import csv
import time # Allows for sleep
from os import system, name
#--FUNCTIONS--------------------------------
def clear():#<--function header
    if name == 'nt': 
        _ = system('cls')
    else:
        _ = system('clear')
def letter(num):

    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let ="F"
    else:
        let = "ERROR"

    return let
def menu(): #<- main menu function
    
    print("\t\t**MAIN MENU**")
    print(f"\t1. Search by LAST name")
    print(f"\t2. Search by FIRST name")
    print(f"\t3. Search by LETTER GRADE")
    print(f"\t4. Exit")

    menu_choice = input("\tChoose A Number [1-4]: ")
    

    while menu_choice != "1" and menu_choice != "2" and menu_choice != "3" and menu_choice != "4":
        print("\t*** !INVALID ENTRY! ***")
        menu_choice = input("\tCHOOSE A NUMBER BETWEEN 1-4!!!: ")

  
    return menu_choice 
   

#--MAIN EXECUTING CODE----------------------


# Initialize variables
total_records = 0
answer = 0
user_choice = 0

#create an empty list for every potential field
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

with open ("text_files/class_grades-2.csv") as csvfile:
    # Reading the CSV file
    file = csv.reader(csvfile)

    for rec in file:
        total_records += 1

        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2])) #cast as integer so we can do math
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnect from the file -- all file data is retained bc we are using lists

#print("----------------------------------------------------------------------------")
#print(f"{'FIRST':10}  {'LAST':10}   {'T1':3}   {'T2':3}    {'T3':3}    {'AVG':3}   {'LET-AVG':3}")
#print("----------------------------------------------------------------------------")

avg = []
let_avg =[]

for i in range(0, len(test1)):
    a = (test1[i] + test2[i] + test3[i]) / 3
    avg.append(a)
    let_avg.append(letter(a))




#for index in range(0, len(firstName)): 
 #   print(f"{firstName[index]:10}  {lastName[index]:10}  {test1[index]:3}   {test2[index]:3}    {test3[index]:3}    {avg[index]:3.1f}      {let_avg[index]}")
#print("--------------------------------------------------------------------------------------\n")


user_choice = menu()
user_choice = 0
    
while user_choice != "4":
        user_choice = menu()

        if user_choice == "1":
            found = -1
            search_last = input("Enter the Last Name you wish to find: ")

            for i in range(len(lastName)):
                if search_last.lower() == lastName[i].lower():
                    found = i

            if found != -1:
                print(f"Your search for {search_last} was FOUND! Here is their data: ")
                print(f"{firstName[found]:10} {lastName[found]:10} {test1[found]:3} {test2[found]:3} {test3[found]:3} {avg[found]:6.1f}")
                print("--------------------------------------------------------------------------------------------")
            else:
                print(f"Your search for {search_last} was NOT FOUND!")
                print("Check your casing and spelling and try again!")
                print("--------------------------------------------------------------------------------------------")
                time.sleep(7) # Sleep for 7 seconds 

        elif user_choice == "2":
            found = -1
            search_first = input("Enter the First Name you wish to find: ")

            for i in range(len(firstName)):
                if search_first.lower() == firstName[i].lower():
                    found = i

            if found != -1:
                print(f"Your search for {search_first} was FOUND! Here is their data: ")
                print(f"{firstName[found]:10} {lastName[found]:10} {test1[found]:3} {test2[found]:3} {test3[found]:3} {avg[found]:6.1f}")
                print("--------------------------------------------------------------------------------------------")
            else:
                print(f"Your search for {search_first} was NOT FOUND!")
                print("Check your casing and spelling and try again!")
                print("--------------------------------------------------------------------------------------------")
                time.sleep(7)   

        elif user_choice == "3":
            found = -1
            search_letter = input("Enter the Letter Grade you wish to find: ")

            for i in range(len(let_avg)):
                if search_letter.lower() == let_avg[i].lower():
                    found = i

            if found != -1:
                    print(f"Your search for {search_letter} was FOUND! Here is their data: ")
                    print(f"{rec[0]:10} {lastName[found]:10} {test1[found]:3} {test2[found]:3} {test3[found]:3} {avg[found]:6.1f}")
                    print("--------------------------------------------------------------------------------------------")
            else:
                print(f"Your search for {search_letter} was NOT FOUND!")
                print("Check your casing and spelling and try again!")
                print("--------------------------------------------------------------------------------------------")
                time.sleep(7) 

        elif user_choice == "4":
            print("Exiting....")
            time.sleep(5)
            print("Thank you for using the Student Database Tool!")
           

        else:
            print("YeeHA!? Please choose again.")
    
