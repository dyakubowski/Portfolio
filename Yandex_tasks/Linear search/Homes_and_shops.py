# 10 buildings were built in a row on Novy Prospekt. Each building can be either a residential building, a store, or an office building.
# But it turned out that residents of some houses on Novy Prospekt had to walk too far to the nearest store. 
# To develop a plan for the development of public transport on Novy Prospekt, 
# the mayor of the city asked you to find out what is the longest distance residents of Novy Prospekt have to cover in order to get from their house to the nearest store.
# The program receives ten numbers as input, separated by spaces. Each number specifies the type of building on New Avenue: 
# the number 1 stands for a residential building, the number 2 stands for a store, and the number 0 stands for an office building. 
# It is guaranteed that there is at least one residential building and at least one store on Novy Prospekt.
# Print one integer: the longest distance from the house to the nearest store. The distance between two neighboring houses is considered equal to 1 
# (that is, if two houses are next to each other, then the distance between them is 1, if there is another house between two houses, then the distance between them is 2, etc.)

street = list(map(int, input().split())) # input scheme of the street (0 is office, 1 is house, 2 is shop)
t = []
s = {i for i, l in enumerate(street) if l == 2}  # create set with indecies of shop
s2 = {i for i, l in enumerate(street) if l == 1}  # create set with indecies of home
for a in s2:
    k = []
    for b in s:
        k.append(abs(b-a))  # distance from house to shop
    t.append(min(k))  # choose the nearest shop to house
    k.clear()
print(max(t))  # choose the maximal distance to shop from this list
