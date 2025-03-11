#Kyle Smith
#SE126.04
#Lab 7
#3-4-2025

#PROGRAM PROMPT:Access the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and
#the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a
#user to interact with the dictionary based on the following menu:
#My Programming Dictionary Menu
#1. Show all words – Show all words and their definitions stored to the dictionary
#2. Search for a word – Allow the user to enter a word and if it is in the dictionary, show its definition (tell the user if
#the word is not in the dictionary)
#3. Add a word – Allow a user to add a word and its definition to the dictionary if it does not already exist
#4. EXIT
#The program should not be case sensitive for user input, and the user should only be able to quit when they have
#selected menu option number 4.
#---------------------------------------------------------

#Variable Dictionary:
#num_words: number of words the user wants to add
#n_word: new word
#n_definition: new definition
#user_choice: Stores numbers for menu options

#--IMPORTS------------------------------------------------------------
import csv
#--FUNCTIONS----------------------------------------------------------
def menu():

    print("\n~Library Dictionary Tool~")
    print("1.  Show All Words")
    print("2.  Search For A Word")
    print("3.  Add A Word")
    print("3.5 Show All Words (A-Z)")
    print("4.  EXIT")

    menu_choice = input("Enter your search type [1-4]: ")

    while menu_choice not in ["1", "2", "3","3.5", "4",]:
        print("\t*** !INVALID ENTRY! ***")
        menu_choice = input("\tCHOOSE A NUMBER BETWEEN 1-4!!!: ")
    return menu_choice

#--MAIN EXECUTING CODE------------------------------------------------

library = {}
num_words = 0
n_word = 0
n_definition = 0
user_choice = 0

with open ("text_files/words.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        library.update({rec[0]: rec[1]})


while user_choice != "4":
    user_choice = menu()

    if user_choice == "1":

        print(f"\n{'WORD'}\t\t{'DEFINITION':30}")
        print("-" * 150)
        for key in library:
            #for every key (and value) pair found within the 'library' dictionary
            print(f"{key.ljust(15)}\t{library[key]}")
            print("-" * 150)
    
    elif user_choice == "2":
        search = input("\nEnter the WORD you are looking for: ").lower()
        found = 0

        for key in library:
            if search.lower() == key.lower():
                found = key

        if found != 0:
            print(f"\nWord: {found:6}\tDefinition: {library[found]:50}")
        else:
            print(f"\nYour search for {search} came up empty. Sorry :/ ")
    
    elif user_choice == "3":
        num_words = int(input("Enter the number of words you wish to add: "))
        for _ in range(num_words):
            n_word = input("Enter the word: ").lower()
            
            while  n_word in library:
                print(f"{n_word} already exists in the dictionary.")
                n_word = input("Enter the word: ").lower()

            n_definition = input("Enter the definition: ")
            library[n_word] = n_definition
            print(f"{n_word} has been added to the dictionary!")


        print(f"\n{'WORD'}\t\t{'DEFINITION':30}")
        print("-" * 150)
        for key in library:
            #for every key (and value) pair found within the 'library' dictionary
            print(f"{key.ljust(15)}\t{library[key]}")
        print("-" * 150)

    elif user_choice == "3.5":

        print(f"\n{'WORD'}\t\t{'DEFINITION':30}")
        print("-" * 100)
        for key in sorted(library.keys()):  #sort the keys alphabetically using the sorted() method
            print(f"{key.ljust(15)}\t{library[key]}")
        print("-" * 100)

    else:
        print("Thank you for using The Library\n\t\tGoodbye...")
    