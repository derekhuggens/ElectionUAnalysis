# Election_Analysis
## Project Overview
### 
A Colorado Board of Elections employee has given me the following tasks to complete the election board audit of a recent local congressional election.

  1. Calculate the total number of votes cast.
  2. Get a complete list of candidates who received votes.
  3. Calculate the total number of votes each candidate received.
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on popular vote.

In addition, I was tasked to:

  1. Calculate the voter turnout for each county.
  2. Calculate the percentage of votes from each county out of the total count.
  3. Calculate the county with the highest voter turnout.  
 
Finally, once the Python election script was run, it should output the election results in layman's format within a text file that is easily read and understood.
 
## Resources

### 
* Data Source: election_results.csv
* Software: Python 3.6.8, Visual Studio Code, 1.61.2
* Seth and Tom the election count employees.

## Election-Audit Results

### The analysis of the election-audit shows that:

* There were 369,711 total votes in the congressional election.
* For the precinct, the county vote breakdown is as follows:
  - Jefferson county: 10.5% of the votes totalling to 38,855
  - Denver county: 82.8% of the votes totalling to 306,055
  - Arapahoe county: 6.7% of the votes totalling to 24,801
* The county with the largest number of votes was Denver.
* The candidates were: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane.
* Charles Casper Stockham received 23.0% of the votes, or 85,213.
* Diana DeGette received 73.8% of the votes, or 272,892.
* Raymon Anthony Doane received 3.1% of the votes, or 11,606.

The winner of the election was candidate Diana Degette with a winning vote count of 272,892 and a winning percentage of 73.8%.

## Images

Below is the output of the PyPoll_Challenge.py script showing what will be output to the election_analysis.txt file.

![image](https://github.com/derekhuggens/Election_Analysis/blob/7c72f173b13e50a97fcb7cc66d2c0233b8c7799a/Resources/terminal_election_results.png)

Below is the election_analysis.txt file showing the election results in an easily understood format.

![image](https://github.com/derekhuggens/Election_Analysis/blob/9c5d338713c4ac820f1b6d5929d9131b5a3253ba/Resources/election_results.png)

## Future Election Proposal

### 
The election commission could license my script with minor modification for future elections. Keeping all variables, lists, and dictionaries the same we could simply load different .csv files into the path, for example, file_to_load = os.path.join("different_path", "different_csv.csv"), and execute the Python script to do the analysis for another election. The file_to_save = os.path.join("another_different_path", "different_election_analysis.txt") would be an example of a new output text file that could store the different, future election results. This of course would be dependent on future .csv files having the same column and row format as the original election_results.csv. In the event of tie vote counts, the script would have to be modified with new conditional logic and comparison operators as well as print statments stating there was a tie. At that point, the commission would need to issue a recount or go into session to determine another way to pick a winner.
