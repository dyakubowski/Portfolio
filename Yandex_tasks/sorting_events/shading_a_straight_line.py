# N segments were painted on the number line. The coordinates of the left and right ends of each segment (Li and Ri) are known. 
# Find the length of the colored part of the number line.
# The first line contains the number N, the next N lines contain the pairs Li and Ri. Li and Ri are integers, -10^9 ≤ Li ≤ Ri ≤ 10^9, 1 ≤ N ≤ 15 000
# Print one number - the length of the colored part of the straight line.

n = int(input())  # count of segments
segments = []  # list of points of segments' borders
for _ in range(n):
    l, r = map(int, input().split())  # input segments' borders
    segments.append((l, 'beginning'))  # create tuple (coordinate, 'beginning') for beginning segment
    segments.append((r, 'ending'))  # create tuple (coordinate, 'ending') for ending segment
segments.sort()  # sort the list by coordinates
segm_count = 0  # how many segments on this line 
painting_over = 0  # total painting area
for i in range(len(segments)):
    if segm_count > 0:
        painting_over += segments[i][0] - segments[i - 1][0]  # add painting segment to total area
    if segments[i][1] == 'beginning':
        segm_count += 1  # it begins current painting area
    else:
        segm_count -= 1  # it ends current painting area
print(painting_over)
