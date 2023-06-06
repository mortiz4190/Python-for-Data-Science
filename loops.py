# ISC2310 - Python for Data Analytics
#%%
#Review
print('''
I want you to write a code where you ask the user for their birth month and based 
on that, you tell them whether they were born in the winter, spring, summer, or 
fall according to the following conditions
-------------------------------------
Months                  Semester
2, 3, 4                 Spring
5, 6, 7                 Summer
8, 9, 10                Fall
11, 12, 1               Winter
-------------------------------------
YOU ARE ONLY ALLOWED TO USE ONE 'AND' LOGICAL OPERATOR AND TWO 'OR' LOGICAL 
OPERATORS.
ALSO YOU ARE SUPPOSED TO CHECK WHETHER THE ENTERED MONTH IS A VALID ONE. (God... my
voice is gone...)
''')
#%%
# TODO: Answer here:
season = int(input('When is your birthmonth?: '))
if season == 1:
    print("Winter")
elif season <= 4:
    print("Spring")
elif season <= 7:
    print("Summer")
elif season <= 10:
    print("Fall")
elif (season <= 12):
    print("Winter")


#%%
'''
Nested IFs
placing one If inside another If or else statement
'''
#Example...
age = int(input('Please enter your age: '))
if age >= 18:
    drive = bool(input('Do you drive? (enter 1 for yes and 0 for no)'))
    if drive:
        print('Happy driving...')
    else:
        print('Time for you to get a driving license')
else:
    drink = bool(input('Do you drink milk? (enter 1 for yes and 0 for no'))
    if drink:
        print('Good. Milk is good for you.')
    else:
        print('Why you no drink milk? Milk is good for you.')
#%%
'''
LOOPS
'''
'''
Lets start with talking about the function range()
'''
#%%
range(5)
# What exactly happened?
# %%
'''
the range() function returns the sequence of the given number between the given 
range - I got this definition from Geeks for Geeks and it doesn't make any sense 
LOL
range() is used for generating a sequence of numbers. It takes a starting point and
ending point, and generates all the integers in between them. - much better 
definition
https://www.bitdegree.org/learn/python-range
My definition: It is a counter.
'''
# But why aren't the numbers inside the code I wrote up there displayed on my interactive shell?
# Well, we need to loop through that range() function and print() whatever number is contained within it
# %%
# Lets loop
# Starting with the 'for' keyword then followed by the condition. This section is  called the loop header. Don't forget to end it with the ':' character
# Then you define a variable that will take the value of the counter in that cycle
# after that you start a new line and you indent it (with tabs) where you write the loop body.
for x in range(5):
    print(x)
# %%
# Huh? why it starts at 0 and why it ends at 4? Where is 5?
# https://giphy.com/gifs/baby-crying-who-framed-roger-rabbit-2Qs2hKWMvEzdu
# But I want 5 to be counted and I hate 0.
# Sure...
for x in range(1, 6):
    print(x)
# %%
# TODO: Ok. What changed in the following loop?
for x in range(1, 6, 2):
    print(x)
#The increments have changed, now x is incrementing plus 2
# %%
# TODO: can you print() the even numbers from 0 to 10?
for x in range (0, 12, 2):
    print(x)
#%%
# But what exactly loops are used for other than printing numbers?
# Ok. Lets say you want to sum all the numbers between 0 and 100, how are you going to do that?
# We sum them one number at a time.
# Correct but that will take us a while.
# Can we do it in a loop
sum = 0 # We declare a variable called 'sum' to store the sum value while looping
for x in range(0, 100): # loop from 0 to 100. Is that correct? #TODO
    sum += x # augmented assignment
print(sum) # print() is out of the loop body only displays sum not iteratively

#%%
# TODO: What happens if we keep the print() function inside the loop body?
sum = 0
for x in range(0, 101):
    sum += x
    print(sum)
# It will print the sum after each iteration all the way until the sum is actualized
# %%
# TODO:
# Can you sum all the ODD numbers between 0 and 100?
oddSum = 0
for x in range(1, 101, 2):
    oddSum += x
print("The sum of all odd numbers between 0 and 100 is: ",oddSum)

#%%
'''
While loop...
----------------
Another way of looping...
an example is better than explaining it by words
'''
x = 0 # notice that we always define a variable before that will be part of the while conditional statement
while x < 10: 
    print(x)
    x += 1
#%%
#%%
# TODO: can you print() the even numbers from 0 to 10 using the while loop?
x = 0 
while x < 11:
    print(x)
    x += 2
#%%
# TODO: Ok. can you print() the odd numbers now? From 0 to 11?
x = 1
while x < 12:
    print(x)
    x += 2
#%%
'''
Nested loops...
--------------------
Annoying at first... Fun when you get it...
It is also annoying to explain...
Confusing...
Let me try and explain it to you as simple as possible
-------------------------------------------------------------------
I want to talk about tables
------------------------------------------
 |   1       2       3       4       5
-|----------------------------------------
1|   x       x       x       x       x
2|   x       x       x       x       x
3|   x       x       x       x       x
4|   x       x       x       x       x
5|   x       x       x       x       x
------------------------------------------
We have a 5x5 table filled with xs
We want to print() that table (Its contents (xs) without the columns and rows 
names) using loops.
'''
# using for loop
for x in range(5):
    for y in range(5):
        print('x')
# TODO: Is this correct?
#%%
# No it is not
# This is how we do it.
for x in range(5):
    s = ''
    for y in range(5):
        s += 'x '
    print(s)

# %%
# Ok. Now I want to stop being a benevolent professor and become a malevolent professor.
# https://www.youtube.com/watch?v=EmZa00hKwx4
# TODO: can you print() the whole table? Columns and Rows names, and the content inside?
s = '  '
for x in range(1, 6):
    s += str(x) + ' '
print(s)
for x in range(1,6):
    s = ''
    s += str(x) + ' '
    for y in range(5):
        s += 'x '
    print(s)

# %%
# # TODO: Can you print() the whole table again using a while loop?
# %%
# TODO: NOW DRAW THE MONA LISA USING NESTED FOR LOOPS:
# https://giphy.com/gifs/food-evil-laugh-spongebon-squarepants-lY1F6BJjbRO3m
# NVM
# %%
'''
That's all folks...
'''
# %%