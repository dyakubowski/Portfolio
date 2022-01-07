# In this task, you will need to answer the query "Find the sum of numbers on a segment in an array" many times.
# For each query, print on a separate line a single number - the sum on the corresponding segment.

n, q = map(int, input().split())  # array's length and requests' count
int_numbers = list(map(int, input().split()))  # array
prefixsum = [0] * (len(int_numbers) + 1)  # create list of prefix sums - sum is got by adding current element
for i in range(1, len(int_numbers) + 1):
    prefixsum[i] = prefixsum[i - 1] + int_numbers[i - 1]  # calculate prefix sums
resultsum = [0] * q  # create array of request's results
for i in range(q):
    l, r = map(int, input().split())  # indecies of array's segment
    resultsum[i] = prefixsum[r] - prefixsum[l-1]  # calculate prefix sum on current segment
for sum in resultsum:
    print(sum)
