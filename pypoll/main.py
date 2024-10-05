import csv
import os

# Define the file paths
input_file_path = r"C:\Users\jayne\OneDrive\Desktop\Class Homework\04_Challenge\Python-Challenge\pypoll\Resources\election_data.csv"
output_folder_path = r"C:\Users\jayne\OneDrive\Desktop\Class Homework\04_Challenge\Python-Challenge\pypoll\Analysis" 
output_file = os.path.join(output_folder_path, 'election_results.txt')

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the CSV file
with open(input_file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row
    
    # Count votes
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]  # Candidate's name
        
        # Count votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate percentages and find the winner
results = []
winner = ""
winning_count = 0

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Determine the winner
    if votes > winning_count:
        winning_count = votes
        winner = candidate

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results:
    print(result)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save results to the specified text file
with open(output_file, 'w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for result in results:
        txt_file.write(result + "\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")
