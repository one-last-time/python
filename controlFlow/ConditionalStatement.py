# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 9
guess = 9

if answer>guess:
    result = "Oops!  Your guess was too low."
elif answer<guess:
    result = "Oops!  Your guess was too high."
elif answer==guess:
    result = "Nice!  Your guess matched the answer!"

print(result)


# '''
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = "CA"
purchase_amount = 5

if state=="CA":
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state=="MN":
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state=="NY":
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)


#complex boolean expression

weight = 72
height = 1.8

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

is_raining = True
is_sunny = True

if is_raining and is_sunny:
    print("Is there a rainbow?")

unsubscribed = False
location ='USA'

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")

errors = 3
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")
