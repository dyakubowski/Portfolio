# In the atrium of the new FNK building, urbanists have installed fashionable granite benches (which are cold to sit on in winter and hot in summer). 
# The shop is arranged as follows: several identical cubic granite blocks are placed in a row, and a granite slab is placed on them.
# In this case, the blocks are positioned so that the slab does not fall: 
# for this it is enough that both to the left and to the right of the center of the slab there is at least one granite block or part of it 
# (in particular, if the center of the slab falls in the middle of a block, then to the left and to the right of the center of the slab is part of the block, 
# and the slab does not fall).
# There are many singers at the FNK (but this is just the deductions for cheating on the O&MP course have not yet occurred) and they do not have enough chairs in the classrooms. 
# Students found that the blocks can be used as a seat in the classroom. You can pull out the blocks located at the edge (both left and right) one by one. 
# They want to pull out as many blocks as possible from under the bench so that it does not fall (you cannot move the remaining blocks). 
# Determine which blocks they should leave.
# The first line of the input contains two numbers: L - the length of the bench and K - the number of granite blocks-legs. Both numbers are natural and do not exceed 10,000.
# The second line contains K different non-negative integers specifying the position of each leg. 
# The position of the leg is determined by the distance from the left edge of the slab to the left edge of the leg (the leg is a 1 × 1 × 1 cube). 
# The legs are listed from left to right (that is, starting with the leg with a smaller distance to the left edge).
# It is required to list the legs that students need to leave. For each leg, you need to return its position as specified in the input data. 
# Legs should be listed from left to right, in the order in which they appear in the input.

l, k = map(int, input().split())  # input the length of the bench and the count of blocks
blocks = set(map(int, input().split()))  # coordinates of blocks
# the blocks which are situated the nearest to medium must not to be touched
list1 = [i for i in blocks if i <= (l-1) / 2]
list2 = [i for i in blocks if i >= (l-1) / 2]
a = max(list1)
b = min(list2)
# if the block is on medium of the bench this block is alone, else there are 2 blocks
if a != b:
  print(a, b)
else:
  print(a)
