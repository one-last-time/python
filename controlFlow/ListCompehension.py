cities =["dhaka","khulna","barisal"]
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())


#above code can be written in this way . its called list comprehention

capitalized_cities1 = [city.title() for city in cities]
print(capitalized_cities1)


#using condition

squares = [ x**2 for x in range(9) if x%2==0]
print(squares)

squares=[x**2 if x%2==0 else x+3 for x in range(9)]
print(squares)


#Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.

ans = [x*3 for x in range(1,21,1)]
print(ans)

#Use a list comprehension to create a list of names passed that only include those that scored at least 65.
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name in scores if scores[name]>=65]
print(passed)