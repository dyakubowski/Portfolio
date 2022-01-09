# Vasya recently studied the polar coordinate system. Namely, he studied the concept of a polar rectangle. Let the standard Cartesian plane be given. 
# If you draw two circles on it with a center at the origin, then the area between them is called a ring (in the figure it is indicated in blue). 
# If you draw two rays on it, then the area swept out by the first ray when moving to the second is called an angle 
# (i.e. the area between these two rays is shown in green in the figure). A polar rectangle is the intersection of a certain angle with a certain ring (shown in red in the figure).
# Several polar rectangles are specified. Find the area of their intersection. Remember that the intersection of polar rectangles can have multiple parts!
# The first line contains an integer N - the number of rectangles (1 ≤ N ≤ 100,000). Next N lines contain the description of the rectangles. 
# Each rectangle is described by four real numbers r1, r2, φ1, φ2, where r1, r2 denote the radii of the circles forming the ring (r1 <r2), 
# and φ1, φ2 denote the angles formed by the first and second rays with the abscissa axis, given in radians. 
# In this case, the region from the first ray to the second is swept out in the counterclockwise direction (i.e., the angles increase), even in the case when φ1> φ2. 
# All numbers are specified with a maximum of six digits after the decimal point. The angles lie in the half-interval [0, 2π), and the radii do not exceed 106. 
# It is guaranteed that φ1 ≠ φ2.
# Print a single number - the area of the required intersection. The answer will be considered correct if its absolute or relative error does not exceed 10^-6

from math import pi  # use 'pi' from library 'math' 
rectangles = int(input())  # count of rectangles
events = []  # list of events: 'polar angle', 'begin'/'end', 'index of rectangle' - tuple
radius1 = []  # list of interior radiuses
radius2 = []  # list of external radiuses
for i in range(rectangles):
    r1, r2, u1, u2 = map(float, input().split())  # input interior radius, external radius, begining of polar sector, ending of polar sector
    events.append((u1, -1, i))  # beginning of sector has '-1'
    events.append((u2, 1, i))  # ending of sector has '1'
    radius1.append(r1)
    radius2.append(r2)
res = set()
count_n = 0
events.sort()
# go round rectangles to find quantity of rectangles at the beginning of round
for event in events:
    if event[1] == -1:
        count_n += 1
        res.add(event[2])
    elif event[2] in res:
        count_n -= 1
square = 0
# the area of the required intersection is situated between internal and external circles
# this intersection is made by maximal internal and minimal external circles
r1 = max(radius1)
r2 = min(radius2)
# go round rectangles repeatedly from beginning to find square
for event in range(len(events)):
    if events[event][1] == -1:
        count_n += 1
    else:
        count_n -= 1
    # at the sector rectangles must be as many as in the condition
    if count_n == rectangles:
        if event < len(events) - 1:
            square += (r2 ** 2 - r1 ** 2) * (events[event + 1][0] - events[event][0]) / 2
        else:
            square += (r2 ** 2 - r1 ** 2) * (2 * pi + events[0][0] - events[len(events) - 1][0]) / 2  # the last sector intersect '0'
print(square)
