# In the family tree, determine the least common ancestor of the two elements. 
# The smallest common ancestor of elements A and B is such that C is the ancestor of A, C is the ancestor of B, and the depth of C is the greatest possible. 
# In this case, the element is considered its own ancestor.
# The input data format is similar to the previous task.
# For each query, print the smallest common ancestor of these members.

with open('input.txt') as inp_f:
    n = int(inp_f.readline())  # the first line of this file is number
    generations = {}  # create dictionary where key is descendant, value is ancestor
    for i in range(n - 1):
        des, anc = inp_f.readline().strip().split()  # read next N-1 lines 
        generations[des] = anc  # these lines is transformed and added to the dictionary
    k = []  # create list of requests
    for line in inp_f.readlines():
        n1, n2 = line.strip().split()  # rest of lines is read
        k.append([n1, n2])  # rest of lines is added to the list
for i in k:
    ans1 = set()  # create set of ancestors
    n1, n2 = i[0], i[1]
    while n1 in generations:
        ans1.add(n1)  # this element add to the set, become as descendant and is found in the dictionary
        n1 = generations[n1]  # find ancestor for current descendant
    ans1.add(n1)  # this element add to the set
    # after ancestor's chain creation the second element is looked for in the dictionary
    while n2 not in ans1:
        n2 = generations[n2]  # this element become as descendant and is found in the dictionary
    print(n2)  # if current element is in the set it is the common ancestor
