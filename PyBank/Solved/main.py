# First import the modules
import os
import csv


csvpath = os.path.join("../","Resources", "budget_data.csv")
# How to print an output text to the analysis folder
file_to_output = os.path.join("../","Analysis","Financial_Analysis.txt")


# Read the csv module
with open(csvpath) as csvfile:

    # CSV reader specifies comma delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the two header rows first 
    next(csvreader)
    next(csvreader)

    # Identify the necessary lists. #

    months = []
    total_profit = []
    profit_change = []


    # Read each row of data after the header and count the number of months in the data
    for row in csvreader:
        months.append(row[0])
        
     # Calculate the net total amount of profit/losses over the entire period   
        total_profit.append(int(row[1]))

    # Calculate the changes in profit/losses over the entire period
    # Loop through to calculate the difference for each year. Add the differences up and then find the average.
    # Originally started with i and i + 1 but got an error message(list index out of range)-why?
       
    for i in range(1,len(total_profit)):
        profit_change.append(total_profit[i] - total_profit[i-1]) 
        profit_average = sum(profit_change)/len(profit_change)

    # Find the greatest increase in profits and the greatest decrease in profits. (Similar to the bonus in the VBA HW only easier iwth lists!)
    
        max_profit = max(profit_change)
        min_profit = min(profit_change)

     # Print out max and min with the corresponding date. Not sure how to do this. Keep getting the month before.
     # Use total_profit to get the month since the month matches up with the second value in the list due to subtraction.
     # If I use profit_change, I get the previous month from where the change occurred. 

        max_profit_month = str(months[total_profit.index(max(total_profit))])
        min_profit_month = str(months[total_profit.index(min(total_profit))])

    # Print out the Financial Analysis for the data. Figure out how to print the date with the last two.
#If using output, I do not need the print statement. output =() 

financial_analysis_output = (
    f"Financial Analysis\n"
    f"-----------------------------\n"
    f"Total Months:{len(months)}\n"
    f"Total Profit: ${sum(total_profit)}\n"
    f"Average Change: ${profit_average:.2f}\n"
    f"Greatest Increase in Profits: {max_profit_month} (${max_profit})\n"
    f"Greatest Decrease in Profits: {min_profit_month} (${min_profit})")

# Print the output to terminal
print(financial_analysis_output)


# Export the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(financial_analysis_output)






