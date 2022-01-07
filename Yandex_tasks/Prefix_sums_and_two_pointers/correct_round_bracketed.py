#  If you delete everything from a correct arithmetic expression except the parentheses, you get the correct parenthesis sequence. 
# Check if the entered string is a valid parenthesis sequence.
# A non-empty string is entered, consisting of open and close parentheses. String length does not exceed 100000
# Print YES if the entered string is a valid parenthesis sequence and NO otherwise

s = str(input())  # input string with brackets
n = 0  # let's think that '()' combination is 0
for i in range(len(s)):
    if s[i] == '(':
        n += 1  # '(' adds 1 to total
    if s[i] == ')':
        n -= 1  # ')' subtracts 1
    if n < 0:
        break  # ')' must not be at the begining. Only after '('
if n == 0:
    print('YES')  # 0 means '(' brackets and ')' brackets are the same in count
else:
    print('NO')
