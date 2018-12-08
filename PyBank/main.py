import os
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

#Calc months and sum
    months = 0
    net_amount = 0
    max_change = 0
    min_change = 0
    for row in csvreader:
        months += 1
        net_amount += int(row[1])
        if int(row[1]) > max_change:
            max_change = int(row[1])
            max_month = row[0]
        if int(row[1]) < min_change:
            min_change = int(row[1])
            min_month = row[0]
    avg_change = round(net_amount / months,2)
    print ("Total Months: " + str(months))    
    print ("Total: $" + str(net_amount))
    print ("Average Change: $" + str(avg_change))
    print ("Greatest Increase in Profits: $" + str(max_change) +", in " + max_month)
    print ("Greatest Decrease in Profits: $" + str(min_change) +", in " + min_month)
