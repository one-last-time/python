animal=["tiger","lion","dog","cat"]
#shows full list
print(animal)
#get size
print(len(animal))
#show an element
print(animal[0])

#show an element from last
print(animal[-4])
print(animal[-3])

#delete an element in list

del animal[2]
print(animal)
#sort
animal.sort()
print(animal)
#sort
animal.sort(reverse = True)
print(animal)

for x in animal:
    print(x)
 
