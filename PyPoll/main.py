import os
import csv

file = os.path.join("..", "..", "PyPoll", "Resources", "election_data.csv")

#read the csvfile
with open(file, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#Initial value of total and winner votes set as 0. 
    totalVotes = 0
    winnerVotes= 0
#Candidate Votes and Percentage as lists {}
    candVotes = {}
    candPerc = {}
#Initiate Candidate and Winner of the election as strings ""
    cand = "" 
    winnerofElections= ""
# ----------------------------------------------------------------------------------
    for row in csvreader:
        cand = row[2]
        totalVotes = totalVotes + 1

        if cand in candVotes:

            candVotes[cand] = candVotes[cand] + 1

        else:

            candVotes[cand] = 1

    for i, j in candVotes.items():

        candPerc[i] = (j/totalVotes )*100
        
        if j >= winnerVotes:

            winnerofElections = i

            winnerVotes = j
# ----------------------------------------------------------------------------------
print(f"Election Results")

print(f"--------------------------------")  

print(f"Total Votes: {totalVotes}")

print(f"--------------------------------")   

for i,j in candVotes.items():

    print(f" ({i}): {round(candPerc[i],4)}% | {j}")

print(f"--------------------------------")  

print(f"Winner: {winnerofElections}")

print(f"--------------------------------")  

# ----------------------------------------------------------------------------------
outputfile = "output.txt"

with open(outputfile, "w") as textfile:

    textfile.write(f"Election Results\n")

    textfile.write(f"--------------------------------\n")

    textfile.write(f"Total Votes: {totalVotes}" +"\n")

    textfile.write(f"--------------------------------\n")

    for i,j in candVotes.items():
        textfile.write(f" ({i}): {round(candPerc[i],4)}% | {j}" + "\n")

    textfile.write(f"--------------------------------\n")
    
    textfile.write(f"Winner: {winnerofElections}" + "\n")

    textfile.write(f"--------------------------------" + "\n")

with open(outputfile, "r") as textfile:

    print(textfile.read())
    
    