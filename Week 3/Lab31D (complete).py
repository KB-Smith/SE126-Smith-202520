#Kyle Smith
#SE126.04
#Lab 3 1D
#1-27-2025

#Program Prompt:Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  
# Store the field data into respective 1D lists, and then process the lists to determine the 4 final output 
# values (make sure they are clearly labeled!). This final solution should have NO input() statements and when 
# the console is ran it should print all 4 totals (you may reprint the data from the lists/fie if you would like)  
# Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file 
# and store data into lists, then use a for loop to process each voter and their data to find the 4 totals.

#variable dictionary:
#not_eligible_to_register = not eligle to register
#eligible_to_vote_nt_reg = eligible to vote but not registered
#eligible_but_no_vote = eligible but didnt vote
#num_voters = number of voters
#total_records = total number of records
#id +voter id number
#age = how old the person is
#registered = whether someone registered or not
#vote = whether someone voted or not

#Imports
import csv

# Initialize variables
not_eligible_to_register = 0
eligible_to_vote_nt_reg = 0
eligible_but_no_vote = 0
num_voters = 0
total_records = 0

# Printing headers for the table of voter information
print("-----------------------------------------------------------")
print(f" {'ID#'} \t{'Age'}  {'Eligible to Vote'}   {'Did Vote'}\t ")
print("-----------------------------------------------------------") 

# Open the CSV file containing the voter data
with open ("text_files/voters_202040.csv") as csvfile:
    # Reading the CSV file
    file = csv.reader(csvfile)

    # Loop through each row in the CSV file
    for rec in file:
        total_records += 1  # Total record count

      
        id_number = rec[0]
        age = int(rec[1])  # Convert age to an integer
        registered = rec[2]
        vote = rec[3]

        
        if age < 18:
            not_eligible_to_register += 1

       
        if age >= 18 and registered != "Y":
            eligible_to_vote_nt_reg += 1

        
        if age >= 18 and registered == "Y" and vote != "Y":
            eligible_but_no_vote += 1

        
        if vote == "Y":
            num_voters += 1

        # Print the current record's details
        print(f"{rec[0]} \t{rec[1]}\t      {rec[2]} \t   {rec[3]}\t")

# Print summary
print("***********************************************************************************")
print(f"* Number of individuals not eligible to register: {not_eligible_to_register}\t\t\t\t  *")
print(f"* Number of individuals who are old enough to vote but have not registered: {eligible_to_vote_nt_reg}\t  *")
print(f"* Number of individuals who are eligible to vote but did not vote: {eligible_but_no_vote}\t\t  *")
print(f"* Number of individual who voted: {num_voters}\t\t\t\t\t\t  *")
print(f"* Number of records: {total_records}\t\t\t\t\t\t\t\t  *")
print("***********************************************************************************")
