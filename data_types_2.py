# ISC2310 - Python for Data Analytics
#%%
# Let us start with a review
# TODO: write a program that asks the user for their favorite color and number, and print the following message back to them.
# "You said that your favorite color is ", color, "and the square of your favorite number is " + number * number
# Write code below:

color = input("What is your favorite color?: ")
number = int(input("What is your favorite number?: "))
square = number * number
print("You said your favorite color is", color, "and the square of your favorite number is", square)
#%%
'''
Integers
---------
They are the positive and negative whole numbers including zero.
Floating-Point Number
----------------------
They are the real numbers. Consists of a whole number, a decimal point, and a 
fractional part.
'''
#%%
x = 5
type(x) # type() is a function that return the type of the variable
#%%
# TODO: What is the type of 0? Write a code to figure that out.
type(0)
# %%
x = 5.5
type(x)
# %%
x = .0
# TODO: What is the type of x? write a code to find out.
type(x)
# %%
# Some questions.
# Which data type would most appropriately be used to represent the following data?
# TODO: answer next to every question.
# The number of months in a year? int
# The area of a circle? float
# The current minimum wage? float
# The approximate age of the universe? float
# Your name? str
# %%
print(
'''
Arithmetic Operators
-----------------------------------------------------------------------------------
---------
Operator                    Meaning                 Syntax
-----------------------------------------------------------------------------------
---------
+                           Addition                x + y
-                           Subtraction             x - y
-                           Negation                -x
*                           Multiplication          x * y
/                           Division                x / y
**                          Exponentiation          x ** y
//                          Quotient                x // y
%                           Remainder of Modulus    x % y
-----------------------------------------------------------------------------------
---------
'''
)
# https://pemdas.info/
# %%
# TODO: What is the value of 5 + 3 * 2? Write a code to find out
print("The value of 5 + 3 * 2 is: " , (5+3*2))
# %%
# TODO: What is the value of (5 + 3) * 2? Write a code to find out
print("The value of (5 + 3) * 2 is: " , ((5+3)*2))
# %%
# TODO: What is the value of 6 % 2? Write a code to find out.
print("The value of 6 % 2 is: " , (6%2))
# %%
# TODO: What is the value of 2 * 3 ** 2? Write a code to find out.
print("The value of 2 * 3 ** 2 is: " , (2 * 3 ** 2))
# %%
# TODO: What is the value of -3 ** 2? Write a code to find out.
print("The value of -3 ** 2 is: " , (-3**2))
# %%
# TODO: What is the value of (3) ** 2? Write a code to find out.
print("The value of (3) ** 2 is: " , ((3)**2))
# %%
# TODO: What is the value of 2 ** 3 ** 2? Write a code to find out.
print("The value of 2 ** 3 ** 2 is: " , (2 ** 3 ** 2))
# %%
# TODO: What is the value of (2 ** 3) ** 2? Write a code to find out
print("The value of (2 ** 3) ** 2 is: " , ((2 ** 3)** 2))
# %%
# TODO: What is the value of 45 / 0? Write a code to find out
print("The value of 45 / 0 is: " , (45 / 0))
# Error division by 0
# %%
# TODO: What is the value of 45 % 0? Write a code to find out
print("The value of 45 % 0 is: " , (45 % 0))
# Error integer division or modulo division by 0
#%%
# TODO: What is the difference between / and // and %?
# What is the value of 43 / 5?
# What is the value of 43 // 5?
# What is the value of 43 % 5?
print("The value of 43 / 5 is: " , (45 / 5))
print("The value of 43 // 5 is: " , (43 // 5)) #Floor division given 43 apples and 5 eaters, how many
                                                # WHOLEE apples can be eaten
print("The value of 43 % 5 is: " , (45 % 5))
# %%
# Interesting example...
x = 5
x += 1 #adds 1 to x and then assigns x as such (6)
print(x)
#%%
# Does this work with other mathematical operators?
# It is called 'Augmented Assignment'
# TODO: Try augmented assignment with different operators
# %%
# TODO: What is the type of variable x in the following code?
x = 5
x += .0  #appends float value to integer
print(x)
type(x)
# Check the type of x using the appropriate function.
# %%
'''
Can we execute arithmetic operations on strings?
We already know that we can concatenate strings using the + sign.
Can we multiply strings?
Yes, but you have to multiply it with a number
'''
x = 'Hello'
y = 'o'
print(x + y) # concatenation of strings is possible
print(x * 5) # multiplication by an int
# %%
'''
Remember the int() function that we used before the input() function to convert the
user input from string to integer?
But what if we want to convert that input to float?
We use the float() function instead of 'int'
float(input('Enter circle radius: '))
'''
# TODO: Area of Trapezoid
# To calculate the area of a trapezoid, you need to ask the user for the the two bases (base_a and base_b), and the height of it.
# Then calculate the area of the trapezoid using teh following equation:
# (base_a + base_b) * height / 2
# Make sure you convert the input into float()
# https://www.omnicalculator.com/math/area-of-a-trapezoid
# Answer below:
base_A = float(input('Enter your first base "A": '))
base_B = float(input('Enter your second base "B": '))
height = float(input('Enter height of the trapezoid: '))
area = (((base_A + base_B) * height) /2)
print("The area of your trapezoid is: ", area)
#%%
'''
Booleans
--------
We will be using these type of variables in our next section of the course (Loops 
and Selection Statements)
Boolean is basically a True or False variable. 1 or 0.
'''
x = True
type (x)
#%%
y = False
type(y)

