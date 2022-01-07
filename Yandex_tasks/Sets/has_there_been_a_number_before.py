# The input line contains a sequence of numbers separated by spaces. For each number, print the word YES (on a separate line), 
# if this number has previously occurred in the sequence, or NO, if it has not.
# A list of numbers is entered. All numbers in the list are on one line.
# Print the answer to the problem.

array = list(map(int, input().split()))
set_of_numbers = set({})  # this set for numbers which are occurred in the sequence
chain = []  # create list of booling for numbers
for elem in array:
    if elem in set_of_numbers:
        chain.append('YES')
    else:
        set_of_numbers.add(elem)
        chain.append('NO')  # add element to the set if it are not occurred
for booling in chain:
    print(booling)
