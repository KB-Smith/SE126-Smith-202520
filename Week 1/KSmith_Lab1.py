#Kyle Smith
#SE126.04
#Lab 1
#1-13-2025

#PROGRAM PROMPT:You will be writing one Python file for this project - it is a program that determines whether a
#meeting room is in violation of fire regulations regarding the maximum room capacity. The
#program will accept the maximum room capacity and the number of people attending the
#meeting. If the number of people is less than or equal to the maximum room capacity, the
#program announces that it is legal to hold the meeting and tells how many additional people may
#legally attend. If the number of people exceeds the maximum room capacity, the program
#announces that the meeting cannot be held as planned due to the fire regulation and tells how
#many people must be excluded in order to meet the fire regulations. The user should be allowed
#to enter and check as many rooms as they would like without exiting the program.

#VARIABLE DICTIONARY
#max_cap: Total number of people the meeting can hold
#people: Number of people attending 
#response: Input from user about whether they have another meeting 
#remaining_sp: Space that's left in the meeting
#meeting_name: Name of meeting
#answer: Loop Control


def difference(people, max_cap):
    #Calculate the difference between max capacity and number of people attending
    diff = max_cap - people
    return diff

def decision():
    #Asking the user if they want to set up another meeting
    response = input("Would you like to set up another meeting? [y/n]: ").lower()
    while response != "y" and response != "n":
        print("***INVALID ENTRY***")
        response = input("\t\t Please Enter Y or N!!!").lower()
    return response

#------Main Code------

answer = "y"

while answer == 'y':
      
    meeting_name = input("Enter the name of your meeting: ")

    #Get the maximum capacity and the number of people attending
    max_cap = int(input("How many people are allowed into this meeting?: "))
    people = int(input("How many people will be attending this meeting?: "))

    #Calculate the difference in space
    remaining_sp = difference(people, max_cap)

    #Checks if the meeting is legal or illegal
    if people <= max_cap:
            print(f"There are {people} people signed up for this meeting. {remaining_sp*-1} is the number of space left in the meeting room. This meeting is LEGAL and fits within fire regulations!")
            print ("Have a good meeting!!")
    else:
            print(f"There are too many people in this meeting and it is now ILLEGAL according to fire regulations. \nRemove {remaining_sp*-1} or you and your associates will soon be riding in a cop car together!!")


    #Display Meeting Information
    print("")
    print("********************")
    print(f"Meeting Name:{meeting_name} ")
    print(f"There will be {people} people in attendance.")
    print("********************")


    #Ask if the user wants to set up another meeting
    answer = decision()


print("\nThank you for using the NEIT Fire Safety Service Tool!! Later!! ")