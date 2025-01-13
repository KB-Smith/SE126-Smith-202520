#W2D2 - Text File Jandling Intro Demo 

#Step 1: import the csv )comma sperated vlaue) Library
import csv

total_records = 0 #holds total num of rec in file

#--connected to file ------------------------------------------
#include relative files path in open() and make sure to switch \ to /
with open ("text_files/simple.csv") as csvfile:
    #make sure to to indent inside of the code block


    #allow the csv>reader()to acess and read the file path; stores
    # contents to 'file' [a 2D list / matrix/ table]
    file =csv.reader(csvfile)

    #print for headers
    print(f"{'NAME':10} {'NUM':10} {'COLOR'}")
    print("-----------------------------------------")
    #STEP 3: process through every record (row) in the file
    for  record in file: 
        #add +1 to total_records to keep accurate count of recs
        total_records +=1
        #print(record)#entire record/row data as a list


        name = record[0]
        number = record[1]
        color = record[2]
        print(f"{name:10} {number:3} \t\t{color.title()}")
#--disconncted from file--------------------------------------
print(f"\nTOTAL RECORDS: {total_records}\n")