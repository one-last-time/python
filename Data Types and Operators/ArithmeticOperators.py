#addtion,subtraction,multiplication,division,mod are same as other language

print(((1+2+3)*(4/2)-5)%3)

#power
#get 2^3
print(2**3)

#integer divison
#it rounds the result 
print(8//3)
print(-8//3)


"""

Quiz: Calculate

In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

    1.How many tiles are needed?
    2.You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?

"""

#1
total=(7*9)+(7*5)
print("total tiles need=",total)
#2

print("tiles remain =",(6*17)%total)


