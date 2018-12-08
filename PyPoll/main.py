import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    print(header)

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

    print (f'Votes: {total_votes}')
    print (f'{candidates[0]}- Total Votes: {khan_votes} Percentage: {k_perc}')
    print (f'{candidates[1]}- Total Votes: {correy_votes} Percentage: {c_perc}')
    print (f'{candidates[2]}- Total Votes: {li_votes} Percentage: {l_perc}')
    print (f'{candidates[3]}- Total Votes: {otooley_votes} Percentage: {o_perc}')

    