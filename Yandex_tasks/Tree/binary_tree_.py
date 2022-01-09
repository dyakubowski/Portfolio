# Write a program that will implement actions in a binary search tree "insert" and "find" (by value). The program should process requests of three types:
# ADD n - if the specified number is not yet in the tree, insert it and display the word "DONE", if it already exists, leave the tree as it was and display the word "ALREADY".
# SEARCH - the word "YES" (if the value was found in the tree) or the word "NO" (if not found) should be output. This does not change the tree.
# PRINTTREE - display the entire tree, always using the algorithm specified in the output format of the results.
# Each line of the input contains one of the ADD n or SEARCH n or PRINTTREE queries. It is guaranteed that PRINTTREE queries will only be called when the tree is not empty. 
# The total number of requests does not exceed 1000, of which no more than 20 PRINTTREE requests.
# For each request, print the answer to it. For ADD and SEARCH queries, the corresponding word is on a separate line. 
# A PRINTTREE request must display a tree, necessarily according to the following algorithm:
# 1) Print the left subtree
# 2) Output the number of points equal to the depth of the node
# 3) Output the key value
# 4) Print the right subtree

memory = []  # create tree of search
for_input = []  # create list of numbers for tree
# all elements are in the file
with open('input.txt') as inp_f:
    inp_f = inp_f.readlines()  # read all lines in the file
    for line in inp_f:
        for_input.append(line.strip().split())  # and add to the list

# the first element of line is command (ADD, SEARCH or PRINTTREE)
# the second element of line is number for tree
# create 3 functions which describe each of these commands
def add(root, x):
    """
    Input element to the tree
    :param root: the array to which the number needs to be added
    :param x: number needs to be added
    :return: message about being done or existing of this number in the tree
    """
    if not root:
        root.extend([None, x, None])  # if there isn't number in this branch it is added
        return 'DONE'  # operation is done
    key = root[1]  # go to the root of the tree or branch
    if x == key:
        return 'ALREADY'  # this number in the tree
    elif x < key:
        left = root[0]  # number less than root will be on the left
        if not left:
            root[0] = [None, x, None]  # this number become current root
            return 'DONE'  # operation is done
        return add(root[0], x)  # by recursion continue adding numbers
    elif x > key:
        right = root[2]  # number more than root will be on the right
        if not right:
            root[2] = [None, x, None]  # this number become current root
            return 'DONE'  # operation is done
        return add(root[2], x)  # by recursion continue adding numbers

def search(root, x):
    """
    Look for number on the tree to know this number exists here or no and give answer
    :param root: array of elements creating tree
    :param x: element which is being looked for
    :return: "YES" if this number exist on this tree, else "NO"
    """
    if not root:
        return 'NO'  # if there is no tree there isn't numbers here
    key = root[1]  # go to the root of the tree or branch
    if x == key:
        return 'YES'  # this element is root of branch and exists
    elif x < key:
        left = root[0]  # number less than root will be on the left
        if not left:
            return 'NO'  # if there is no branch there isn't numbers here
        return search(root[0], x)  # by recursion continue searching numbers
    elif x > key:
        right = root[2]  # number more than root will be on the right
        if not right:
            return 'NO'  # if there is no branch there isn't numbers here
        return search(root[2], x)  # by recursion continue searching numbers

def printtree(root, depth=0):
    """
    Image all elements of the array as a tree
    :param root: array which must be printed as tree
    :param depth: which branch (how far from root) will be imaged. By default, it will be root of tree
    :return: tree of these elements which describes links between numbers
    """
    if not root:
        return
    if root[0]:
        printtree(root[0], depth + 1)  # image current depth and get down on the left brunch
    print(f"{''.join('.' * depth)}{root[1]}")
    if root[2]:
        printtree(root[2], depth + 1)  # image current depth and get down on the right brunch

# run on each request with command and number in this array
for request in for_input:
    if request[0] == 'ADD':
        print(add(memory, int(request[1])))  # execute function for adding number
    elif request[0] == 'SEARCH':
        print(search(memory, int(request[1])))  # execute function for searching number
    else:
        printtree(memory)  # execute function for imaging tree
