# In this problem you need to find the non-empty segment of the array with the maximum sum.
# The first line of the input contains a single number n (1≤n≤3⋅10 ^ 5) is the size of the array. The second line contains n integers ai (−10 ^ 9≤ai≤10 ^ 9) - the array itself.
# Print one number - the maximum sum on a segment in the given array.

n = int(input())  # input array's length
array = list(map(int, input().split()))  # create array
prefix = [0] * (len(array) + 1)  # create array with prefix sums
for i in range(1, len(array) + 1):
    prefix[i] = prefix[i - 1] + array[i - 1]  # input prefix sums by adding current element
    if prefix[i - 1] <= 0:
        prefix[i] = array[i - 1]  # if prefix sum is negative calculating begin with start
max_el = max(prefix[1:])  # the maximum from the array
print(max_el)
