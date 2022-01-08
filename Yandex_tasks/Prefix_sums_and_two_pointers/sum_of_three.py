# Given three arrays of integers A, B, C and an integer S. Find i, j, k such that Ai + Bj + Ck = S.
# The first line contains the number S (1≤S≤10 ^ 9). The next three lines contain the description of arrays A, B, C in the same format: 
# the first number specifies the length n of the corresponding array (1≤n≤15000), then n integers from 1 to 10 ^ 9 are given - the array itself.
# If there are no such i, j, k, print a single number - 1. Otherwise, print three numbers on one line - i, j, k. 
# Array elements are numbered starting from zero. If there are several answers, print the lexicographically minimal one.

sum = int(input())
# make arrays to lists
massive_A = list(map(int, input().split()))
massive_B = list(map(int, input().split()))
massive_C = list(map(int, input().split()))
coordinates = []  # list of coordinates of arrays A, B, C respectively
massive_C = massive_C[1:]  # formulate array C
c = set(massive_C)  # remove duplicates from array C to speed up search
# take each element from array A and run to all elements of array B
for i in range(1, len(massive_A)):
    for j in range(1, len(massive_B)):
        # calculate element of array C subtracting elements A and B from sum
        if sum - massive_A[i] - massive_B[j] in c:
            coordinates.append((i - 1, j - 1, massive_C.index(sum - massive_A[i] - massive_B[j])))
            break
# if such elements absent in array C, to make sum is impossible (print '-1')
if coordinates == []:
    print(-1)
else:
    for point in coordinates[0]:
        print(point, end=' ')
