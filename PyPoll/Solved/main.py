# First import the modules
import os
import csv

csvpath = os.path.join("../","Resources", "election_data_2.csv")

file_to_output = os.path.join("../","Analysis","Election_Results.txt")

# Read the csv module
with open(csvpath) as csvfile:

    # CSV reader specifies comma delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row first 
    next(csvreader)
    
    # Identify the necessary lists and initialize the vote count for each candidate.

    total_votes = []
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    candidates = ["Khan", "Correy","Li","O'Tooley" ]
    

    # Read each row of data after the header and count the number of votes in the data
    for row in csvreader:
        total_votes.append(row[2])

    # Count the votes that each candidate received.

        if row[2] == 'Khan':
            khan_votes = khan_votes + 1   
        elif row[2] =='Correy':
            correy_votes = correy_votes + 1   
        elif row[2] =='Li':
            li_votes = li_votes + 1   
        else: 
            otooley_votes = otooley_votes + 1

               
    # Calculate the percentage of votes for each candidate   
    khan_vote_percent = (khan_votes)/len(total_votes) 
    correy_vote_percent = (correy_votes)/len(total_votes)
    li_vote_percent = (li_votes)/len(total_votes)
    otooley_vote_percent = (otooley_votes)/len(total_votes)

#Identify the winner by comparing total votes.    

if (khan_votes > correy_votes and khan_votes > li_votes and khan_votes > otooley_votes):
    winner = "Khan"
elif (correy_votes > li_votes and correy_votes > otooley_votes and correy_votes > khan_votes):
    winner = "Correy"
elif (li_votes > khan_votes and li_votes > correy_votes and li_votes > otooley_votes):
    winner = "Li"
elif (otooley_votes > khan_votes and otooley_votes > li_votes and otooley_votes > correy_votes):
    winner = "O'Tooley"
else:
     winner = "A tie has occurred. We need a run-off election"



    # Print out analysis of election results.
election_results_output = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {len(total_votes)}\n"
    f"----------------------------\n"
    f"Khan: {(khan_vote_percent):.3%} {khan_votes}\n"
    f"Correy {(correy_vote_percent):.3%} {correy_votes}\n"
    f"Li {(li_vote_percent):.3%} {li_votes}\n"
    f"O'Tooley {(otooley_vote_percent):.3%} {otooley_votes}\n"
    f"-----------------------------\n"
    f"Winner: {(winner)}\n"
    f"-----------------------------")

# Print the output to terminal
print(election_results_output)


# Export the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(election_results_output)


    