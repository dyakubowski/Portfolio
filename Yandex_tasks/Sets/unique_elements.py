# A list is given. Print those elements of it that appear in the list only once. Items should be displayed in the order in which they appear in the list.
# A list of numbers is entered. All numbers in the list are on one line
# Print the answer to the problem.

list_of_numbers = list(map(int, input().split()))
array_for_research = set(list_of_numbers)
unique_numbers = [unit for unit in array_for_research if list_of_numbers.count(unit) == 1]  # create list of elements, the count of them in array is equal to 1
for digit in unique_numbers:
    print(digit, end=' ')
