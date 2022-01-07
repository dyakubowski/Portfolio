# This year Ivan finishes school and enters a university. During his studies, he often participated in computer science Olympiads and has accumulated many diplomas. 
# Ivan put diplomas into folders completely haphazardly, that is, any diploma could end up in any of the folders. Fortunately, 
# Ivan remembers how many diplomas are in each of the folders.
# Ivan wants to bring to the selection committee of the selected university a folder containing a diploma from the Moscow Olympiad in Programming 
# (Ivan has exactly one such diploma). In order to understand that this folder does not contain the required diploma, 
# Ivan needs to look through all the diplomas from this folder. 
# Viewing one diploma takes him exactly one second and he can instantly switch to viewing the next folder after finishing viewing the previous one. 
# Ivan can choose the order of viewing the folders.
# For a given number of diplomas in each of the folders, it is required to determine in what least time, in the worst case, 
# Ivan will understand which folder contains the diploma he needs.
# The first line of the input file contains an integer N (1 ≤ N ≤ 100) - the number of folders. 
# The second line contains N integers a1, a2, ..., aN (1 ≤ ai ≤ 100) - the number of diplomas in each of the folders.
# Print one number - the minimum number of seconds that Ivan needs in the worst case to determine which folder contains the diploma.

doc_case = int(input())
diploms = list(map(int, input().split()))  # folders this diplomas
total = sum(diploms)
diplom_amount = max(diploms)  # find the folder where there are the most diplomas
min_amount = total - diplom_amount  # this case is the minimum time for search in the worst case
print(min_amount)
