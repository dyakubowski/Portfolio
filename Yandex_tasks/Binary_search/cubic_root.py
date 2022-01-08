# A cubic equation ax3 + bx2 + cx + d = 0 (a ≠ 0) is given. It is known that this equation has exactly one root. It is required to find it.
# The input file contains four space-separated integers: -1000 <= a, b, c, d <= 1000
# Print the only root of the equation with an accuracy of at least 5 digits after the decimal point.

a, b, c, d = map(int, input().split())  # input coefficients to the equation
# Take root as meaning between -1 and 1
x1 = -1  
x2 = 1
# calculate the equation with these roots
y1 = a * x1 ** 3 + b * x1 ** 2 + c * x1 + d
y2 = a * x2 ** 3 + b * x2 ** 2 + c * x2 + d
while y1 * y2 >= 0:
    x1 *= 2  # find borders for root
    x2 *= 2
    y1 = a * x1 ** 3 + b * x1 ** 2 + c * x1 + d
    y2 = a * x2 ** 3 + b * x2 ** 2 + c * x2 + d
l = x1
r = x2
# monotony of function depends on coefficient a
# make binary search of root
if a > 0:
    # take accuracy of 5 digits after the decimal point
    while l + 0.00001 < r:
        med = (l + r) / 2
        y = a * med ** 3 + b * med ** 2 + c * med + d
        # if a > 0 branches are pointing up
        if y > 0:
            r = med
        else:
            l = med
    print(l)
else:
    # take accuracy of 5 digits after the decimal point
    while l + 0.00001 < r:
        med = (l + r) / 2
        y = a * med ** 3 + b * med ** 2 + c * med + d
        # if a < 0 branches are pointing down
        if y < 0:
            r = med
        else:
            l = med
    print(r)
