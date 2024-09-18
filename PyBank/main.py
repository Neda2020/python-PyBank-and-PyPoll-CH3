import pandas as pd
import os

# Path to collect data from the Resources folder
file_path = r'D:\AssignmentsUOFT\python-PyBank-and-PyPoll-CH3\PyBank\Resources\budget_data.csv'

# Load the budget_data.csv file using the correct file path
budget_data = pd.read_csv(file_path)

# Total number of months
total_months = budget_data['Date'].nunique()

# Net total amount of "Profit/Losses" over the entire period
net_total = budget_data['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" and the average of those changes
budget_data['Change'] = budget_data['Profit/Losses'].diff()
average_change = budget_data['Change'].mean()

# Greatest increase in profits (date and amount)
greatest_increase = budget_data.loc[budget_data['Change'].idxmax()]
greatest_increase_date = greatest_increase['Date']
greatest_increase_value = greatest_increase['Change']

# Greatest decrease in profits (date and amount)
greatest_decrease = budget_data.loc[budget_data['Change'].idxmin()]
greatest_decrease_date = greatest_decrease['Date']
greatest_decrease_value = greatest_decrease['Change']

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value:.2f})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value:.2f})")

# Optionally, export the results to a text file
with open("financial_analysis.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value:.2f})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value:.2f})\n")