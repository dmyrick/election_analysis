# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# 3.4.2 Open and Read Files

# Assign a variable for the file to load and the path.
import csv

file_to_load: str = 'Resources/election_results.csv'

# Direct - Completed.
# Open the election results and read the file
# Indirect
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
    print(election_data)

# 3.4.3 Write Files to Python
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file. - Completed
# Write three counties to the file. - Completed

# Initialize a total vote counter. -3.5.1
total_votes = 0

# Candidate Options - 3.5.2
candidate_options = []

# Declare the empty dictionary.- 3.5.3
candidate_votes = {}

# Winning Candidate and Winning Count Tracker - 3.5.5
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 3.4.4 Read Results
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # 3.5.(1-6) Get Total Votes/Candidates/Candidates Votes/Candidates Percentage of Votes/Winner
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count. [3.5.1]
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts. - 3.5.4

# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
