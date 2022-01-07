# Article 83 of the Law “On the Election of Deputies of the State Duma of the Federal Assembly of the Russian Federation” defines 
# the following algorithm for the proportional distribution of seats in parliament.
# It is necessary to distribute 450 seats among the parties that participated in the elections. 
# First, the sum of the votes cast for each party is calculated and the sum of the votes cast for all parties is calculated. 
# This amount is divided by 450, the result is a value called the "first electoral quotient" 
# (the meaning of the first electoral quotient is the number of votes that must be collected to get one seat in parliament).
# Further, each party receives as many seats in parliament, which is equal to the integer part of dividing the number of votes for this party by the first electoral quotient.
# If, after the first round of distribution of seats, the sum of the number of seats given to parties is less than 450, 
# then the remaining seats are transferred one by one party, 
# in descending order of the fractional part of the quotient from dividing the number of votes for this party by the first electoral quotient. 
# If for two parties these fractional parts are equal, then the priority is given to the party that received the largest number of votes.
# At the entrance to the program, a list of parties that participated in the elections is submitted. 
# Each line of the input file contains the name of the party (a line possibly containing spaces), then, separated by a space, 
# the number of votes received by this party is a number not exceeding 10^8.
# The program should display the names of all parties and the number of votes in parliament received by that party. 
# The names must be printed in the same order in which they appeared in the input data.

my_file = open("input.txt", "r")  # open the file with election's results
words = list()  # create the list to write the file's rows
for line in my_file:
    line = [' '.join(line.split()[:-1]), int(line.split()[-1])]  # reform lines by unification words (the party's name) besides the last word as it is the number
    words.append(line)  # add new rows to the list
my_file.close()  # close the file
s = sum(i[-1] for i in words)  # summarize all numbers in the list
d = {}  # create the dictionary where keys are party's name, values - list [the integer part of dividing the number of votes for this party by the first electoral quotient,
# the rest of dividing the number of votes for this party by the first electoral quotient]
for party in words:
    d[party[0]] = [450 * party[1] // s, party[1] % (s / 450)]
d1 = dict(sorted(d.items(), key=lambda key: (-key[1][1], -key[1][0])))  # sort the dictionary by the values' rest (the second element) in reverse order and by the values' count
# (the first element) in reverse order
i = 450 - sum(val[0] for val in d1.values())  # find parlament votes' count which not be distributed
if i <= len(d1):
    for val in list(d1.values())[:i]:
        val[0] += 1  # each vote are given each party in sorted order
else:
    for val in d1.values():
        val[0] += i // len(d1)  # each vote are given each party in sorted order while the rest is more than the parties' total count
    for val in list(d1.values())[:i % len(d1)]:
        val[0] += 1  # the rest votes are given in round while there are votes
for key, value in d.items():
    print(key, value[0])
