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

# Modules
import os
import csv
import statistics

# initialize list to store data
dates = []
changes = []
max_gain =[]
max_loss =[]

#initialize variable

total_month = 0
net_month = 0

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")


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


# open csv 
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    # * The total number of months included in the dataset
    for row in csvreader:
        # Read the header row first (skip this part if there is no header)
        date = row[0]
        dates.append(date)
       

        # * The changes in "Profit/Losses" over the entire period, and then the average of those changes
        #how do I get current month minus previous month 
        # variables for current month, previous month and change between months
        # current month will be next iteration's previous month 
        # change = current month - previous month
        # initialize previous month as 0
        
        cur_month = int(row[1])
        
        if total_month > 0:

            change = int(cur_month) - int(pre_month)
        
            changes.append(change)

        pre_month = cur_month

        total_month += 1

        # total amount of profit and loss
    
        net_month += int(row[1])

        # * The greatest increase in profits (date and amount) over the entire period
        max_gain = max(changes)
        
        # * The greatest decrease in profits (date and amount) over the entire period
        
        

        
    avg_change = sum(changes) / len(changes)
    ans_avg_change= "{:.2f}".format(avg_change)

print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {len(dates)}")
print(f"total: ${net_month}")
print(f"Average Change ${ans_avg_change}")
print(f"Greatest Increase in Profits: {max_gain} ")
print(f"Greatest Decrease in Profits {max_loss}")
