#Kyle Smith
#SE126.04
#Lab 6
#2-24-2025

#PROGRAM PROMPT:Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane. Assume a
#small airplane with seat numbering as follows.The program should display the seat pattern, with an ‘X’ making the seats already assigned. For
#example, after seats 1A, 2B and 4C are taken the display should look like this:
#Row
# 1 X B C D
# 2 A X C D
# 3 A B C D
# 4 A B X D
# 5 A B C D
# 6 A B C D
# 7 A B C D
#After displaying the seats available, the program prompts for the seat desired, the user types in a seat
#and then the display of available seats is updated. This continues until all seats are filled or until the
#user signals that the program should end. If a user types in a seat that is already assigned, the
#program should say that the seat is occupied and ask for another choice.
#• You must use a function to display the seating map
#• You must use a function that asks the user in they want to continue reserving seats or stop.
#The function should only accept an uppercase or lowercase ‘y’ or ‘n’.

import csv

def seating_map():

    a = []
    b = []
    c = []
    d = []

    seat_setup = [a,b,c,d]

    with open ("text_files/plane.csv") as csvfile:
    # reading the CSV file
        file = csv.reader(csvfile)

        for rec in file:
            a.append(rec[0])
            b.append(rec[1])
            c.append(rec[2])
            d.append(rec[3])
    
    print("Row")
    for index in range(0,len(a)):
        print(f" {index+1}  {a[index]} {b[index]} {c[index]} {d[index]}")
 
    return a,b,c,d

def again():

    answer = input("Would you like to reserve another seat?[Y/N]: ").lower()
    return answer

    
seat_setup = seating_map()
  
answer = "y"

while answer == "y":

    
    

    row = int(input("Enter the row you want to sit in: "))    
        
    while row not in [1,2,3,4,5,6,7] :
            row = int (input("INVALID ENTRY!!! Please Choose A Row 1-7: "))

    index = row -1

    seat = input(f"Enter the seat (A, B, C, D): ").upper()

    
    if seat == "A":
        seat_column = 0
    elif seat == "B":
        seat_column = 1
    elif seat == "C":
        seat_column = 2
    else:
        seat_column = 3


    if seat_setup[seat_column][index] != "X":
        seat_setup[seat_column][index] = "X"  # this marks the seat as taken
        print(f"Congratulations!!! Your seat has been successfully reserved!")
    else:
        print(f"This seat is already taken. Please choose another seat.")


    print("\nSeats Available:") #updates map seating
    for i in range(len(seat_setup[0])):
        print(f"Row {i + 1}: {seat_setup[0][i]} {seat_setup[1][i]} {seat_setup[2][i]} {seat_setup[3][i]}")

    answer = again()

if answer == "n":
    print("\nThank you for flying with us! Have a safe trip!")
