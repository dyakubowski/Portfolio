# In the new academic year, students came to the computer classes at the Palace of Youth Creativity, which were divided into N groups. 
# There were Xi people in the i-th group. Immediately, the director faced a serious problem: how to distribute the groups to audiences. 
# The palace has M ≥ N classrooms, the j-th classroom has Yj computers. For classes, it is necessary that each student has a computer and another computer for the teacher. 
# It is prohibited to transfer computers from one classroom to another. Help the director!
# Write a program that finds the maximum number of groups that can be simultaneously distributed among classrooms, 
# so that all students in each group have enough computers, and at the same time there would be at least one more for the teacher.
# Print on the first line the number P - the number of groups that can be distributed among audiences. 
# On the second line print the distribution of groups by audiences - N numbers, 
# the i-th number must correspond to the number of the audience in which the i-th group should train. 
# (Both groups and audiences are numbered starting at 1). If the i-th group was left without an audience, the i-th number should be equal to 0. 
# If there are several admissible distributions, print any of them.

n, m = map(int, input().split())  # groups' and auditories' count respectively
students = list(map(int, input().split()))  # students groups
classrooms = list(map(int, input().split()))  # computers in classrooms
students = [(students[i], i) for i in range(len(students))]  # create tuples with group number
classrooms = [(classrooms[j], j) for j in range(len(classrooms))]  # create tuples with class number
s = sorted(students)  # sort list by group's size
c = sorted(classrooms)  # sort list by computer's count
distributions = [(s[stud][1], 0) for stud in range(len(s))]  # the smaller group the more chances to find classroom. 0 means the group without auditory
stud = 0  # index for student group
i = 0  # index for classroom
while stud < len(s) and i < len(c):
    if c[i][0] > s[stud][0]:
        distributions[stud] = (s[stud][1], c[i][1] + 1)  # if current classroom has computers more than current group size, instead 0 there is added classroom's number
        i += 1
        stud += 1
    else:
        i += 1  # else we run to next classroom
n = len([i for i in distributions if i[1] != 0])  # find count student groups with the classroom
print(n)
# print classrooms for each group in order
for k in sorted(distributions):
    print(k[1], end=' ')
