# As you know, in the United States, the president is not elected by direct vote, but by a two-level vote. 
# First, elections are held in each state and the winner of the elections in that state is determined. 
# Then state elections are held: in these elections, each state has a certain number of votes - the number of electors from that state. 
# In practice, all state electors vote according to the results of intra-state voting, that is, states with a different number of votes vote in the final round of elections. 
# You know who each state voted for and how many votes were cast by that state. Summarize the results of the elections: 
# for each of the voting participants, determine the number of votes cast for him.
# Each line of the input file contains the name of the candidate for which the electors of that state are voting, 
# followed by the number of electors who voted for this candidate, separated by a space.
# Print the surnames of all candidates in lexicographic order, then, separated by a space, the number of votes cast for them.

my_file = open("input.txt", "r")  # open the file with results of elections
words = list()  # create list for record lines of the file to process
for line in my_file:
    words.append(line.split())  # read the file's lines
my_file.close()  # close the file
d = {}  # create the dictionary where key is the candidate's name, value - vote's count
for line in words:
    if line[0] not in d.keys():
        d[line[0]] = int(line[1])  # add candidate's name to the dictionary with value if the name not in the dictionary
    else:
        d[line[0]] += int(line[1])  # increase the vote's count for the candidate
d = dict(sorted(d.items()))  # sort the dictionary in lexicographic order
for key, value in d.items():
    print(key, value)  # print the result as "key, value"
