#WD2 - Sequential Search Review + Creating & Writing to Text Files 

#Program Prompt: 

#IMPORTS---------------------------------
import csv
#FUCTIONS------------------------------------

#MAIN CODE-----------------------------------

#Create empty Lists for every field
dragons =[] #field 0 dragon names 
riders = [] #field 1 rider names
counts = [] #num of colors 
color1 = []
color2 = []

with open("text_files/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        dragons.append(rec[0])
        riders.append(rec[1])
        counts.append(rec[2])
        color1.append(rec[3])
        #color2.append(rec[4])

        if rec [2] == "2": 
            color2.append(rec[3])

        elif rec[2] == "1":
            color2.append("----")

        else:
            color2.append("ERROR")
#disconnected from file-----------------------

#provess lists to display to the console
print(f"{'DRAGONS':15} {'RIDERS':30} {'#':3} {'COLOR 1':8} {'COLOR 2':8}")
print("-----------------------------------------------------------------------")

for i in range (0,len(dragons)):
    print(f"{dragons[i]:15} {riders[i]:30} {counts[i]:3} {color1[i]:8} {color2[i]:8}")
    print("-----------------------------------------------------------------------")


#SEARCH FOR A SPECIFIC DRAGON
#step1: setup and grain of search
found = "x"
search = input("Which dragon are you looking for: ")

#step 2: perform search --> for loop w/ of statement 
for i in range(0,len(dragons)):
    if search.lower()in dragons[i].lower():
        #hold onto the found location (indext) of our searched for value
        found = i

#step 3: filter and display results 
if found != "x": 
        print(f"Your search for {search} has been FOUND:")
        print(f"{dragons[found]:15} {riders[found]:30} {counts[found]:3} {color1[found]:8} {color2[found]:8}")
    
else:
        print(f"Your search for {search} was NOT FOUND:")


#SEARCH For COL
# searcf OR SET
found =[]
search = input("Enter the color you are looking for: ")

for i in range (0,len(color1)):
     if search.lower() in color1[i] or search.lower() in color2[i]:
          found.append(i)


#WRITE SOME DATA TO A FILE + CREATING SAILD FILE
file = open("targs.csv", "w")

for i in range (0,len(dragons)):
     file