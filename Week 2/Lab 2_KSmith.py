#Kyle Smith
#SE126.04
#Lab 2
#1-16-2025

#PROGRAM PROMPT:You have been asked to produce a report that lists all the computers in the csv file
#filehandling.csv.

#Varible Dictionary:

#Imports--------------------
import csv

#Functions-------------------

#Main Code------------------

#initialze variables 
total_pcs = 0

print (f"{'Type':7} {'Brand':7} {'CPU':2} {'RAM':2} {'1st Disk':5} {'No HDD':1} {'2nd Disk':5} {'OS':3} {'YR':2}")
print ("--------------------------------------------------------------------------------------------------------")
with open ("text_files/filehandling.csv") as csvfile:
    file =csv.reader(csvfile)

    

    for rec in file:
        total_pcs +=1

        type = rec[0]
        brand = rec[1]
        cpu = rec[2]
        ram = rec[3]
        disk = rec[4]
        num = int(rec[5])
        sec_disk = rec[6]
        os = rec[7]

        if num == 1:
            sec_disk = "" 
            os = rec[6]
            yr = rec[7]


        if rec [0] == 'D':
            rec [0] = "Desktop"
            
        print(f"{type:7} {brand:7} {cpu:2}   {ram:2}\t  {disk:5}\t   {num:1}  \t{sec_disk:5} \t {os:3} {yr:2}")