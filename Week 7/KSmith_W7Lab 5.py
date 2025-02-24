#Kyle Smith
#SE126.04
#Lab 4
#2-21-2025

#PROGRAM PROMPT:tore the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options.
#Your program should give your user the following menu:
#Personal Library Menu
#1. Show All Titles – list all book data to the user alphabetically by title
#2. Search by Title – allow for an entire title or a title key word
#3. Search by Author – show all titles of the searched-for author
#4. Search by Genre - show all titles of the searched-for genre
#5. Search by Library Number – only allow for one specific library number item
#6. Show All Available – show all titles with status “available”
#7. Show All On Loan - show all titles with status “on loan”
#8. EXIT
#When your user runs any of the options 1 – 7, show all data associated with the search [Library Number, Title, Author,
#Genre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches
#should not be case sensitive.
#---------------------------------------------------------
#Variable Dictionary:

#total_records: Total number of records
#user_choice: Stores numbers for menu options





#Imports------------------
import csv
import time # Allows for sleep
#Functions-------------------
def menu():#<- main menu function
    print("~Personal Library Menu~")
    print("1. Show All Titles")
    print("2. Search by Title")
    print("3. Search by Author") 
    print("4. Search by Genre")
    print("5. Search by Library Number")
    print("6. Show All Available")
    print("7. Show All On Loan")
    print("8. EXIT")
    

    menu_choice = input("Enter your search type [1-8]: ")

    while menu_choice not in ["1", "2", "3", "4","5","6","7","8"]:
        print("\t*** !INVALID ENTRY! ***")
        menu_choice = input("\tCHOOSE A NUMBER BETWEEN 1-8!!!: ")

    return menu_choice


#initialize variables
total_records = 0
user_choice = 0

#create an empty list for every potential field

library_num = []
title = []
author = []
genre = []
page_count = []
status = []
found = []

with open ("text_files/book_list.csv") as csvfile:
    # Reading the CSV file
    file = csv.reader(csvfile)

    for rec in file:
        total_records += 1
        library_num.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3])
        page_count.append(rec[4])
        status.append(rec[5])

#print("----------------------------------------------------------------------------------------------------------------------------------------------------")
#print(f"{'LIBRARY NUM':4}\t{'TITLE':30}\t\t{'AUTHOR':35}\t{'GENRE':20}\t{'PAGE#':3}\t\t{'STATUS':10}")   
#print("----------------------------------------------------------------------------------------------------------------------------------------------------")

#for index in range(0, len(library_num)):
    # print(f"{library_num[index]:4}\t\t{title[index]:34}    {author[index]:35}\t{genre[index]:20}\t{page_count[index]:3}   \t\t{status[index]:10}")
#print("------------------------------------------------------------------------------------------------------------------------------------------\n")


#--MAIN EXECUTING CODE----------------------

while user_choice != "8":
    user_choice = menu()

    if user_choice == "1":
        for i in range(0, total_records - 1):

            for k in range(0, total_records - 1):

                if (title[k] > title[k + 1]):

                    temp = title[k]
                    title[k] = title[k + 1]
                    title[k + 1] = temp

                   
            # prints Collumn Headers
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"{'LIBRARY NUM':4}\t{'TITLE':30}\t\t{'AUTHOR':35}\t{'GENRE':20}\t{'PAGE#':3}\t\t{'STATUS':10}")   
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")

            # printing the data
        for index in range(0, len(library_num)):
            print(f"{library_num[index]:4}\t\t{title[index]:34}    {author[index]:35}\t{genre[index]:20}\t{page_count[index]:3}   \t\t{status[index]:10}")
            print("------------------------------------------------------------------------------------------------------------------------------------------\n")


    elif user_choice == "2":

        
        search = input("Enter the Title of the Book: ")
        
        found = []   

       
        for i in range(len(title)):
            if search.lower() in title[i].lower():  
                found.append(i)

        if not found:
             
            print(f"Sorry, '{search}' was NOT found!!! Please try again.")


        else:
            print(f"Found these Books:")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"{'LIBRARY NUM':4}\t{'TITLE':30}\t\t{'AUTHOR':35}\t{'GENRE':20}\t{'PAGE#':3}\t\t{'STATUS':10}")   
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")

            for index in found:
                
                print(f"{library_num[index]:4}\t\t{title[index]:34}    {author[index]:35}\t{genre[index]:20}\t{page_count[index]:3}   \t\t{status[index]:10}")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")


            
    elif user_choice == "3":

        search = input("Enter the Author of the Book: ")
        
        found = []   

       
        for i in range(len(author)):
            if search.lower() in author[i].lower():  
                found.append(i)

        if not found:
            print(f"Sorry, '{search}' was NOT found!!! Please try again.")

        
    
        
        else:
            print(f"Found these Books:")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"{'LIBRARY NUM':4}\t{'TITLE':30}\t\t{'AUTHOR':35}\t{'GENRE':20}\t{'PAGE#':3}\t\t{'STATUS':10}")   
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")
            for index in found:
                print(f"{library_num[index]:4}\t\t{title[index]:34}    {author[index]:35}\t{genre[index]:20}\t{page_count[index]:3}   \t\t{status[index]:10}")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")

    
    elif user_choice == "4":

        search = input("Enter the Genre of the Book: ")
            
        found = []   

        
        for i in range(len(genre)):
                if search.lower() in genre[i].lower():  
                    found.append(i)

        if not found:
                print(f"Sorry, '{search}' was NOT found!!! Please try again.")
           
        else:
                print(f"Found these Books:")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")
                print(f"{'LIBRARY NUM':4}\t{'TITLE':30}\t\t{'AUTHOR':35}\t{'GENRE':20}\t{'PAGE#':3}\t\t{'STATUS':10}")   
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")
                for index in found:
                    print(f"{library_num[index]:4}\t\t{title[index]:34}    {author[index]:35}\t{genre[index]:20}\t{page_count[index]:3}   \t\t{status[index]:10}")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------") 

    
    
    elif user_choice == "5":
        
        found = -1
        search = input("Enter the Library Number of the book: ")

        for i in range(len(library_num)):
                if search == library_num [i]:
                    found = i
        
        if found != -1:


            print(f"Found these Books:")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"{'LIBRARY NUM':4}\t{'TITLE':30}\t\t{'AUTHOR':35}\t{'GENRE':20}\t{'PAGE#':3}\t\t{'STATUS':10}")   
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"{library_num[found]:4}\t\t{title[found]:34}    {author[found]:35}\t{genre[found]:20}\t{page_count[found]:3}   \t\t{status[found]:10}")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")    
           
            
            
        else:

           
            print(f"The Library Number {search} was NOT FOUND!")
            print("Check the number and try again!")
            print("--------------------------------------------------------------------------------------------")
            time.sleep(5) # Sleep for 5 seconds

    
    elif user_choice == "6":
              
        found = []   

       
        for i in range(len(status)):
            if status[i] == "available":  
                found.append(i)
       
           
        print(f"Found these Books:")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"{'LIBRARY NUM':4}\t{'TITLE':30}\t\t{'AUTHOR':35}\t{'GENRE':20}\t{'PAGE#':3}\t\t{'STATUS':10}")   
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        for index in found:
                print(f"{library_num[index]:4}\t\t{title[index]:34}    {author[index]:35}\t{genre[index]:20}\t{page_count[index]:3}   \t\t{status[index]:10}")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")


    elif user_choice == "7":
              
        found = []   

       
        for i in range(len(status)):
            if status[i] == "on loan":  
                found.append(i)
       
           
        print(f"Found these Books:")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"{'LIBRARY NUM':4}\t{'TITLE':30}\t\t{'AUTHOR':35}\t{'GENRE':20}\t{'PAGE#':3}\t\t{'STATUS':10}")   
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        for index in found:
                print(f"{library_num[index]:4}\t\t{title[index]:34}    {author[index]:35}\t{genre[index]:20}\t{page_count[index]:3}   \t\t{status[index]:10}")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    
    else: 
         print("\nThank you for using the Personal Library Tool!!!\n\t\tGOODBYE!\nShutting down........")
         time.sleep(3)