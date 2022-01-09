# On the straight line at points a1, a2,…, an (possibly coinciding) n kittens sit. The same line contains m segments [l1, r1], [l2, r2],…, [lm, rm]. 
# It is necessary for each segment to find out its fullness with kittens - how many kittens are sitting on the segment.
# The first line contains n and m (1≤n, m≤10^5). The second line contains n integers ai (0≤ai≤10^9). The next m lines contain pairs of integers li, ri (0≤li≤ri≤10^9).
# Print m integers. i-th number - fullness of kittens of the i-th segment.

n, m = map(int, input().split())  # kittens and segments respectively
kittens = list(map(int, input().split()))  # points where kittens sit
events = []  # create list which describes events on the straight on each point
lines = [[0, 0, 0]] * m  # list of segment, where there are indicated beginning, ending and quantity of kittens on the segment
for i in range(m):
    l, r = map(int, input().split())  # beginning and ending segment
    events.append((l, -1, i))  # '-1' is beginning
    events.append((r, 1, i))  # '1' is ending. i means segment's number  
    lines[i] = [l, r, 0]  # 'line' list has lists with beginning, ending and quantity of kittens on the segment
for kitty in kittens:
    events.append((kitty, 0, -1))  # '0' is kitten. '-1' instead of segment's number
events.sort()  # sort list by coordinates. 'Begin' is the first, then 'kitten'. 'End' in the ending
kitten_count = 0
for j in range(len(events)):
    if events[j][1] == -1:
        lines[events[j][2]][2] = kitten_count  # if segment begins it has current quantity of kittens
    elif events[j][1] == 1:
        lines[events[j][2]][2] = kitten_count - lines[events[j][2]][2]  # if segment ends let's get final count of kittens
    else:
        kitten_count += 1  # if '0', kitten's current quantity is increased on 1
for kittens in lines:
    print(kittens[2], end=' ')
