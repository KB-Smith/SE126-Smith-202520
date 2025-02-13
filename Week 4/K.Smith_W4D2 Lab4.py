#Kyle Smith
#SE126.04
#Lab 4
#2-3-2025

#PROGRAM PROMPT:Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in
#the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique
#email address, a department, and a unique phone extension.Once you have completed populating all eight parallel lists and displaying the five 
#required back to the user (and in the same Python file), create and write the following data for each employee to a file named westeros.csv: first name, last name, email, department, and phone extension. 
#note: each employee’s data should be on its own record (row) within
#the newly created file. You will most likely end up with an extra empty line at the end of the file (this is okay for this lab
#as we will not be reprocessing the data found in this new file).
#Once the file is ready, close it and alert the user via a displayed message. Also tell them how many employees are in the
#file, and the total count of employees for each department

#Variable Dictionary:
#total_records = total amount of records in the file.
#rd_count = rd counter
#mk_count = marketing counter
#hr_count = hr counter
#acc_count= accounting counter
#sales_count = sales counter
#audit_count = audit counter
#firstName = first name of character
#lastName = last name of character
#age = age of character
#screen_name = screen name
#house = house they are apart of 
#email =email address
#department= dept they work in
#extension = phone extension


#--IMPORTS----------------------------------
import csv
import random
#--FUNCTIONS--------------------------------
  

#--MAIN EXECUTING CODE----------------------


# Initialize variables
total_records = 0
#create an empty list for every potential field
firstName = []
lastName = []
age = []
screen_name = []
house = []
email =[]
department=[]
extension =[]


rd_count = 0
mk_count = 0
hr_count = 0
acc_count= 0
sales_count = 0
audit_count = 0


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
            extension.append(random.randint(100,199))
            rd_count+=1
        elif rec[4] == "House Targaryen":
            department.append("Marketing")
            extension.append(random.randint(200,299))
            mk_count+=1
        elif rec[4] == "House Tully":
            department.append("Human Resources")
            extension.append(random.randint(300,399))
            hr_count+=1
        elif rec[4] == "House Lannister":
            department.append("Accounting")
            extension.append(random.randint(400,499))
            acc_count+=1
        elif rec[4] == "House Baratheon":
            department.append("Sales")
            extension.append(random.randint(500,599))
            sales_count+=1
        elif rec[4] == "The Night's Watch":
            department.append("Auditing")
            extension.append(random.randint(600,699)) 
            audit_count+=1         

    
#disconnect from the file -- all file data is retained bc we are using lists
email = [screen_name +'@westeros.net'for screen_name in screen_name]


#printing collumn headers
print("--------------------------------------------------------------------------------------------------------")
print(f"{'FIRST':10}  {'LAST':10}      {'EMAIL':35} {'DEPARTMENT':30}  {'EXT':3}" )   
print("--------------------------------------------------------------------------------------------------------")


#printing all the data
for index in range(0, len(firstName)): 
    print(f"{firstName[index]:10}  {lastName[index]:10}    {email[index]:35}\t{department[index]:20}\t\t{extension[index]:3}")
print("---------------------------------------------------------------------------------------------------------------\n")

print(f"Total Employees:{total_records}")
print(f"Department Totals:\nR&D:{rd_count}\nMarketing:{mk_count}\nHR:{hr_count} \nAccounting:{acc_count} \nSales:{sales_count} \nAudit:{audit_count} ")
print("-----------------------------------------------------------------------------------------------------------------")

#create and write the new database to a new text file:
file = open('text_files/westeros.csv', 'w')

for i in range(0, len(firstName)):
    file.write(f"{firstName[i]},{lastName[i]},{email[i]},{department[i]},{extension[i]}\n")

file.close()

    
