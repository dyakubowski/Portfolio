# You are given two lists of numbers, each containing up to 100,000 numbers. Count how many numbers are contained simultaneously in both the first list and the second. 
# Note. This problem in Python can be solved in one line.
# Two lists of numbers are entered. All numbers in each list are on a separate line.
# Print the answer to the problem.

# numbers can be contained in sets
rank_1 = set(map(int, input().split()))
rank_2 = set(map(int, input().split()))
# from the first set take each number and find it in the second set
# if this element is in both sets it is added to list
general_elements_count = len([i for i in rank_1 if i in rank_2])
print(general_elements_count)  # the length of the list is count of elements in the list
