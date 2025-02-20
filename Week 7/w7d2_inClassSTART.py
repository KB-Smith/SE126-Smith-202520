#W7D2 - Live Class: Review of Binary Search & Bubble Sort + 2D Lists

#This demo uses the file: simple.csv (also named simple-2.csv)

#this start file contains a "shell" program, or a coded outline, for the full working program we will build in class to review bubble sort and binary search, as well as introduce basic processing of 2D lists

import csv 


def menu():
    print("Simple Searching Menu")
    print("1. Search by NAME")
    print("2. Search by NUM")
    print("3. Search by COLOR")
    print("4. EXIT")

    menu_choice = input("Enter your search type [1-4]: ")
    return menu_choice

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp


#create your empty 1D parallel lists
names = []
nums = []
colors = []

#we will use the below hand-populated list
valid_menu = ["1", "2", "3", "4"]

with open("text_files/simple-2.csv") as csvfile: 
    file = csv.reader(csvfile)

    for rec in file: 
        names.append(rec[0])
        nums.append(rec[1])
        colors.append(rec[2].title()) #just for Ray in the morning session
#disconnected from file-----------------------
ans = "y"

while ans == "y":
    choice = menu()

    if choice != "1" and choice != "2" and choice != "3" and choice != "4": 
        print("!INVALID ENTRY!\nPlease try again.\n")

    elif choice == "1": #search by NAME
        print("\n~Search by NAME~")


    elif choice == "2": #search by NUM
        print("\n~Search by NUM~")


    elif choice == "3": #search by COLOR
        print("\n~Search by COLOR~")


    else:
        print("\n~EXIT~")
        ans = "X" #ans changes from "y" to end the loop (condition will now eval as false)

print("\nThank you for using my program.\n\t\tGOODBYE!\n")


#------2D Lists ----------------------------------------------------------------------------------------------
#2D lists are just lists that contain 1D lists inside of them! 

