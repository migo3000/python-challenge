import csv
import os

# Path to collect data from the Resources folder
input_file_path = os.path.join('Resources', 'budget_data.csv')
output_file_path = os.path.join('analysis', 'financial_analysis.txt')

# Initialize variables
total_months = 0
net_total = 0
monthly_changes = []
previous_profit_loss = 0
greatest_increase = ["", 0]  # Date and amount
greatest_decrease = ["", 0]  # Date and amount

# Read in the CSV file
with open(input_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row first
    header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # Count the total months
        total_months += 1

        # Update the net total amount of "Profit/Losses"
        current_profit_loss = int(row[1])
        net_total += current_profit_loss

        # Calculate changes in "Profit/Losses"
        if total_months > 1:
            change = current_profit_loss - previous_profit_loss
            monthly_changes.append(change)

            # Check for greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]

            # Check for greatest decrease in profits
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

        # Update previous profit/loss for next iteration
        previous_profit_loss = current_profit_loss

# Calculate average change
average_change = sum(monthly_changes) / len(monthly_changes)

# Generate output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
)

print(output)

# Export the results to a text file
with open(output_file_path, 'w') as textfile:
    textfile.write(output)
