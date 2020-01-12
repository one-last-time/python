card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand)<25:
    hand.append(card_deck.pop())

print(card_deck)
print(hand)

number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

while current <= number :
    product*=current
    current+=1



# print the factorial of number
print(product)

#Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

#For example, if limit is 40, your code should set the nearest_square to 36.

limit =40
ans =1

while (ans+1)*(ans+1) <= limit:
    ans+=1
print(ans)