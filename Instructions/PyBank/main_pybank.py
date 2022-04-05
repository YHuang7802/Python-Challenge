# In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: "Date" and "Profit/Losses". 
# (Thankfully, your company has rather lax standards for accounting, so the records are simple.)
# Your task is to create a Python script that analyzes the records to calculate each of the following:
# * The total number of months included in the dataset
# * The net total amount of "Profit/Losses" over the entire period
# * The changes in "Profit/Losses" over the entire period, and then the average of those changes
# * The greatest increase in profits (date and amount) over the entire period
# * The greatest decrease in profits (date and amount) over the entire period

#step 1: read in csv X
#step 2: initialization to assign X
    #step 2.1: initialize dates_list, dates =[]X
    #step 2.2: initialize previous month at 0 X
    #step 2.3: initialize profit_loss_list =[] X

#step 3: go through loop: for row in csvreader: x
    #step 3.1: dates, pull the dates out of each row X
        #3.1.1: row[0]:row index position of 0. pulling the date from the 0 position X
        #3.1.2: append date to dates_listX

    #step 3.2: profit/loss, determine the change from month to month x
        #step 3.2.1: pull the profit/loss out of each row, row[1] X
        #step 3.2.2: subtract previous month from current month. initial value = 0 X
        #step 3.2.3: change previous month to current month x
        #step 3.2.4: append to profit_loss list x
#step 4: calculate average for changes x
    #step 4.1: import statistics module x
    #step 4.2: use statistics mean function x
    #step 4.3: set the dollar sign and set the decimal places to 2 places x
#step 5: calculate net total amount of "profit/losses"
    #step 5.1: pull out the profit/loss out of each row, row [1]
    #step 5.2: add up previous month to current month
    #step 5.3: append sum of profit_loss list 
#step 6: determing the max gain and max loss for profit/loss
    #step 6.1: create a new list max_loss =[]
    #step 6.2: append row[1] to max_loss list
    #step 6.3: use min and max function to identify the max gain and max loss
    #step 6.4: connext the max gain value to the date it's associated it
        #step 6.4.1: index the row [0] and row [1] to each other, to do it by hand: scroll down row [1] to find the max value then look at the corresponding date


# Modules
import os
import csv
import statistics

# initialize list to store data
dates = []
changes = []

#initialize variable
net_month = 0

#initialize dictonary
max_d ={"increase":{"date":"","change": 0}, "decrease":{"date":"","change":0}}
min_d ={}
# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# open csv 
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    
    # * The total number of months included in the dataset
    for row in csvreader:
        # Read the header row first (skip this part if there is no header)
        cur_month = int(row[1])
        # max_d[row[0]] = {'profit': row[1]}
        
        # len(dates) is only equal to 0 in on first row
        if len(dates) == 0:
            pre_month = cur_month
        
            change = 0

        if len(dates) > 0:

            change = int(cur_month) - int(pre_month)
        
            changes.append(change)
           
        pre_month = cur_month

        date = row[0]
        dates.append(date)
       
        # total amount of profit and loss
    
        net_month += int(row[1])

    # average change        
    avg_change = sum(changes) / len(changes)
    ans_avg_change= "{:.2f}".format(avg_change)
    ans_avg_change2 = f'{avg_change:.2f}'

with open ("Analysis/pybank_analysis.txt", "w") as file:
    print("Financial Analysis")
    file.write("Financial Analysis\n")
    print("--------------------------------")
    file.write("--------------------------------\n")
    total_months = len(dates)
    print(f"Total Months: {total_months}")
    file.write(f"Total Months: {total_months}\n")
    print(f"Total: ${net_month}")
    file.write(f"Total: ${net_month}\n")
    print(f"Average Change ${ans_avg_change2}")
    file.write(f"Average Change ${ans_avg_change2}\n")
    great_inc = dates[changes.index(max(changes))+1], max(changes)
    print(f'Greatest Increase in Profits: {great_inc}')
    file.write(f"Greatest Increase in Profits: {great_inc}\n")
    great_dec = dates[changes.index(min(changes))+1], min(changes)
    print(f'Greatest Decrease in Profits: {great_dec}\n')
    file.write(f"Greatest Decrease in Profits: {great_dec}\n")