# ISC2310 - Python for Data Analytics
'''
Quick review
'''
#%%
print('''write a for loop that print() the numbers from 0 to 10 and whether the number is even or odd.
Example:
'0 is even'
'1 is odd'
''')
# %%
# Answer here:
for x in range(0, 11):
    if (x % 2 == 0):
        print(x, "is even")
    else:
        print(x, "is odd")
# %%
print('''
NESTED LOOPS    
''')
# %%
for x in range(3):
    for y in range(0,2):
        for z in range(2):
            print('x:', x, '| y:', y, '| Hello' + str(z)) 
            
# %%
print('''
To better understand what goes on inside a nested loop, you need to debug.
So what is debugging? And how to debug?
''')
# %%
print('''
Press the 'Debug Cell' command on top of the code cell and trace the code with the 
'Step over' command.
''')
#%%
print('''
Can you write the above code using while loops and debug it?
''')
#%%
# Answer here:
x = 0
while x < 3:
    y = 5
    while y > 3:
        z = 0
        while z < 2:
            print('x:', x, '| y:', y, '| Hello' + str(z)) 
            z += 1
        y -= 1
    x += 1
# For while loop must declare your range explicitly, if you have an infinite loop it is becasue 
# I forgot to decrement or increment accordingly
# Use debug to TRACE loops as they iterate

# %%
print('''
Now that you got an idea how to write nested loops and how to debug your it, let us
do more examples.
''')
# %%
print('''
print() the following output using both for and while loops:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
''')
# %%
# Answer here - for loop:
for x in range(1,6):
    s = " " # Erases empty string
    for y in range(x): # iterates "x" times
        s += str(x) + " " 
    print(s) # breaks the loop after iterating "x" times
#Number of rows = Outer loop
#Number of columns = Inner loop
# %%
# Answer here - while loop:
# %%
print('''
print() the following output using both for and while loops:
x
x x
x x x
x x x x
x x x x x
x x x x
x x x
x x
x
''')
# %%
# Answer here - for loop
for x in range(9):
    s = " "
    if x >= 4:
        for y in range(9-x): # first iteration x = 5
            s += "x "
    else:
        for y in range(x+1):
            s += "x "
    print(s)

# %%
# Answer here - while loop
# %%
print('''
Checkerboard. This question is bloody hard... LOL
ONE NESTED FOR LOOP OR WHILE LOOP ONLY...
---------------------
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
''')
#%%
# Answer here:
for x in range(8):
    s = ''
    for y in range(8):
        s += str((x+y)%2) + ' '
    print(s)
# %%
print('''
Now you draw the board again using a while loop
''')
#%%
# Answer here
x = 0
while x < 8:
    s = ''
    y = 0
    while y < 8:
        s += str((x+y)%2) + ' '
        y += 1
    print(s)
    x += 1



# %%
