x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []

for l,x,y,z in zip(labels,x_coord,y_coord,z_coord):
    tmp=l+" : "+str(x)+", "+str(y)+", "+str(z)
    points.append(tmp)


for point in points:
    print(point)



cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast ={}
for name, height in zip(cast_names,cast_heights):
    cast[name]=height
print(cast)



#unzip tuples

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

nm,ht = zip(*cast)

print(nm)
print(ht)


#Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

transpose = tuple(zip(*data))
print(transpose)


#Enumerate
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, char in enumerate(cast):
    cast[i]=cast[i]+" "+str(heights[i])


print(cast)