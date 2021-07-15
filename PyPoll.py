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

# Direct - Tried and worked.
# Open the election results and read the file


# Indirect - HELP - Import cvs code caused error! Not needed.?.?
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
    print(election_data)

# 3.4.3 Write Files to Python - Final Examples
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file. - Completed
# Write three counties to the file. - Completed

# 3.4.4 Read Results
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
