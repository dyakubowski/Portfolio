# creating testing system for result
task_compl_code = int(input())  # input integer number from -128 to 127 inclusively
interactor = int(input())  # input integer number from 0 to 7 inclusively
checker = int(input())  # input integer number from 0 to 7 inclusively
if interactor == 0:
    if task_compl_code == 0:
        result = checker  # if interactor and program code is null, result is equal checker
    else:
        result = 3  # if interactor is null and program code is not null, result is equal 3
elif interactor == 1:  # if interactor is 1 result is equal checker
    result = checker
elif interactor == 4:  # if interactor = 4 and program code is null, result is equal 4
    if task_compl_code == 0:
        result = 4
    else:
        result = 3  # if program code is not null, result is equal 3
elif interactor == 6:
    result = 0  # if interactor = 6, result is equal 0
elif interactor == 7:
    result = 1 # if interactor = 7, result is equal 1
else:
    result = interactor  # if interactor is equal 2, 3 or 5, result is equal interactor (2, 3 or 5)
print(result)
