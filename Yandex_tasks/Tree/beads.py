# Little boy makes beads. It has many numbered beads. Each bead has a unique number - an integer in the range from 1 to N. 
# He lays out all the beads on the floor and connects the beads to each other in an arbitrary way so that no closed shapes are formed. 
# In this case, each of the beads turns out to be connected to some other bead.
# It is required to determine what is the maximum number of series-connected beads present in the resulting figure.
# The first line contains the number of beads 1 ≤ N ≤ 2500. The next N-1 lines contain two integers - the numbers of the connected beads.
# Output one number - the required number of beads.

# use library sys
import sys
sys.setrecursionlimit(2500)  # the number of beads not more than 2500 - maximal depth of tree

def long_chain(top, neig, subsize, visited):
    """
    Create possible chains of beads and find the longest chain (its length)
    :param top: start of chain
    :param neig: list of linked beads
    :param subsize: how many beads linked with this one
    :param visited: this bead in the chain or not
    :return: length of the longest chain of beads
    """
    visited[top] = True  # the top bead in the chain
    chain = 1  # length of source chain is 1
    max1 = -1  # count beads which are linked to current bead
    max2 = -1  # count beads to which current bead is linked
    subsize[top] = 1  # top bead is linked with one bead
    # run to beads which are linked
    for next in neig[top]:
        if not visited[next]:
            chain = max(long_chain(next, neig, subsize, visited), chain)  # choose chain which longer. Use recursion
            # compare count of linked beads with current maximum
            if subsize[next] > max1:
                max2 = max1  # maximal count linked beads
                max1 = subsize[next]  # maximal count linking beads
            elif subsize[next] > max2:
                max2 = subsize[next]
    chain = max(chain, max1 + 1)  # find maximum chain
    chain = max(chain, max1 + max2 + 1)  # find maximum chain
    subsize[top] = max(subsize[top], max1 + 1)  # take this element count of linked beads
    return chain

n = int(input())
neig = []  # create list of linked beads
for i in range(n+1):
    neig.append([])  # create list of beads which are linked with bead
for i in range(n - 1):
    a, b = map(int, input().split())
    neig[a].append(b)  # create linked beads by adding elements to each of these lists
    neig[b].append(a)
subsize = [0] * (n + 1)  # list of quantity of linked beads
visited = [False] * (n + 1)  # list describes has this bead links or not
print(long_chain(1, neig, subsize, visited))
