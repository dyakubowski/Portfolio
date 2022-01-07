# The sequence consists of natural numbers and ends with the number 0. In total, no more than 10,000 numbers are entered (not counting the trailing number 0). 
# Determine how many elements of this sequence are equal to its largest element.
# Numbers following 0 do not need to be read.
# A sequence of integers is entered, ending with the number 0 (the number 0 itself is not included in the sequence).
# Print the answer to the problem

number = int(input()) # input natural number
max_num = number # this number is assigned as maximum
count = 1
while number != 0:
    number = int(input()) # if number = 0, the loop is broken
    # if the number is more than maximum, the number is assigned as maximum
    if number > max_num:
        max_num = number
        count = 1
    # if the number is equal to maximum, the number is maximum
    elif number == max_num:
        count += 1
print(count)
