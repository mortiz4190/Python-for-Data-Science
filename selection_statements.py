# ISC2310 - Python for Data Analytics

#%%
print('''
SELECTION STATEMENTS...
''')
#%%
print('''
Let us start with the Boolean type variable... bool()
True or False...
1 or 0...
1 means True and 0 means False
Ok... so what?...
''')
# %%
print('''
Before I answer the 'so what?' question, let me demonstrate what I mean by 1 is 
True and 0 is False
--------------------------------------------------------
''')
'''
x = 1
print('x is: ', x)
print('x type is ', type(x))
print('convert x to boolean using the bool() function')
x = bool(x)
print('x is: ', x)
print('x type is ', type(x))
print('-----------------------------------------------------')
'''
#TODO: copy the above code and paste it below but change the value of x = 1 to x = 0 and see what happens
# Enter code below:
x = 0
print('x is: ', x)
print('x type is ', type(x))
print('convert x to boolean using the bool() function')
x = bool(x)
print('x is: ', x)
print('x type is ', type(x))
print('-----------------------------------------------------')
# %%
print('''
Ok, back to the 'so what?' question.
In programming there are statement we call 'conditional statements'
Ok. What is a conditional statement?
Simply "If A, then B" which means that B will only happen if A is True.
If today is Tuesday, then I have a class to teach...
If today is Sunday, then I sleep all day...
If your grade is greater than 70, then you pass
Ok. So how do you determine whether A is True or False
'A' must be a boolean expression... A statement that only gives a True or False 
answer (Boolean value).
''')
#%%
print('''
Let us talk about Relational Operators
-------------------------------------------------------------------------
>                   Greater than
<                   Less than
>=                  Greater than OR equal
<=                  Less than OR equal
==                  Equal to
!=                  NOT equal to
-------------------------------------------------------------------------
If today is Tuesday, then I go teach.
If today == Tuesday, then I go teach.
If your grade is greater than 70, then you pass.
if your grade > 70, then you pass.
''')
#%%
print('''
What about 'greater than / Less than' OR equal.
Notice the OR in between. It is called a logical operator (or boolean operator) 
along with AND.
AND Table
-------------------------------------------------------------------------
A                   B                   AND
-------------------------------------------------------------------------
True                True                True
True                False               False
False               True                False
False               False               False
-------------------------------------------------------------------------
OR Table
-------------------------------------------------------------------------
A                   B                   OR
-------------------------------------------------------------------------
True                True                True
True                False               True
False               True                True
False               False               False
-------------------------------------------------------------------------
If today is Tuesday OR Thursday, then I go to work.
If today == Tuesday or Today == Thursday, then I go to work.
''')
#%%
#TODO: Write the following comment statements as code inside the print() function 
# and check their answers. First example is done for you...
# 2 > 5
print('2 > 5 is', 2 > 5)
# 9 < 11
print('9 < 11 is', 9 < 11)
# 7 >= 3
print('7 >= 3 is', 7 >= 3)
# 8 <= 8
print('8 <= 8 is', 8 <= 8)
# 10 != 12
print('10 != 12 is', 10 != 12)
# 6 == 3
print('6 == 3 is', 6 == 3)
# 4 > 2 and 7 != 9
print('4 > 2 and 7 != 9 is', 4 > 2 and 7 != 9)
# 3 > 1 and 9 == 9 and 1 > 2
print('3 > 1 and 9 == 9 and 1 > 2 is', 3 > 1 and 9 == 9 and 1 > 2)
# 2 > 3 or 5 > 1
print('2 > 3 or 5 > 1 is', 2 > 3 or 5 > 1)
# 3 > 1 or 5 == 5
print('3 > 1 or 5 == 5 is', 3 > 1 or 5 == 5)
# 3 > 1 or 10 != 8 or 9 < 2
print('3 > 1 or 10 != 8 or 9 < 2 is', 3 > 1 or 10 != 8 or 9 < 2)
# %%
print('''
Now we have all the pieces we need to understand selection statements
A selection statement is a statement where you allow the computer to test several 
conditions instead of just one.
If today == Tuesday or today == Thursday, then I go to Poly to teach Python
else if today == Monday or today == Wednesday or today == Friday, then I go and 
research disinformation
else I go into deep sleep.
''')
# %%
print('''
How to write a selection statement
start with 'if', then write a conditional statement, then end with a colon : and 
start a new line
example:
if today == 'Tuesday':
''')
#%%
print('''
In the next line, the code should be indented. VSCode will automatically do that 
for you. However, if it didn't, then you have to either indent it with a tab or 
spaces.
https://www.businessinsider.com/tabs-vs-spaces-from-silicon-valley-2016-5
https://www.youtube.com/watch?v=SsoOG6ZeyUI&t=1s
After you make sure you indent your code (with tab, ofcourse), then you write the 
statement to excute if the condition is met
if today == 'Tuesday' or today == 'Thursday':
    print('I go to work!!!')
''')
#%%
print('''
However, the code above is only one condition, so how do you make it a multi 
condition code.
Using the elif and else statements.
elif is used if we want to define another condition and else statement is used when
we would settle for any other condition no matter what it is.
if today == 'Tuesday' or today == 'Thursday':
    print('I go to work!!!')
elif today == 'Monday' or today == 'Wednesday' or today == 'Friday':
    print('I do research on disinformation)
else:
    print('I go to sleep')
''')
# %%
# Let us demonstrate with a real code...
grade = int(input('What grade you got? (Your parents ask)'))
if grade >= 90:
    print('Fabulous Job...')
elif grade >= 80 and grade < 90:
    print('Good job...')
else:
    print('These Grades are Terrible - Your parents shouting at me (JJ), your benevolent professor')
#https://darylcagle.com/2010/04/27/teachers-in-1960-and-2010-color/
# %%
# TODO: Write a code that tells the user their grade in letter according the following table
print('''
Grade in numbers                    Grade in Letters
----------------------------------------------------------------------------------
90% - 100%                          A
86% - 89%                           B+
83% - 85%                           B
80% - 82%                           B-
76% - 79%                           C+
73% - 75%                           C
70% - 72%                           C-
66% - 69%                           D+
63% - 65%                           D
60% - 62%                           D-
0%  - 59%                           F
----------------------------------------------------------------------------------
''')

# %%
grade = int(input('What grade you got? (Your parents ask)'))
if grade >= 90:
    print("A")
elif grade >= 86:
    print("B+")
elif grade >= 83:
    print("B")
elif grade >= 80:
    print("B-")
elif grade >= 76:
    print("C+")
elif grade >= 73:
    print("C")
elif grade >= 70:
    print("C-")
elif grade >= 66:
    print("D+")
elif grade >= 63:
    print("D")
elif grade >= 60:
    print("D-")
elif grade >= 0:
    print("F")
