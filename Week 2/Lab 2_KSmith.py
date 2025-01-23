#Kyle Smith
#SE126.04
#Lab 2
#1-16-2025

#PROGRAM PROMPT:You have been asked to produce a report that lists all the computers in the csv file
#filehandling.csv.Your report should look like the following sample output.The last line should print the number of computers in the file.


#Varible Dictionary:
#total_pcs: Total number of Pcs 

#Imports--------------------
import csv

#Functions-------------------

#Main Code------------------

#initialze variables 
total_pcs = 0

#display column headings
print (f"{'Type':7}   {'Brand':7}  {'CPU':2}   {'RAM':2}\t{'1st Disk':5}   {'No.HDD':1}   {'2nd Disk':5}\t {'OS':3}\t{'YR':2}")
print ("---------------------------------------------------------------------------------------------------------------------")
with open ("text_files/filehandling.csv") as csvfile:
    file =csv.reader(csvfile)

    
    #below code occurs for every record (row) in the file
    for rec in file:
        total_pcs +=1

        #assigning variable name to items in each record 
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


        #changing acronyms to  full words
        if rec [0] == 'D':
            rec [0] = "Desktop"

        else: 
            rec[0] = "Laptop"

        if rec [1] == 'DL':
            rec[1] = "Dell"
        elif rec [1] == "GW":
            rec [1] = "Gateway"
        


        print(f"{rec[0]:7}\t  {rec[1]:7}  {cpu:2}     {ram:2}\t  {disk:5}\t    {num:1}  \t      {sec_disk:5} \t {os:3}\t{yr:2}")

#final print of total pcs
print(f"\nThere are {total_pcs} PCs in Total\n")