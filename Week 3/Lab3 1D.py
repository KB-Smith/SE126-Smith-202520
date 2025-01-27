import csv

not_eligible_to_register = 0
eligible_to_vote_nt_reg = 0
eligible_but_no_vote = 0
num_voters = 0
total_records = 0

print("-----------------------------------------------------------")
print(f" {'ID#'} \t{'Age'}  {'Eligible to Vote'}   {'Did Vote'}\t ")
print("-----------------------------------------------------------") 

with open ("text_files/voters_202040.csv") as csvfile:
    file =csv.reader(csvfile)

    for rec in file:

        total_records +=1

        id_number =  rec[0]
        age = int (rec [1]) 
        registered = rec [2]
        vote = rec [3]

        if age < 18:
            not_eligible_to_register = not_eligible_to_register +1

        if age >= 18 and registered != "Y":
            eligible_to_vote_nt_reg = eligible_to_vote_nt_reg +1

        if age  >=18 and registered == "Y" and vote != "Y":
            eligible_but_no_vote = eligible_but_no_vote +1
        if vote == vote == "Y":
            num_voters = num_voters +1

        print(f"{rec[0]} \t{rec[1]}\t      {rec[2]} \t   {rec[3]}\t")

print("***********************************************************************************")
print(f"* Number of individuals not eligible to register: {not_eligible_to_register}\t\t\t\t  *")
print(f"* Number of individuals who are old enough to vote but have not registered: {eligible_to_vote_nt_reg}\t  *")
print(f"* Number of individuals who are eligible to vote but did not vote: {eligible_but_no_vote}\t\t  *")
print (f"* Number of individual who voted: {num_voters}\t\t\t\t\t\t  *")
print(f"* Number of records: {total_records}\t\t\t\t\t\t\t\t  *")
print("***********************************************************************************")


        