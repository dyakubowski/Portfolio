# The Huffman algorithm allows you to encode characters of the alphabet with a prefix-free code of various lengths, associating frequent characters with a shorter code, 
# and rare - a longer one. This algorithm is used in many data compression programs. The character code is determined according to the following rules:
# 1. Symbols of the input alphabet form a list of free nodes. Each sheet has a weight, 
# which can be equal to either the probability or the number of occurrences of the character in the compressed message.
# 2. Two free tree nodes with the least weights are selected.
# 3. Their parent is created with a weight equal to their total weight.
# 4. The parent is added to the free list, and its two children are removed from the free list.
# 5. Bit 1 is assigned to the right arc leaving the parent, bit 0 to the left one. 
# The bit values of the branches outgoing from the root do not depend on the weights of the descendants.
# 6. The steps starting from the second are repeated until only one free node remains in the free list. He will be considered the root of the tree.
# The binary code of a letter is all the numbers on the path from the root of the tree to the leaf corresponding to this letter.
# It is also important to efficiently compress the Huffman tree as economically as possible. Let's describe a deep traversal of this tree, 
# in which case we will first traverse the left subtree completely, then return to the node, and then traverse the right subtree. 
# Each time passing along the edge, we will write the letter L, R or U, depending on where we went along the edge 
# (L - to the left child, R - to the right child, U - to the parent). The tree given in the example will correspond to the line: LURLLURUURUU
# Such a string allows you to unambiguously reconstruct the tree and match the binary codes to all leaves of the tree. 
# However, the record can be modified by replacing edges of type L and R with edges of type D, which means that we descend into the child 
# (first to the left, and if the left is visited, to the right). Then the entry for our tree will look like this: DUDDDUDUUDUU
# This line is also unambiguously possible to restore the tree structure. It uses an alphabet of only two characters instead of three and can be encoded in fewer bits.
# This record can also be modified by replacing the meaning of the command U. 
# Now U will denote that we climb to the ancestor of the current vertex as long as we are the right child. 
# If during the ascent we came to the top from the left child, then we will immediately go to the right one. The entry for our tree will look like this: DUDDUU
# You need to use a record built according to these rules to define codes for all leaves in the order they are traversed.
# The first line of the input file contains the number N (1 ≤ N ≤ 100) - the number of lines. Each of the next N lines contains a description of tree traversal.
# The total number of characters in descriptions does not exceed 100,000.
# As an answer, print N blocks of codes for each of the lines of the input file. 
# Each block consists of the number of leaves K in this tree and of K lines containing numbers 0 and 1 and describing the code of each of the leaves.
# It is guaranteed that the size of the output does not exceed 2MB.

def maketree(serialized):
    """
    Create tree of source elements: root and 2 branches
    :param serialized: string of elements: 'D' and 'U'
    :return: dictionary where keys are 'left', 'right', 'type' or 'up' and values: elements, existence of root and
            type of element respectively
    """
    tree = {'left': None, 'right': None, 'up': None, 'type': 'root'}  # create root of tree
    nownode = tree  # this branch has root. By default, it is tree's root
    # run to source string
    for sym in serialized:
        # 'D' means we get down to left branch
        if sym == 'D':
            newnode = {'left': None, 'right': None, 'up': nownode, 'type': 'left'}  # create new branch
            nownode['left'] = newnode  # this branch is left from current root
            nownode = newnode  # get down to one depth
        # 'U' means we climb to the ancestor of the current vertex as long as we are the right child
        elif sym == 'U':
            while nownode['type'] == 'right':
                nownode = nownode['up']  # while we climb on the right we go to branch which is higher
            nownode = nownode['up']
            newnode = {'left': None, 'right': None, 'up': nownode, 'type': 'right'}  # create new branch
            nownode['right'] = newnode  # this branch is right from current root
            nownode = newnode  # get down to one depth
    return tree  # get dictionary which describes final tree

def traverse(root, prefix=[]):
    """
    Create combination of running to current element by branches (left or right)
    :param root: current branch or tree
    :param prefix: list storing branches from tree's top to current element
    :return: list of move's combination of each tree's element
    """
    if root['left'] is None and root['right'] is None:
        return [''.join(prefix)]  # if we reach to element image branches of way
    prefix.append('0')  # '0' - we go to left branch
    ans = traverse(root['left'], prefix)  # by recursion get down to branch and go to element
    prefix.pop()  # remove the last symbol if there are no branches for current element
    prefix.append('1')  # 'q' - we go to right branch
    ans.extend(traverse(root['right'], prefix))  # by recursion add to answer branches combination
    prefix.pop()  # remove the last symbol if there are no branches for current element
    return ans  # get list of branches combination for each element of the tree

# create two functions. The first function describes algorithm of tree making
# The second function
n = int(input())
blocks = []  # create list of branches combination for each element of created tree
for _ in range(n):
    tree_leafs = input()  # input elements for tree creation and branches combination
    # execute functions. Arguments for 'traverse' function is result of 'maketree' function
    blocks.append(traverse(maketree(tree_leafs)))  
# let's run to list 'blocks' and print result
for block in blocks:
    print(len(block))  # quantity of leafs is block's length
    for leaf in block:
        print(leaf)  # combination of branch for way from top to the leaf
