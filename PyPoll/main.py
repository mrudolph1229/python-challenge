import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    total_votes = 0
    candidates = []
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    for row in csvreader:
        total_votes +=1
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li":
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1    
        k_perc = round(khan_votes/total_votes,2)
        c_perc = round(correy_votes/total_votes,2)
        l_perc = round(li_votes/total_votes,2)
        o_perc = round(otooley_votes/total_votes,2)

    winner_list = max([khan_votes, correy_votes, li_votes, otooley_votes])
    if winner_list == khan_votes:
        winner = "Khan"
    elif winner_list == correy_votes:
        winner = "Correy"
    elif winner_list == li_votes:
        winner = "Li"
    elif winner_list == otooley_votes:
        winnner = "O'Tooley"

    with open("Output.txt", "w") as text_file:
        text_file.write("ELECTION RESULTS\n")
        text_file.write("---------------------------------------\n")
        text_file.write(f'Total Votes: {total_votes}\n')
        text_file.write("---------------------------------------\n")
        text_file.write(f'{candidates[0]}- Votes: {khan_votes} Percentage: {k_perc}\n')
        text_file.write(f' {candidates[1]}- Votes: {correy_votes} Percentage: {c_perc}\n')
        text_file.write(f' {candidates[2]}- Votes: {li_votes} Percentage: {l_perc}\n')
        text_file.write(f' {candidates[3]}- Votes: {otooley_votes} Percentage: {o_perc}\n')
        text_file.write("---------------------------------------\n")
        text_file.write(f'The winner is {winner}!')

    print (f'ELECTION RESULTS\n\
---------------------------------------\n\
Total Votes: {total_votes}\n\
---------------------------------------\n\
{candidates[0]}- Votes: {khan_votes} Percentage: {k_perc}\n\
{candidates[1]}- Votes: {correy_votes} Percentage: {c_perc}\n\
{candidates[2]}- Votes: {li_votes} Percentage: {l_perc}\n\
{candidates[3]}- Votes: {otooley_votes} Percentage: {o_perc}\n\
---------------------------------------\n\
The winner is {winner}!')    

