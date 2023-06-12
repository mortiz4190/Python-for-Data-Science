# ISC2310 - Python for Data Analytics
#%%
print('''
In the following dictionary, there are three keys and each key has a set as a 
value.
Create a for loop that loops through all the values in this dictionary and print 
each element in the values in similar fashion to the following example:
'hello is kon'nichiwa in Japanese and salve in Latin'
'''
languages = {'english': {'hello', 'excuse me', 'where is my food'},
    'japanese': {'kon\'nichiwa', 'sumimasen', 'watashi no tabemono wa dokodesu ka'},
    'latin' : {'salve', 'ignoscas', 'ubi est cibus'}}
)

# Is the order correct?
# What do you need to do?
#%%
#Review from last week
d = {}
d['english'] = 'hello' , 'excuse me', 'where is my food'
d['japanese'] = 'kon\'nichiwa', 'sumimasen', 'watashi no tabemono wa dokodesu ka'
d['latin'] = 'salve', 'ignoscas', 'ubi est cibus'

for i in d:
    print(i, d[i])



#%%
languages = {
    'english': {'hello', 'excuse me', 'where is my food'},
    'japanese': {'kon\'nichiwa', 'sumimasen', 'watashi no tabemono wa dokodesu ka'},
    'latin' : {'salve', 'ignoscas', 'ubi est cibus'}
}
for x, y, z in zip(languages['english'], languages['japanese'], languages['latin']):
    print(x, "is", y , "in Japanese and ", z, "in latin")




#%%
# Function
# Let us create a function
# A function that prints "Hello, World!"
# %%
def sayHello(): #Must use keyword def to define function in python
    print("Hello World")

# Call that function
sayHello()



# %%
# Create a function where you provide your name and it prints() "Hello <your name>".
# Your name is provided as an argument to the function
#%%
def inputHello(name):
    print('Hello', name)
# Call that function
inputHello('Mike')



# %%
# A function that returns a value
# Create a function that adds two numbers
def addTwo(x, y):
    addition = x + y
    return addition

# Call that function
results = addTwo(9, 2)
print(results)

# or 
def addtwo(x, y):
    return x + y
# Call that function
result = addtwo(9, 1)
print(result)



#%%
# TODO: create a function that takes two numbers and a mathematical operator and 
# return the calculation between the two number based on that operator. Use if else 
# statements
#%%
def operation(x, y, o):
    if o == '+':
        return x + y
    elif o == '*':
        return x * y
    elif o == '/':
        return x / y
    elif o == '-':
        return x - y
    else:
        print('Wrong operator!')
        return 0 # means do nothing 


calc = operation(10, 5, '+')
print(calc)





# Set a default value for arguments
#%%
def addtwo(x=1, y=2): #Can declare the function values explicitly in the definition
    return x + y

results = addtwo() # Will add the two numbers in function definiton
print(results)



#%%
# Create a new file - call it library.py
# Create a function inside library.py that print() 'Hello'
# Import the file in here
import library
#Call that function
library.printhello() #Always look for cube to pull function from other file, use dot operator



# %%
# In library.py, create a function that adds three numbers and call it from here.
import library
library.addThree(1, 2, 3) # Have to save the library file, and restart kernel everytime to get it to work
#Which is why we are ditching interactive shell and going to importing functions from other files.
# %%
