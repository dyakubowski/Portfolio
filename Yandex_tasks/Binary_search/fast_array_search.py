# An array of N integers is given. All numbers from -10 ^ 9 to 10 ^ 9. You need to be able to answer queries like "How many numbers have values from L to R?"
# Number N (1≤N≤10^5). Further N integers. Then the number of queries is K (1≤K≤10^5). Further, K pairs of numbers L, R (−10^9≤L≤R≤10^9) are the actual queries.
# Print K numbers - answers to queries

n = int(input())
array = list(map(int, input().split()))  # create array
array.sort()  # sort array to find all elements by request
count = int(input())
s = []  # list for answers for request
for _ in range(count):
    left, right = map(int, input().split())  # create borders of segment of the array
    first1 = -1
    last1 = len(array)
    # make binary search to find left border
    while first1 + 1 < last1:
        mid = (first1 + last1) // 2  # find medium to reduce the boundaries
        if left <= array[mid]:
            last1 = mid  # if left border in the left half right border is shifted to medium
        else:
            first1 = mid  # if left border in the right half left border is shifted to medium
    if first1 == -1:
        index0 = 0  # case where the left border is the first element of the array
    elif array[first1] == left:
        index0 = first1  # if the left border is element of the array this element is included in result
    else:
        index0 = first1 + 1  # else it is minimal element more than the border

    first2 = -1
    last2 = len(array)
    # make binary search to find right border
    while first2 + 1 < last2:
        mid = (first2 + last2) // 2  # find medium to reduce the boundaries
        if right < array[mid]:
            last2 = mid  # if right border in the left half right border is shifted to medium
        else:
            first2 = mid  # if right border in the right half left border is shifted to medium
    if last2 == len(array):
        index1 = last2  # case where the right border is the last element of the arra
    elif array[last2] == right:
        index1 = last2 + 1  # if the right border is element of the array border is shifted to right
    else:
        index1 = last2  # else this element is right border and not be included in segment
    res = index1 - index0  # substraction between right and left element is the result
    s.append(res)  # add result to list
print(*s)
