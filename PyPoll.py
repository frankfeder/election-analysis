# os.chdir("Documents/Bootcamp/Repos/election-analysis")
#%%
# Packages
import os
import datetime as dt # current time: dt.datetime.now()
import csv

# File Paths
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Declare accumulators
total_votes = 0
candidate_options = []
candidate_votes = {}
candidate_pcts = {}
candidates_resultstxt = {}
winning_candidate = ""
winning_count = 0
winning_pct = 0.00

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)

    for row in file_reader:
        candidate_name = row[2]

        # Create votecount variable for each candidate
        if candidate_name not in candidate_options:
           candidate_options.append(candidate_name)
           candidate_votes[candidate_name] = 0

        # Total votes for each name and store in related votecount
        candidate_votes[candidate_name] += 1

        # Sum all votes to get total vote count
        total_votes += 1

# Print candidate names with percentage of total votes, and winner info
for candidate in candidate_options:
    candidate_pcts[candidate] = (candidate_votes[candidate] / total_votes) * 100
    print(f"{candidate} recieved {candidate_pcts[candidate]:.1f}% of the total vote")
    if candidate_votes[candidate] > winning_count:
        winning_candidate = candidate
        winning_count = candidate_votes[candidate]
        winning_pct = (candidate_votes[candidate] / total_votes) * 100
print(f"{winning_candidate} won, with {winning_count:,} votes cast for them ({winning_pct:.1f}% of the total vote)")

## Write output to new file
with open(file_to_save, "w") as outfile:
    # Create header with total and write to output file
    election_results = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------\n")
    print(election_results, end="")
    outfile.write(election_results)
    # Create text summaries per candidate and save to dictionaries
    for candidate in candidate_options:
        candidates_resultstxt[candidate] = (
            f"{candidate}: {candidate_pcts[candidate]:.1f}% ({candidate_votes[candidate]:,})\n" )
    # Iterate through candidate summaries text dicitonary and output to file
    for candidate in candidate_options:
        print(candidates_resultstxt[candidate])
        outfile.write(candidates_resultstxt[candidate])

# %%
