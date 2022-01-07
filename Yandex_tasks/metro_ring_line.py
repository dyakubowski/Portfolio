n, i, j = map(int, input().split())  # input the count of stations, station number for enter and station number for exit respectively
a = abs(i - j) - 1  # the count of intermediate stations for running if running is clockwise
b = n - abs(i - j) - 1  # the count of intermediate stations for running if running is counterclock-wise
# choise the minimum of two results
if a < b:
  print(a)
else:
  print(b)
