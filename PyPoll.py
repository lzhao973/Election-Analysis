# The data we need to retrieve.
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The winner of the election based on popular votes
import datetime
now=datetime.datetime.now()
print("The time right now is",now)
import os
import csv
file_to_load =os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    #for row in file_reader:
        #print(row)
    headers=next(file_reader)
    print(headers)
