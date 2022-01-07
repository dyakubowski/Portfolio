# A string consisting of lowercase Latin letters was brought to the line repair shop. The customer wants to make a palindrome out of it. 
# In the workshop, they can replace an arbitrary letter in a string with any letter chosen by the customer for 1 Bytlandian tugrik.
# What is the minimum amount the customer will have to pay for line repair?
# Recall that a palindrome is a string that is equal to itself, read in the opposite direction.
# Print one integer - the minimum amount that the customer will have to pay for turning the string brought by the customer into a palindrome.

s = list(str(input()))
cost = 0
# create palindrom in the string
for i in range(len(s) // 2):
    # change the character in the second half of the string by the character in the first half
    if s[i] != s[-1 - i]:
        s[i] = s[-1 - i]
        cost += 1  # the cost of this change is 1
print(cost)
