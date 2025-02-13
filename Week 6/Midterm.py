#Imports------------------
import csv
from os import system, name
import time # Allows for sleep
#Functions-------------------
def clear():#<--function header
    if name == 'nt': 
        _ = system('cls')
    else:
        _ = system('clear')

def menu(): #<- main menu function
    
    print("\t\t**MAIN MENU**")
    print(f"\t1. EMAIL")
    print(f"\t2. DEPARTMENT")
    print(f"\t3. Exit")

    menu_choice = input("\tChoose A Number [1-3]: ")
    

    while menu_choice != "1" and menu_choice != "2" and menu_choice != "3":
        print("\t*** !INVALID ENTRY! ***")
        menu_choice = input("\tCHOOSE A NUMBER BETWEEN 1-3!!!: ")

  
    return menu_choice 


total_records = 0
officeN = 100
user_choice = 0

#create an empty list for every potential field
firstName = []
lastName = []
email =[]
department=[]
extension =[]
officeNum = []

with open ("text_files/westeros.csv") as csvfile:
    # Reading the CSV file
    file = csv.reader(csvfile)

    for rec in file:
        total_records += 1
        firstName.append(rec[0])
        lastName.append(rec[1])
        email.append(rec[2])
        department.append(rec[3])
        extension.append(rec[4])
        
for i in range(0, len(firstName)):
    o = officeN+1
    officeN +=1
    officeNum.append(o)

      
        

    


print("------------------------------------------------------------------------------------------------------------------------------")
print(f"{'FIRST':10}  {'LAST':10}      {'EMAIL':35} {'DEPARTMENT':30}  {'EXT':3}         {'OFFICE NUMBER'}")   
print("----------------------------------------------------------------------------------------------------------------------------------")


for index in range(0, len(firstName)): 
    print(f"{firstName[index]:10}  {lastName[index]:10}    {email[index]:35}\t{department[index]:20}\t\t{extension[index]:3}   \t\t{officeNum[index]:3}")
print("------------------------------------------------------------------------------------------------------------------------------------------\n")

print(f"There are {total_records} employees at this firm")



while user_choice != "3":
        user_choice = menu()

        if user_choice == "1":
            found = -1
            search_email = input("Enter the email you wish to find: ")

            for i in range(len(email)):
                if search_email.lower() == email[i].lower():
                    found = i

            if found != -1:
                print(f"Your search for {search_email} was FOUND! Here is their data: ")
                print(f"{'FIRST':10}  {'LAST':10}      {'EMAIL':35} {'DEPARTMENT':30}  {'EXT':3}         {'OFFICE NUMBER'}")   
                print("----------------------------------------------------------------------------------------------------------------------------------")
                print(f"{firstName[found]:10} {lastName[found]:10} {email[found]:3} \t\t\t{department[found]:15} \t\t{extension[found]:3}\t\t{officeNum[found]:3}")
                print("----------------------------------------------------------------------------------------------------------------------------------")
            else:
                print(f"Your search for {search_email} was NOT FOUND!")
                print("Check your casing and spelling and try again!")
                print("--------------------------------------------------------------------------------------------")
                time.sleep(5) # Sleep for 5 seconds 

        elif user_choice == "2":
            search_DPT = input("Enter the Department you wish to find: ")
            found = []

            for i in range(len(department)):
                if search_DPT.lower() == department[i].lower():
                    found.append(i)

            if not found : 
                print(f"Your search for {search_DPT} was NOT FOUND!")
                print("Check your casing and spelling and try again!")
                print("--------------------------------------------------------------------------------------------")
                time.sleep(4) 

            else:
                print(f"Your search for {search_DPT} was FOUND! Here is their data: ")
                print(f"{'FIRST':10}  {'LAST':10}      {'EMAIL':35} {'DEPARTMENT':30}{'EXT':3}     {'OFFICE NUMBER'}")
                print("----------------------------------------------------------------------------------------------------------------------------------") 
               
                for i in range (0,len(found)):
                    print(f"{firstName[found[i]]:10} {lastName[found[i]]:10} {email[found[i]]:30} \t\t{department[found[i]]:15} \t     {extension[found[i]]:3}\t\t{officeNum[found[i]]:3}")
                    print("------------------------------------------------------------------------------------------------------------------------------")
                    time.sleep(2) 

        elif user_choice == "3":
            print("Exiting....")
            time.sleep(5)
            print("Thank you for using the Westeros Inc Database Tool!")

file = open("midterm_choice1.csv", "w")
for i in range (0,len(firstName)):
    file.write(f"{firstName[[i]]},{lastName[[i]]},{email[[i]]},{department[[i]]},{extension[[i]]},{officeNum[[i]]} ") 
file.close()