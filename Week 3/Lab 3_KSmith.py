#Kyle Smith
#SE126.04
#Lab 3
#1-27-2025

#PROGRAM PROMPT:Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company 
# to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops 
# and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the 
# file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be 
# replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.


#Varible Dictionary:
#total_pcs: Total number of Pcs
#total_laptop: Number of laptops 
#total_desktop: Number of desktops 
#total_cost_desktops: Cost of replacing desktops
#total_cost_laptops: Cost of replacing laptops 

#Imports--------------------
import csv

#Functions-------------------

#Main Code------------------

#initialze variables
 
total_pcs = 0
total_cost_desktops = 0
total_cost_laptops = 0
total_desktop = 0
total_laptop = 0

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
            yr = int (rec[7])
           


        #changing acronyms to  full words
        if rec [0] == 'D':
            rec [0] = "Desktop"

        else: 
            rec[0] = "Laptop"
 
        if rec [1] == 'DL':
            rec[1] = "Dell"
        elif rec [1] == "GW":
            rec [1] = "Gateway"

      
      
        
        if yr <= 16 and rec [0] == "Desktop":
            total_desktop += 1
            total_cost_desktops = 2000 * total_desktop
            

        if yr <= 16 and rec [0] == "Laptop":
            total_laptop += 1
            total_cost_laptops = 1500 * total_laptop
            
       


        print(f"{rec[0]:7}\t  {rec[1]:7}  {cpu:2}     {ram:2}\t  {disk:5}\t    {num:1}  \t      {sec_disk:5} \t {os:3}\t{yr:2}")

#final print of total pcs
print(f"\nThere are {total_pcs} PCs in Total\n")
print("*************************************************")
print (f"To replace {total_desktop} desktops it will cost you: ${total_cost_desktops}")
print(f"To replace {total_laptop} laptops it will cost you: ${total_cost_laptops}")
print("*************************************************\n")
print("Thank You For Using The PC Database Tool!!!\n")
