# A certain set of segments with integer coordinates of the ends [Li, Ri] is given on the line. 
# Choose from the given set the subset of segments that completely covers the segment [0, M], (M is a natural number), containing the smallest number of segments.
# The first line contains the constant M (1 ≤ M ≤ 5000). 
# Each subsequent line contains a pair of numbers Li and Ri (Li, Ri ≤ 50000), specifying the coordinates of the left and right ends of the segments. 
# The list is terminated with a pair of zeros. The total number of segments does not exceed 100,000.
# In the first line of the output file print the minimum number of segments required to cover the segment [0; M]. 
# Next, print the list of the covering subset, sorted in ascending order of the coordinates of the left endpoints of the segments. 
# The list of segments is displayed in the same format as in the input. The trailing two zeros do not need to be printed. 
# If the covering of the segment [0, M] by the original set of segments [Li, Ri] is impossible, then the only phrase “No solution” should be deduced.

m = int(input())  # input ending of segment [0, M]
s = []  # create list of segments' coordinates
l, r = map(int, input().split())
# input segments till both of elements are equal 0
while l != 0 or r != 0:
    if l < m and r > 0:
        s.append((l, r))  # beginning and ending of segment create tuple
    l, r = map(int, input().split())
s = sorted(s, key=lambda x: (x[0], -x[1]))  # sort the list by beginning points, if there are equal the list is sorted by ending points in reverse order
ending = 0  # cover source segment, taking point as 0
max_border = 0  # maximum ending for covering segment
segments = []  # create list for segments combination
n = []  # this list stores
# cover the segment by segments
while ending < m and len(s) > 0:
    # if covering point is on current segment it may be as covering segment
    if s[0][0] <= ending <= s[0][1]:
        if s[0][1] > max_border:
            n.clear()
            n.append(s[0])  # current segment is added to intermediate list 
            max_border = s[0][1]  # current border of covering is shifted to the end of the current segment
        s.pop(0)
    # all segments lefter source segment are removed
    # if current segment are lefter than current border of covering it is removed too
    elif s[0][0] <= max_border and s[0][1] <= max_border:
        s.pop(0)
    # if current segment begins righter than current border of covering check if there is combination
    elif len(n) != 0:
        segments.append(n[0])  # add all means of intermediate list to list for segments combination (segments)
        n.clear()  # clear intermediate list after adding
        ending = max_border  # ending covering point is shifted to current maximum border
    # if there are no segments to combine source segment there are hole zones
    else:
        segments.clear()  # delete all segments. There are no segments to combine source segment
        break
if len(s) == 0:
    if len(n) > 0:
        segments.append(n[0])  # add all elements of intermediate list to list for segments combination
        ending = max_border  # take current border for combination and compare it with ending point M
# if border is lefter than M there are no combinations
if ending < m:
    segments.clear()
if len(segments) == 0:
    print('No solution')
else:
    print(len(segments))
    for k in segments:
        print(k[0], k[1])
