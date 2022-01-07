# As you know, the two most common date formats are European (first day, then month, then year) and American (first month, then day, then year). 
# The system administrator changed the date on one of the backups and now wants to return the date back. But he did not check what format the date is in the system. 
# Can he do without this information? In other words, you are given a record of some correct date. 
# It is required to find out whether the date is uniquely determined from this record even without additional information about the format.
# Print 1 if the date is uniquely determined, and 0 otherwise.
x, y, z = map(int, input().split())  # Input the first two variables as suggested day and month and the third variable as year respectively
# if x and y are not more than 12 the date can have either European or American format
if x <= 12 and y <= 12:
  if x == y:
    result = 1  # for example, 05.05.2021 means only the 5th May of 2021 in any format
  else:
    result = 0 
else:
  result = 1  # when one of these variables is more than 12 it means day unequivocally
print(result)
