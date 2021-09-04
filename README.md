# Election-Analysis
## Overview of Election Audit:
### The purpose of the election audit analysis
After we know who win the election and the winning count, we also want to know vote turnout for each county, the percentage of votes from each county, and the county with the highest turnout.
## Election-Audit Results:
* There were 369,711 votes in congressional election.
* From the image, we can see Jefferson: 10.5% (38,855)  Denver: 82.8% (306,055)  Arapahoe: 6.7% (24,801
* Denver had the largest number of votes.

                                        <img width="331" alt="Screen Shot 2021-09-04 at 3 43 33 PM" src="https://user-images.githubusercontent.com/88211298/132109672-40513dd2-da9a-45b3-b12f-850da002fd2d.png">

* Charles Casper Stockham: 23.0% (85,213)  Diana DeGette: 73.8% (272,892)  Raymon Anthony Doane: 3.1% (11,606)
* Diana DeGette won the election, she got 272,892 votes which has 73.8% of total votes. We use Python to find who won. Before we use if function to find the largest number of votes among three candidates, we should use for loop to count each candidate's votes in dictionary and then compare them by using if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            
                                        <img width="374" alt="Screen Shot 2021-09-04 at 3 44 31 PM" src="https://user-images.githubusercontent.com/88211298/132109678-961d9462-920e-4d95-8dd5-f6857564abf7.png">

## Election-Audit Summary:
First, we should read different csv file and find its directory. And then we need to change the os.join.path to load and save in different files and create a new txt file to write as well. Probably pay attention to the csv file and check the first row has the same categories as this code, if not, we have to change the row[] in the following csv file.
