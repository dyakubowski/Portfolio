# Given text. Print all words in the text, one for each line. Words should be sorted in descending order of their number of occurrences in the text, 
# and with the same frequency of occurrence - in lexicographic order. Indication. After you create a dictionary of all words, 
# you will want to sort it by the frequency of occurrence of the word. You can achieve what you want if you create a list, 
# the elements of which will be tuples of two elements: the frequency of occurrence of the word and the word itself. 
# For example, [(2, 'hi'), (1, 'what'), (3, 'is')]. Then the standard sort will sort the list of tuples, with the tuples being compared on the first element, 
# and if they are equal, then on the second. This is almost what the task requires.
# Input text
# Print the answer to the problem

my_file = open("input.txt", "r")  # open the file
words = list()  # create list to write the file's rows
d = {}  # create the dictionary where keys are the text's word and values are word's count
for line in my_file:
    line = line.split()  # read lines in the file
    for word in line:
        if word not in d.keys():
            d[word] = 1  # if the word not in the dictionary add it
        else:
            d[word] += 1  # increase the word's count on 1
my_file.close()  # close the file after reading and forming dictionary
d = sorted(list(zip(d.values(), d.keys())), key=lambda word: (-word[0], word[1]))  # sort the dictionary by values in reverse order and in lexicographic order
for i in d:
    print(i[1])  # print words in the sorted dictionary
