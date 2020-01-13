def my_range (n):
    x=0
    while x<n:
        yield x
        x+=1
print(my_range(4))

for x in my_range(4):
    print(x)

'''
Write your own generator function that works like the built-in function enumerate.

Calling the function like this:

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
should output:

Lesson 1: Why Python Programming
Lesson 2: Data Types and Operators
Lesson 3: Control Flow
Lesson 4: Functions
Lesson 5: Scripting
'''
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(lesson,start):
    for st in lesson:
        yield start,st
        start+=1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))