# In the family tree, each person, except for the ancestor, has exactly one parent.
# Each element of the tree is associated with a non-negative integer called the height. The parent has a height of 0, any other element has a height 1 more than its parent.
# Given two elements in the tree. Determine if one of them is a descendant of the other.
# The program receives as input the number of elements in the family tree N. Then N − 1 lines follow, specifying the parent for each element of the tree, except for the ancestor. 
# Each line is of the form descendant_name parent_name. Further to the end of the file there are lines containing the names of two elements of the tree.
# For each such query, output one of three numbers: 1 if the first element is the ancestor of the second, 2 if the second is the ancestor of the first, 
# or 0 if none of them is the ancestor of the other.

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
    ans1 = set()  # create set for adding all ancestors
    n1, n2 = i[0], i[1]
    while n2 in generations:
        ans1.add(n2)  # the second element is ancestor
        n2 = generations[n2]  # this element becomes descendant and is looked for in the dictionary
    ans1.add(n2)
    if n1 in ans1:
        print(1)  # if the first element there is in the chain of ancestors it is the ancestor for the second
    else:
        # else check out it is descendant for the second 
        ans2 = set()
        n1, n2 = i[0], i[1]
        while n1 in generations:
            ans2.add(n1)  # the first element is ancestor
            n1 = generations[n1]  # this element becomes descendant and is looked for in the dictionary
        ans2.add(n1)
        if n2 in ans2:
            print(2)  # if the second element there is in the chain of ancestors it is the ancestor for the first
        else:
            print(0)  # these elements has no relativity
