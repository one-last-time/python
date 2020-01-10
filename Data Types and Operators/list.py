example = ['Jan','Feb','March',90,76.9]
print(example[0])
print(example[3])
print(example[4])
#last elemt
print(example[-1])
#ecnd from last
print(example[-2])


"""
Use list indexing to determine how many days are in a particular month based on the integer variable month, and store that value in the integer variable num_days. For example, if month is 8, num_days should be set to 31, since the eighth month, August, has 31 days.

Remember to account for zero-based indexing!

"""

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
month+=1
num_days=days_in_month[month]

print(num_days)


#Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
#print(eclipse_dates)

ans = eclipse_dates[-3:]
print(ans)


#in, not in
print(31 in days_in_month)
print(31 not in days_in_month)
print(32 in days_in_month)


#some methods

elements =["a","b","c","d","e"]
print(max(elements))
print(min(elements))
elements.append("a")
newStr=" hi ".join(elements)

elements=sorted(elements,reverse=False)
print(elements)
print(newStr)