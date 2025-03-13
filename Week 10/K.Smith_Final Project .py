#Kyle Smith
#SE126.04
#Final Project
#2-24-2025

import csv

def seating_map():
   
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []

   
    seat_setup = [a, b, c, d, e, f]

    
    with open("text_files/final_plane.csv") as csvfile:
        file = csv.reader(csvfile)

       
        for rec in file:
            a.append(rec[0])
            b.append(rec[1])
            c.append(rec[2])
            d.append(rec[3])
            e.append(rec[4])
            f.append(rec[5])

    return seat_setup  

def show_seats(seat_setup):
    print("Seats Available:")
    for i in range(len(seat_setup[0])):  
        print(f"Row {i + 1:2}: {seat_setup[0][i]} {seat_setup[1][i]} {seat_setup[2][i]} {seat_setup[3][i]} {seat_setup[4][i]} {seat_setup[5][i]}")

def again():
    answer = input("Would you like to reserve another seat? [Y/N]: ").lower()
    return answer

def menu():
    print("~Welcome to Bahamas Air Flight 257~")
    print("\t1. Show All Seats")
    print("\t2. First Class")
    print("\t3. Business Class")
    print("\t4. Economy Class")
    print("\t5. EXIT")

    menu_choice = input("Enter your search type [1-5]: ")
    while menu_choice not in ["1", "2", "3", "4", "5"]:
        print("\t*** !INVALID ENTRY! ***")
        menu_choice = input("\tCHOOSE A NUMBER BETWEEN 1-5!!!: ")
    return menu_choice

def reserve_seat(seat_setup):
    answer = "y"
    while answer == "y":
        try:
            row = int(input("Enter the row you want to sit in: "))
            if row not in range(1, 25):  
                row = int(input("INVALID ENTRY!!! Please Choose A Row 1-24: "))
        except ValueError:
            row = int(input("Try Again ERROR!! Choose A ROWWW!! 1-24: "))

        index = row - 1

       
        try:
            seat = input(f"Enter the seat (A, B, C, D, E, F): ").upper()
            while seat not in ["A", "B", "C", "D", "E", "F"]:
                seat = input("INVALID ENTRY!!! Please Choose A Seat (A,B,C,D,E,F): ").upper()

        except ValueError:
            seat = input("PLEASE READ THE INSTRUCTIONS AND CHOOSE A SEAT (A, B, C, D, E, F)!!: ").upper()

       
        seat_columns = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
        seat_column = seat_columns[seat]

       
        if seat_setup[seat_column][index] != "X":
            seat_setup[seat_column][index] = "X"  
            print(f"Congratulations!!! Seat {seat}{row} has been successfully reserved!!")
        else:
            print(f"This seat is already taken. Please choose another seat.")

       
        show_seats(seat_setup)

        answer = again()

#initial variable
user_choice = 0
seat_setup = seating_map()  

while user_choice != "5":
    user_choice = menu()

    if user_choice == "1":  
        show_seats(seat_setup)

    elif user_choice == "2":  
        print("Seating Map for First Class:")
        for index in range(5):  
                print(f"Row {index + 1:2}: {seat_setup[0][index]} {seat_setup[1][index]} {seat_setup[2][index]} {seat_setup[3][index]} {seat_setup[4][index]} {seat_setup[5][index]}")

        reserve_seat(seat_setup)  

    elif user_choice == "3":  
        print("Seating Map for Business Class:")
        for index in range(5, 10): 
                print(f"Row {index + 1:2}: {seat_setup[0][index]} {seat_setup[1][index]} {seat_setup[2][index]} {seat_setup[3][index]} {seat_setup[4][index]} {seat_setup[5][index]}")

        reserve_seat(seat_setup)  

    elif user_choice == "4":  
            print("Seating Map for Economy Class:")
            for index in range(10, 24):  
                print(f"Row {index + 1:2}: {seat_setup[0][index]} {seat_setup[1][index]} {seat_setup[2][index]} {seat_setup[3][index]} {seat_setup[4][index]} {seat_setup[5][index]}")

            reserve_seat(seat_setup) 

    elif user_choice == "5": 
            print("\nThank you for flying with us! Have a safe trip!")

