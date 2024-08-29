#Import the CSV file
import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)
   
    #Skip the header
    header = next(csvreader)

    #Store the values
    votes = []
    candidates = set()
    candidate_votes = []

    #Iterate through the rows
    for row in csvreader:
        votes.append(row[0])
        candidates.add(row[2])
        candidate_votes.append(row[2])

#Get the total votes
total_votes = len(votes)

print("""Election Results
--------------------------""")
print(f'Total Votes: {total_votes}')
print("--------------------------")

#Get the candidate vote counts and max number of votes
candidate_counts = {value: candidate_votes.count(value) for value in candidates}
max_votes = max(candidate_counts.values())

#Detemine the vote counts per candidate
for candidate in candidates:
    vote_count = candidate_votes.count(candidate)
    percentage_votes = (vote_count/total_votes)* 100
    print(f'{candidate}: {percentage_votes:.3f}% ({vote_count})')
    
    #Find the candidate with the max votes
    if vote_count == max_votes:
        winner = candidate

print("--------------------------")
print(f'Winner: {winner}')
print("--------------------------")

#Write results to a text file
output_path = os.path.join('analysis','results.txt')

with open(output_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    #Write the contents
    writer.writerow(["Election Results"])
    writer.writerow(["--------------------------"])
    writer.writerow([f'Total Votes: {total_votes}'])
    writer.writerow(["--------------------------"])
    
    for candidate in candidates:
        vote_count = candidate_votes.count(candidate)
        percentage_votes = (vote_count/total_votes)* 100
        writer.writerow([f'{candidate}: {percentage_votes:.3f}% ({vote_count})'])
        
    writer.writerow(["--------------------------"])
    writer.writerow([f'Winner: {winner}'])
    writer.writerow(["--------------------------"])
    
print(f'Results written to {output_path}')