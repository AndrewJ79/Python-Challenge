import csv
import os

# File path for the dataset
file_path = r"C:\Users\jayne\OneDrive\Desktop\Class Homework\04_Challenge\Python-Challenge\pybank\Resources\budget_data.csv"

# Specify the directory where you want to save the output file
output_directory = r"C:\Users\jayne\OneDrive\Desktop\Class Homework\04_Challenge\Python-Challenge\pybank\Analysis"
output_file_path = os.path.join(output_directory, "financial_analysis.txt")

# Initialize variables
total_months = 0
net_total = 0
changes = []
previous_profit = 0
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}
first_row = True

# Open the CSV file
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    
    # Iterate over each row in the CSV file
    for row in reader:
        date = row[0]
        profit = int(row[1])
        
        # Update the total number of months and the net total amount
        total_months += 1
        net_total += profit
        
        # Calculate the change in profit/loss from the previous month
        if not first_row:
            change = profit - previous_profit
            changes.append(change)
            
            # Check if the current change is the greatest increase or decrease
            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = date
                
            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = date
        else:
            first_row = False
            
        # Update the previous profit/loss for the next iteration
        previous_profit = profit

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else 0

# Create the result summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print the analysis to the terminal
print(output)

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Export the results to the specified text file
with open(output_file_path, mode='w') as file:
    file.write(output)
