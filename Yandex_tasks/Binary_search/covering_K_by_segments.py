# Given n points on a straight line, you need to cover them with k segments of the same length ℓ. Find the minimum ℓ.
# The first line contains n (1≤n≤10 ^ 5) and k (1≤k≤n). On the second n numbers xi (∣xi∣≤10^9).
# The minimum is ℓ such that the points can be covered by k segments of length ℓ.

n, k = map(int, input().split())  # input count of points and length segments
x = list(map(int, input().split()))  # input array of points
x.sort()  # sort array of points
left = 0
right = x[n - 1] - x[0]  # take right border for segment
while left < right:
    # binary search of segment's border
    l = (left + right) // 2  # medium is segment's border
    # take segments' count as 0
    cnt = 0
    maxright = x[0] - 1
    # let's draw segments in array
    for point in x:
        # each segment is compared to rest points
        if point > maxright:
            cnt += 1
            maxright = point + l
    # look if there are points outside segments
    if cnt <= k:
        right = l
    else:
        left = l + 1
print(left)
