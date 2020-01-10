line = '"This line have both single quote \' and double quote "" "'
print(line)

length = len(line)
print(length)

#print ant index
print(line[4])



# TODO: Fix this string!
#ford_quote = 'Whether you think you can, or you think you can't--you're right.'

ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford_quote)



#some methods

name = 'shaffat nur dipu'

name= name.title()
print(name)

print("is it all lowercase ? ",name.islower())
print("is it all uppercase? ",name.isupper())

fish = 'One fish, two fish,three fish'
print('how many fish in the line?',fish.count('fish'))
print('find the index of \'fish\' in the fish string?',fish.find('fish'))

#split
new_str = "The cow jumped over the moon."
print(new_str.split())

print(new_str.split(' ',3))

print(new_str.split('.'))

print(new_str.split(None,3))