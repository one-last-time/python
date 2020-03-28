import re

sentence ="Heello I am learning regex"
# . means any charachater and * means 0 or more count of that charcter
ans = re.match(r'.*',sentence)

# + means 1 or more count of that charcter
ans1 = re.match(r".+",sentence)


ans2 = re.match(r'[a-zA-Z]*',sentence)

ans3= re.match(r'[A-Z]e?',sentence)
print(ans)
print(ans1)
print(ans2)
print(ans3)

sentence1 = "7040 is my id"
# starts with a pattern 
# ^ means start
if  re.match(r'^70.*',sentence1):
    print('matched')
else:
    print("no match")

#end with
# $ means end
if re.search(r'id$',sentence1):
    print('matched')
else:
    print("no match")

#substitution

sentence2="I love ML ML"

ans4= re.sub(r'.ML','NLP',sentence2)
print(ans4)
ans4= re.sub(r'[a-z]','0',sentence2)
print(ans4)
ans4=re.sub(r'[a-z]','0',sentence2,flags=re.I)
print(ans4)
ans4=re.sub(r'[a-z]','0',sentence2,3,flags=re.I)
print(ans4)