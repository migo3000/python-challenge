import csv
import os

# Path to collect data from the Resources folder
input_file_path = os.path.join('Resources', 'election_data.csv')
output_file_path = os.path.join('analysis', 'election_results.txt')

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read in the CSV file
with open(input_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row first
    header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        # If candidate has other votes, add to their count
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Prepare the output with the results
output = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------"
]

# Calculate the percentage of votes each candidate won and print each candidate's voter count and percentage
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    output.append(f"{candidate}: {percentage:.3f}% ({votes})")

# Determine the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)
output.append("-------------------------")
output.append(f"Winner: {winner}")
output.append("-------------------------")

# Join the output into a single string
final_output = "\n".join(output)
print(final_output)

# Export the results to a text file
with open(output_file_path, 'w') as textfile:
    textfile.write(final_output)
