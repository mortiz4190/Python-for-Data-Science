# ISC2310 - Python for Data Analytics

#%%
print('''
Let us paint...
Tell me the name of the paint you can create from the file some_other_numbers.txt 
(input file).
You need to read that file one line at a time and do some calculations and then 
write to another file your results into another file (call it output.txt, output 
file).
The results should be in lines of length 736.
Similar to what we did when we drew the Mona Lisa.
However for this paint you need to adhere to the following conditions:
if the value read from the input file is greater than 600, the output should be 
'1'.
if the value read from the input file is greater than 300, the output should be 
'3'.
if the value read from the input file is greater than 150, the output should be 
'0'.
else, the output should be '8'.
''')
#%%
# TODO: Answer here:
some_other_numbers = open('some_other_numbers.txt', 'r') #opens file in read only mode
output = open('output.txt', 'w') #opens output file that can be written to
s = ' '
for number in some_other_numbers:
    if len(s) == 736: #Will create a new line at this character, line length == 736
        s += '/n' #New line character
        output.write(s) 
        s = ' ' #Empty the string to restart the process on a new line
    if int(number) > 600:
        s += '1' #cant write numbers into a file, must be in string format
    elif int(number) > 300:
        s += '3' #we start with the higher number 736 such that we can go through our conditions properly
    elif int(number) > 150:
        s += '0'
    else:
        s += '8'
some_other_numbers.close()
output.close()



#%%
print('''
Tuples, Lists, Sets, and Dictionaries
Easiest way to distinguish between them is through the parenthesis used

Tuples: ( )
Lists: [ ]
Sets: { }
Dictionaries: {key : value}
''')

#%%
print('''
Tuples are a collection data types where you can store multiple values into one 
variable. n-value tuple
1. Ordered
2. Unchangeable
3. Allow duplicates
''')

#%%
# An empty tuple
t = ()
print(type(t)) # will return class tuple
#%%
# One element tuple
t = (1)
print(type(t)) 
# Not gonna work, parenthesis create precedence, no comma is an integer or float
#%%
t = (1,) # add a comma after your value to make it a tuple
print(type(t))
print(len(t)) #Length of 1
#%%
t = ("Hello, ", "World!") # can be strings
print(len(t)) # Length of 2
#%%
t = (1, "Hello,", 2.5, True, "World!", False, True) # can be a salad of value types, prints vertically
print(t[0])
print(t[-1]) #Prints last item
print(t[-3]) #Prints third item from back
print() #Prints blank space
for i in t: # You can loop through it
    print(i) # Will print all of the values of the tuple
#%%
# You can't change it
t[0] = 1
print(t) # Will produce an error, cant change values in tuple
#%%
# A tuple of tuples
t = (
    (1,2), 
    (1, "Hello")
    )

# For loop
for i in t:
    print(i) #Prints entire tuple (1,2)
    #print() Prints the same thing as code below (1, "Hello") but with space in between
print() #Prints entire tuple (1, "Hello")

# Nested Loop
for i in t:
    for j in i: # j becomes every sub-element in the tuple, prints each individual of the tuple
        print(j) # Prints every element of the tuple in separate lines



#%%
print('''
Lists are - again - a collection data types where you can store multiple values 
into a single variable: NOTATION IS BRACKETS []
1. Ordered
2. Changeable, different form tuple which is unchangeable
3. Allow duplicates
''')

#%%
# An empty list
l = []

#%%
# A list of integers
l = [1, 2, 3, 4]

#%%
# A list of floats
l = [1.0, 2.5, 3.2, 4.1]
print(l[-1])
print(l)

#%%
# A list of strings
l = ["Hello,", "World!"]
print(l)

#%%
# Remember me
s = 'Hello, World!'
s.split(',') #Splits the string by the comma, but keeps the comma
#%%
# TODO: create an empty list and assign it a variable of your calling
# TODO: fill this list with different types of variables
# TODO: Loop through this list
# TODO: print() the variables in this list
m = [1, 'Two', 3.0, 'Four']
print("This is the array printed: ",m)
for i in m: # go through elements in list one by one, store in i
    print([i]) # turns into a list, prints each element with brackets
    #print(i) ## go through elements in list one by one, store in i, then print i (vertically)


#%%
lst = [1, 2, 3, 4]
# TODO: Change the third value of lst to 5
lst[3-1] = 5 #lst[3-1] is equivalent to lst[2] which is the 0, 1, 2nd element in list or third
print(lst)
#%%
# TODO: Change the last value of lst to 0
lst[-1] = 0
print(lst)
#%%
# TODO: print the first three values of the list using subscripts
lst[:3] #prints first 3 values 





#%%
# A list of lists
lst = [ 
    [1,2], 
    ['Hello', 'World']
    ]
#%%
# TODO: Using nested loops, loop through the list of lists and print its content
lst = [
    [1,2], 
    ['Hello,', 'World!']
    ]
# Two nested loops will print every item in the list of lists
for l in lst: #Takes the lists as a whole as an input
    for item in l: #Gets every subelement of the list
        print(item)


#%%
# Two lists
a = [1, 2, 3, 4]
b = ['one', 'two', 'three', 'four']
# Traverse both of them at the same time using the zip() function
for i, j in zip(a,b): #two variables in this loop i for a, and j for b
    print(i, 'is', j) #Prints a is b respectively


#%%
# Traverse three lists
# TODO: Traverse the following lists and print their values
a = [1, 2, 3, 4]
b = ['One', 'Two', 'Three', 'Four']
c = ['Ichi', 'Ni', 'San', 'Yon']

# i is a, j is b, k is c
for i, j, k in zip(a,b,c): #Same idea with three variables, just set a variable for each list and zip them
    print(i, "is", j, "is", k) #Then print all of the variables



#%%
print('''
Sets are - again - a collection data types where you blah blah blah
1. Not ordered
2. Does not allow duplicates
3. Unchangeable
''')
#%%
# Empty set
s = {}
print(type(s))
print()
# WHAT? Why is it a dictionary, a set cant be empty, python will think its a dictionary
# https://www.reactiongifs.com/tag/what/
# You need to add at least one value in it to become a set
s = {1} #One value makes it a set
print(type(s))
#%%
s = {1, 1}
print(type(s))
# WHAT? I created a set with duplicate values
# https://www.reactiongifs.com/tag/what/
#%%
# Yes, but print() that set
print(s) #It will discard the duplicate when you print it
# https://giphy.com/clips/ufc-ko-thug-rose-weili-zhang-gMzZN2X6G5CSqaQ4vK
#%%
# Can't change that value
s[0] = 0 # values must be unique, cant change the order because the values must be unique otherwise will be discarded
#%%
# You can loop through a set same way you do with a list
# Enough looping for today. Let us move forward





#%%
print('''
{key: value}  //Where key is the name and the values are such
Dictionaries are - again - blah blah blah blah
1. As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, 
dictionaries are unordered.
2. Changeable
3. Can't have two keys with the same name (case sensitive)
''')


#%%

#{key: value} -> dictionary
# Empty dictionary
{}
#%%
# Keys and Values
# {key: value, key: value}
d = {'One': 1, 'Two': 2, 'Three': 3}
print(d)

#%%
# Can't have duplicate keys
d['One'] = 2 #changes the :value to 2 preceding 'One':
print(d)
# WHAT? I just duplicated the first key
# https://www.reactiongifs.com/tag/what/

#%%
# No you did not. You just replaced the value in that key to a new one
print(d)
#%%
# Dictionary length
print(len(d)) #Each 1 count is a combination of a key and a value
# %%
# TODO: Create an empty dictionary and assign it to a variable of your calling
# TODO: Create multiple keys and values in this dictionary
# TODO: loop through this dictionary and print its values. Can't get enough of looping
# %%
d = {}
d['Mike Phone Number'] = 5555555555 # Value, 'Mike Phone Number' is the key
d['Reg Phone Number'] = 7777777777 #Diifferent key
d['Twin Phone Number'] = 4444444444 #Different key

print(d) #Will print all keys with their respective values

#%%
#Can for loop through a dictionary, but it will loop through the KEYS and not the VALUES
for i in d:
    print(i) #Only prints the Keys
    print(d[i]) #Prints only values
    #print(i,d[i]) #Prints the Keys with the values right next to them d[i] means dictionary of i


# %%
d = {'A+': [100, 99, 98, 97, 96], 'B+': [89, 88, 87, 86, 85]}

# %%
for i in d:
    print(i, d[i])
# %%
