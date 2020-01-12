#Use a for loop to take a list and print each element of the list in its own line.

#Example:

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for i in range(len(sentence)):
    print(sentence[i])

#Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.

for i in range(1,31,1):
    if i%5==0:
        print(i)

# Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

#should create the list:
#usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

for i in range(len(names)):
    names[i]=names[i].replace(' ','_')

print(names)

#Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.

#You can assume that the list of strings will not contain empty strings.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for i in range(len(tokens)):
    tmp=tokens[i].find('<')

    if tmp>=0:
        count+=1

print(count)

#Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list. For example, if the list is items = ['first string', 'second string'], printing html_str should output:

#<ul>
#<li>first string</li>
#<li>second string</li>
#</ul>

items = ['first string', 'second string']
html_str = "<ul>\n"  

for st in items:
    
    html_str+=st
    html_str+='\n'

html_str+="</ul>"

print(html_str)



cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary

#if the key is in the list of fruits, add the value (number of fruits) to result

for fruit in fruits:
    result+=basket_items.get(fruit,0)


print(result)

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary

#if the key is in the list of fruits, add to fruit_count.

#if the key is not in the list, then add to the not_fruit_count

for fruit,value in basket_items.items():
    if fruit in fruits:
        fruit_count+=value
    else:
        not_fruit_count+=value


print(fruit_count, not_fruit_count)