array = set(int(i) for i in range(1, int(input()) + 1))  # August conceives number for guessing in array
quess_num = input()  # Beatrice is trying to guess numbertelling some of numbers
while quess_num != 'HELP':
  quess_num = set(int(j) for j in quess_num.split())  # Transform list of guessing numbers into set
  output = str(input())
  if output == 'NO':
    array.difference_update(quess_num) # if August says "NO" all of numbers, which Beatrice says, are excepted from array
                                    # It is achieved by using set's difference: all numbers in set 'array' and in set 'quess_num' are excepted from set 'array'
    quess_num = str(input())
  elif output == 'YES':
    array.intersection_update(quess_num) # if August says "YES" all of numbers, which Beatrice doesn't say, are excepted from array
                                        # all numbers in set 'array' but not in set 'quess_num' are excepted from set 'array'
    quess_num = str(input())
true_digit = sorted(list(array))  # Output rest number in order to increasing
for i in true_digit:
  print(i, end=' ')
