#W3D2 - List Review - 1Dimensional Lists & Parallel Lists

#this file uses: class_grades.csv 

#--IMPORTS----------------------------------
import csv
#--FUNCTIONS--------------------------------

#--MAIN EXECUTING CODE----------------------

total_records = 0 

#create an empty list for every potential field
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

with open("text_files/class_grades.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #fname = rec[0]
        #print(fname)
        #test_1 = rec[2]

        #stired data from current record to its corresponding list (1 list per field)
        #.append() --> to adds data to the next available space in the list(end)
        #parallel list --> data dispersed across lists, connected by the same index

        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2])) #cast as integer so we can do math
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnect from the file -- all file data is retained bc we are using lists

#processing lists - USE A FOR LOOP
print("----------------------------------------------------------------------------")
print(f"STUDENT ID {'#':3} : {'FIRST':10}  {'LAST':10}  {'T1':3}  {'T2':3}  {'T3':3}")
print("----------------------------------------------------------------------------")



for index in range(0, len(firstName)): 
    #for every item, idex will start at 0 and run up to (not including) the length (# of items)
    #len() --> length of collection, returns # of items
    #index --> key of the list, allows acces to ONE specific value 
    print(f"STUDENT ID {index:3} : {firstName[index]:10}  {lastName[index]:10}  {test1[index]:3}  {test2[index]:3}  {test3[index]:3}")
print("--------------------------------------------------------------------------------------\n")



#create a new list to hold each student's test score average
avg = []

#process the current student data to find and store each student's test score avg to the avg list 
for i in range(0, len(test1)):
    a = (test1[i] + test2[i] + test3[i]) / 3
    avg.append(a)
    #could also: avg.append((test1[i] + test2[i] + test3[i]) / 3)

print(f"\nSTUDENT ID {'#':3} : {'FIRST':10}  {'LAST':10}  {'T1':3}  {'T2':3}  {'T3':3}  {'AVG':3}")
print("------------------------------------------------------------------------")
for index in range(0, len(firstName)): #len() --> length of collection, returns # of items
    #index --> key of the list, allows acces to ONE specific value 
    print(f"STUDENT ID {index:3} : {firstName[index]:10}  {lastName[index]:10}  {test1[index]:3}  {test2[index]:3}  {test3[index]:3}   {avg[index]:3.2f}")
print("------------------------------------------------------------------------\n")

#find current average of class by processing the avg list data 
total_avg = 0

for i in range(0, len(avg)):
    total_avg += avg[i] #adds each avg value to the total_avg variable

#calculate the average
class_avg = total_avg / len(avg)
print ("-----------------------------------------------------------------")
print(f"Current Class Average of {len(avg)} students is: {class_avg:.2f}")
print ("------------------------------------------------------------------")