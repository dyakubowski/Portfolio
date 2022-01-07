# Tolya-Karp has requested n parcels from the Alligator Express for himself.
# The package is a box. There is an integer ai inside the box. The number on the box di indicates the color of the number inside.
# Tolya-Karp is interested in what the values of the numbers will be equal to if all those that have the same color are added together. 
# Please write a program that outputs the result.
# The first line contains one number n (0 ≤ n ≤ 2 * 105).
# The next n lines contain two numbers each: the color of the number in the box di and the value of the number ai (-1018 ≤ di, ai ≤ 1018).
# It is guaranteed that the sum of numbers of the same color does not exceed 1018.
# Print, in ascending order of the color number of a pair of numbers, each on a new line: the color number and the sum of all numbers of the given color.

n = int(input())
d = {}  # create dictionary to accumulate values of each color
for i in range(n):
    i = input().split()  # input indicates the color and values
    if int(i[0]) not in d.keys():
        d[int(i[0])] = int(i[1])  # add color as key to the dictionary with value
    else:
        d[int(i[0])] += int(i[1])  # add value if the color in the dictionary
d = dict(sorted(d.items()))  # sort the dictionary by keys (color's number)
for key, value in d.items():
    print(key, value)
