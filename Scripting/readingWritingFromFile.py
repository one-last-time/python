f = open('sometxt.txt','r')
file_data=f.read()
f.close()
print(file_data)

f= open('sometxt.txt','w')
f.write('I am ediing this file')

f= open('sometxt.txt','r')
file_data=f.read()
f.close()
print(file_data)

#below sytax closr file autometically
with open('sometxt.txt','r') as f:
    file_data1=f.read()
print(file_data1)

with open('camelot.txt','r') as song:
    file_data1=song.read(2)
    print(file_data1)
    file_data1=song.read(8)
    print(file_data1)
    file_data1=song.read()
    print(file_data1)

print(file_data1)

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)


'''
You're going to create a list of the actors who appeared in the television programme Monty Python's Flying Circus.

Write a function called create_cast_list that takes a filename as input and returns a list of actors' names.
It will be run on the file flying_circus_cast.txt (this information was collected from imdb.com).
Each line of that file consists of an actor's name, a comma, and then some (messy) information about roles they played in the programme. 
You'll need to extract only the name and add it to a list.
You might use the .split() method to process each line.
'''
def castList(name):
    actorList=[]
    with open(name,'r') as f:
        for line in f:
            tmp=line.split(',')
            actorList.append(tmp[0])
    return actorList
res = castList('cast_list.txt')
print(res)
