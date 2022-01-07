# An unknown driver committed an accident and fled the scene. The police are interviewing witnesses. Each of them says that he memorized some letters and numbers of the number. 
# But at the same time, the witnesses do not remember the order of these numbers and letters. The police want to check several suspected vehicles. 
# We will say that the number is consistent with the testimony of the witness if all the symbols that the witness named are present in this number (no matter how many times).
# First, a number is given - the number of witnesses. Then there are M lines, each of which describes the testimony of the next witness. 
# These lines are non-empty and contain no more than 20 characters. Each character in a line is either a digit or a capital Latin letter, and the characters can be repeated.
# Then comes the number - the number of numbers. The next lines are the numbers of the suspected cars and have the same format as the testimony of the witnesses.
# Write down the vehicle numbers that match the maximum number of witnesses. 
# If there are several such numbers, then output them in the same order in which they were given at the input.

n = int(input())
evidences = [str(input()) for i in range(n)]
m = int(input())
avto = [str(input()) for j in range(m)]
d = {}
# create dictionary where key is avto's number
# if witness' testimony is matched to avto's number the value of the avto's number is increased on 1
for i in evidences:
    for j in set(avto):
        if j not in d.keys():
            d[j] = 0
        if set(i).issubset(set(j)):
            d[j] += 1
d = dict(sorted(d.items(), key=lambda d: d[1], reverse=True))  # Sort the dictionary by values in reverse order
new_avto = [k for k in avto if d[k] == max(d.values())]  # highlight keys with maximal values and output them
for k in new_avto:
    print(k)
