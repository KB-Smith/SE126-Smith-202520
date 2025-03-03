
#--IMPORTS------------------------------------------------------------
import csv

#--MAIN EXECUTING CODE------------------------------------------------

library = {}

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
    