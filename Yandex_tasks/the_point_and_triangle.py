# An isosceles right-angled triangle ABC with leg length d and point X are located on the coordinate plane. 
# The legs of the triangle lie on the coordinate axes, and the vertices are located at the points: A (0,0), B (d, 0), C (0, d).
# Write a program that determines the relative position of the X point and the triangle. If point X is located inside or on the sides of the triangle, output 0. 
# If the point is outside the triangle, output the number of the vertex closest to it.
# First, a natural number d (not exceeding 1000) is entered, and then the coordinates of the X point are two integers from the range from –1000 to 1000.
# If the point lies inside, on the side of the triangle, or coincides with one of the vertices, then output the number 0. 
# If the point lies outside the triangle, then output the number of the vertex of the triangle to which it is closest (1 - to the vertex A, 2 - to B, 3 - to C). 
# If the point is located at the same distance from two vertices, output the vertex whose number is less.

a = 1
b = 2
c = 3
cathetus = int(input())
point = list(map(int, input().split()))
if point[0] >= 0 and point[1] >= 0:
    if point[0] + point[1] <= cathetus:
        print(0) # the point is the inside the triangle
    # image the perpendicular from A to the hypotenuse
    # in the intersection point coordinates are equal
    elif point[1] <= point[0]:
        print(b) # if the abscissa coordinate is more the point is nearer to B
    else:
        print(c) # if the ordinate coordinate is more the point is nearer to C
elif point[0] < 0 and point[1] > cathetus / 2:
    print(c) # by the ordinate axis the point is nearer to C than A, when by abscissa axis the distance is the same (B is on the opposite side)
elif point[0] > cathetus / 2 and point[1] < 0:
    print(b) # by the abscissa axis the point is nearer to B than A, when by ordinate axis the distance is the same (C is on the opposite side)
else:
    print(a)
