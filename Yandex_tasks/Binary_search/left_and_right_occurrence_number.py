# It is required to determine in the given array the number of the leftmost and rightmost element equal to the required number.
# The first line contains one natural number N, not exceeding 10^5: the number of numbers in the array. 
# The second line contains N natural numbers not exceeding 10^9, each next one is not less than the previous one. 
# The third line contains the number of required numbers M - a natural number not exceeding 10^6. The fourth line contains M natural numbers not exceeding 10^9.
# For each query, print on a separate line two numbers separated by a space: the number of the element of the leftmost and rightmost array elements, 
# which are equal to the query-number. The array elements are numbered starting from one. 
# If there is no such number in the array, print on the corresponding line two zeros separated by a space.

n = int(input())
array = list(map(int, input().split()))  # input n numbers for array
count = int(input())
numbers = list(map(int, input().split()))  # input numbers for search in the array
s = []  # create array of answers
for i in range(len(numbers)):
    first1 = 0  # take left border
    last1 = len(array) - 1  # and right border
    # make binary search of the element
    while first1 < last1:
        mid = (first1 + last1) // 2  # take medium of segment (array)
        if numbers[i] <= array[mid]:
            last1 = mid  # if the element is in the left half right border is shifted
        else:
            first1 = mid + 1  # if the element is in the right half left border is shifted
    if array[first1] == numbers[i]:
        first1 = first1 + 1  # left border must be at the earliest of elements equal the one
    else:
        first1 = 0  # if the element absents in the array print '0'

    first2 = 0
    last2 = len(array) - 1
    # make binary search of the element
    while first2 < last2:
        mid = (first2 + last2) // 2  # take medium of segment (array)
        if numbers[i] < array[mid]:
            last2 = mid - 1  # if the element is in the left half right border is shifted
        else:
            first2 = mid + 1  # if the element is in the right half left border is shifted
    if array[last2] == numbers[i]:
        last2 = last2 + 1  # right border must be at the latest of elements equal the one
    elif array[last2] > numbers[i]:
        # check the element left than one
        if array[last2 - 1] == numbers[i]:
            last2 = last2  
        else:
            last2 = 0  # if the element absents in the array print '0'
    else:
        # check the element left than one
        if array[last2 - 1] == numbers[i]:
            last2 = last2
        else:
            last2 = 0  # if the element absents in the array print '0'
    s.append((first1, last2))  # create tuple from left and right borders
for k in s:
    print(k[0], k[1])
