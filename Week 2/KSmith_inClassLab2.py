#Kyle Smith
#SE126.04
#Lab 2
#1-16-2025

#PROGRAM PROMPT:The csv file classLab2.csv contains a list of rooms, the maximum number of people that the room
#can accommodate, and the number of people currently registered for the event. Write a program that
#displays all rooms that are over the maximum limit of people and the number of people that have to
#be notified that they will have to be put on the wait list. After the file is completely processed the
#program should display the number of records processed and the number of rooms that are over the limit

#Variable Dictionary:
#max_cap/max: Total number of people the room can hold
#people/ppl: Number of people attending 
#remaining: Space that's left in the room
#diff:returned value from the function
#total_rec: total number of records
#rooms_over: the number of rooms that are over capacity
#name:name of room

#Imports--------------------------------------
import csv

#Function--------------------------------------
def difference(people,max_cap):
    '''This function is passed two values and returns the difference 
    between them'''
    diff = max_cap - people
    return diff #this value will replace the difference() call in the miain code

#Main Code------------------------------------
#initialize needed count variables
total_rec = 0 
rooms_over = 0

#----------conneted to the file-------------------------
with open ("text_files/classLab2.csv") as csvfile:
    #make sure to to indent inside of the code block
    file =csv.reader(csvfile)

    print(f"{'ROOM':20}  \t {'MAX':3}  \t{'PEOPLE':3} \t  {'OVER'}")
    print("----------------------------------------------")

    for rec in file:
        #below code occurs for every record (row) in the file (text file -> 2D list!

        #assig each field data value to a friendly variable name.
        name = rec[0]
        max = int (rec[1]) #all text data is read as a string so cast as a num!
        ppl = int (rec[2])

        #call the difference() to find people over/under capacity
        reamaining = difference(ppl,max)

        #count and display rooms that are over capacity (remaining is negative)
        if reamaining < 0:
            rooms_over += 1
            print(f"{name:20} \t {max:3} \t {ppl:3} \t {reamaining* -1:5}")

        #count ALL roooms
        total_rec += 1

#----------disconnected from the file------------------------

#display final data 
print("----------------------------------------------")
print(f"Rooms currently OVER capacity:{rooms_over}")
print(f"Total rooms in the file:{total_rec}")
print("----------------------------------------------\n")
