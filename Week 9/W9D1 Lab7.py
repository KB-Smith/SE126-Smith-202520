
#--IMPORTS------------------------------------------------------------
import csv

#--MAIN EXECUTING CODE------------------------------------------------

library = {}
num_words = 0

with open ("text_files/words.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        library.update({rec[0]: rec[1]})

#disconnect from file
print(f"\n{'WORD'}\t\t{'DEFINITION':30}")
print("-" * 100)
for key in library:
    #for every key (and value) pair found within the 'library' dictionary
    print(f"{key.ljust(15)}\t{library[key]}")
print("-" * 100)


search = input("\nEnter the WORD you are looking for: ")
found = 0

for key in library:
    if search.lower() == key.lower():
        found = key

if found != 0:
    print(f"\nWord: {found:6}\tDefinition: {library[found]:50}")
else:
    print(f"\nYour search for {search} came up empty. Sorry :/ ")

num_words = int(input("Enter the number of words you wish to add: "))

for key in range(num_words): 
    key = input("Enter the word: ")
    value = input("Enter the definition: ")
    library[key] = value

if key in library:
        print("This word already exists in the dictionary already")
        print(f"{key} has now been added to the dictionary!!")

else:
        print(f"{key} has been added to the dictionary!!")
        library.update({rec[0] : rec[1]})
          


print(f"\n{'WORD'}\t\t{'DEFINITION':30}")
print("-" * 100)
for key in library:
    #for every key (and value) pair found within the 'library' dictionary
    print(f"{key.ljust(15)}\t{library[key]}")
print("-" * 100)