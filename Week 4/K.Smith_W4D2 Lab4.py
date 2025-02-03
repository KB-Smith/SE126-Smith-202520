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


  

#--MAIN EXECUTING CODE----------------------


# Initialize variables
total_records = 0
answer = 0
user_choice = 0
stark_ext = 100
targaryen_ext = 200
tully_ext = 300
lannister_ext = 400
baratheon_ext = 500
nightwatch_ext = 600

#create an empty list for every potential field
firstName = []
lastName = []
age = []
screen_name = []
house = []
email =[]
department=[]
extension =[]

with open ("text_files/got_emails.csv") as csvfile:
    # Reading the CSV file
    file = csv.reader(csvfile)

    for rec in file:
        total_records += 1

        firstName.append(rec[0])
        lastName.append(rec[1])
        age.append(rec[2])
        screen_name.append(rec[3])
        house.append(rec[4])

        if rec[4] == "House Stark":
            department.append("Research & Development")
            extension.append(stark_ext)
            stark_ext+1
        elif rec[4] == "House Targaryen":
            department.append("Marketing")
            extension.append(targaryen_ext)
            targaryen_ext+1
        elif rec[4] == "House Tully":
            department.append("Human Resources")
            extension.append(tully_ext)
            tully_ext+1
        elif rec[4] == "House Lannister":
            department.append("Accounting")
            extension.append(lannister_ext)
            lannister_ext+1
        elif rec[4] == "House Baratheon":
            department.append("Sales")
            extension.append(baratheon_ext)
            baratheon_ext+1
        elif rec[4] == "The Night's Watch":
            department.append("Auditing")
            extension.append(nightwatch_ext)
            nightwatch_ext+1

        

#disconnect from the file -- all file data is retained bc we are using lists
email = [screen_name +'@westeros.net'for screen_name in screen_name]



    

print("--------------------------------------------------------------------------------------------------------")
print(f"{'FIRST':10}  {'LAST':10}      {'EMAIL':35} {'DEPARTMENT':30}  {'EXT':3}" )   
print("--------------------------------------------------------------------------------------------------------")





for index in range(0, len(firstName)): 
    print(f"{firstName[index]:10}  {lastName[index]:10}    {email[index]:35}\t{department[index]:20}\t\t{extension[index]:3}")
print("---------------------------------------------------------------------------------------------------------------\n")



    
