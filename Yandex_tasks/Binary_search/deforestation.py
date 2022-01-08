# Farmer Nikolai hired two lumberjacks, Dmitry and Fedor, to cut down the forest, in the place of which there should be a corn field. There are X trees in the forest.
# Dmitry cuts down A trees a day, but every K-th day he rests and does not cut down a single tree. Thus, Dmitry is resting on the K-th, 2K-th, 3K-th day, etc.
# Fedor chops down B trees a day, but every M day he rests and does not cut down a single tree. Thus, Fedor rests on M-th, 2M-th, 3M-th day, etc.
# Lumberjacks work in parallel and, thus, on days when none of them is resting, they cut down A + B trees, on days when only Fedor is resting - A trees, 
# and on days when only Dmitry is resting - B trees. On days when both loggers are resting, not a single tree is felled.
# Farmer Nikolai wants to understand how many days it will take lumberjacks to cut down all the trees, and he will be able to sow a corn field.
# It is required to write a program that, given the integers A, K, B, M and X, determines how many days it will take for all the trees in the forest to be cut down.
# The input file contains five space-separated integers: A, K, B, M and X (1 ≤ A, B ≤ 10 ^ 9, 2 ≤ K, M ≤ 10 ^ 18, 1 ≤ X ≤ 10 ^ 18)
# The output file must contain one integer - the required number of days.

a, k, b, m, x = map(int, input().split())  # input source data
l = 0
r = 2 * x // a + 1  # take case when Dmitriy works alone
while l < r:
    days = (l + r) // 2  # make binary search to find day when works will be made
    wd = days // k  # total days of Dmitriy's weekend
    wf = days // m  # total days of Fedor's weekend
    z = (days - wd) * a + (days - wf) * b  # total deforestation for days
    # if total deforestation less than necessary x, increase border l (total days)
    if z < x:
        l = days + 1
    # else right border is shifted to days
    else:
        r = days
print(l)
