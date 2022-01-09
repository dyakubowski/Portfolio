# In the village of Internetovka, all houses are located along one street on one side of it. 
# There is nothing on the other side of this street yet, but soon everything will be - schools, shops, cinemas, etc.
# To begin with, they decided to build a school in this village. 
# It was decided to choose the place for the construction of the school so that the total distance that students travel from their homes to the school was minimal.
# The plan of the village can be represented as a straight line, at some integer points of which there are pupils' houses. 
# It is also allowed to build a school only at an integer point of this straight line (it is also allowed to build a school at the point where one of the houses is located -
# after all, the school will be located on the other side of the street).
# Write a program that, using the known coordinates of the students' houses, will help determine the coordinates of the school's construction site.
# Print one integer - the coordinate of the point where it is best to build the school. If there are several answers, print any of them.

count_pupils = int(input()) # input the count of pupils in the school
house_number = list(map(int, input().split())) # input the coordinates (numbers) of pupils' houses
if count_pupils == 1:
  print(house_number[0]) # for one pupil the school will be located on the opposite side
elif count_pupils == 2:
  print((house_number[0] + house_number[1]) // 2) # for two pupil the school will be located on the medium between their houses
else:
  k = (count_pupils - 1) // 2 # for more pupils the school will be located on the opposite side of the medium pupil's house
  print(house_number[k])
