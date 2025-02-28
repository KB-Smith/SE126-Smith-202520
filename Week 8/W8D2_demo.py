#W8D2 Dictionary Review + Gaining data from Text Files
#this demo utilizes: dictionary_file.csv

#Imports---------------------------------------
import csv
#Main executing Code
library = {
    #'key' : value
    "1230" : "Red Rising",
    "1231" : "The Little Prince"
}

with open ("text_files/dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        #for every record in the file, do the following
        #file --> 2D list; rec --> record's data, also a list!
        library.update({rec[0]: rec[1]})
        #library_num --> rec[0], a string
        #title --------> rec [1], also a string

#disconected from file------------------------

print(f"{'KEY':4}: {"TITle"}")
print("-"* 50 )
for key in library:
    #for every key in the library dictionary
    print(f"{key.upper():4}: {library[key]}")

search = input("\nEnter the Keyyou are looking for: ")

found = 0

for key in library:
    if search.lower() == key.lower():
        found = key

if found != 0:
    print(f"We found your search for {search}, here is the info: ")
    print("-"*50)
    print(f"{key.upper():4}: {library[key]}")
    #for i in range (0,len(found:))
    #print(f"{found[i].upper():4}: {library[found[i]]}")

else: print (f"We could not find your search for {search} :[")