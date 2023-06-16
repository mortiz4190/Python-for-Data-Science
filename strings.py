# ISC2310 - Python for Data Analytics

'''
Review
'''
#%%
print('''
Assume there is a city of 3000 residents (start_population) where you are the 
mayor. You manged to formulate an equation that will predict the population growth 
at the end of every year:
The equation is as follows:
growth = start_population * e ** (growth_rate * year)
e is Euler number = 2.71
Assume the growth rate is 7%
Write a for loop to predict the growth rate of this city for the next 5 years
https://socratic.org/questions/how-do-you-calculate-population-growth
''')
#year must be the counter or year must be the index
#%%
# Answer here:
start_population = 3000
euler = 2.71
growthRate = 0.07
year = int(input("What year is it?: "))
for year in range(1, 6):
    growth = start_population * euler ** (growthRate * year)
    print("Population growth for year", year ,"is: ", growth)

'''
Back to Strings...
--------------------
Never get tired of them.
'''
#%%
# TODO: print() 'Hello, World!'
hey = print("Hello World!")
# %%
# What is the length of that sentence you just printed?
# TODO: Any guesses?
len("Hello World") #Length of strings are 1 indexed
# %%
# To find the length of a string, we use the len() function
len('Hello, World!')
# %%
# TODO: What is the len() of an empty string?
len('')
# %%
# TODO: What is the len() of a space (' ')
len(' ')
# %%
# TODO: Create a variable and assign to it the sentence 'Hello, World!
s = 'Hello, World!'
s[-6:-1]
# %%
# TODO: What is the len() of that variable?
hey = "Hello World!"
len(hey)
# %%
print('''
The Subscript Operator...
---------------------------
Lets say I want to print() only the 5th character of that sentence 'o'.
We use the subscript operator [].
Remember, Python starts counting from 0 and not 1.
''')
s = 'Hello, World!'
print(s[4])
print(s[5-1])
# %%
# TODO: print() the 13th character of that sentence (1 indexed)
s = 'Hello, World!'
print(s[12])
#%%
print('''
A better way to get the last character in a string using subscript
''')
print(s[-1])
#%%
print('''
str functions
lower() and upper() are great beginner examples.
https://www.askpython.com/python/string/python-string-functions
''')
# Change the characters in variable s above to all lower case
print(s.lower())
# TODO: change it to upper case
print(s.upper())

#%%
print('''
Splitting a str. Using the split() function
''')
s = 'Hello, World!'
print(s.split(','))
# The output of this is called a list of strings.
#%%
# TODO: Split the variable s at the character o
s = 'Hello, World!'
print(s.split('o'))

# %%
data = "myprogram.exe"
# TODO: What does the following commands do?
data[2]
print(data[-2])
len(data) #Returns a one-indexed count of the length
data[0:8] #Does not include 8, [] operator is zero indexed!!

#%%
# Using the variable data again
# TODO: extract "gram" from it
print(data[5:9])


# Anther TODO: extract ".exe" from it.
print(data[9:]) #Start at 9 and go from there
print(data[-4:]) #Start 4 spaces back (1 index count)
#%%
'''
LOOPING AGAIN. But with Strings 
'''
s = 'Hello, World!'
for x in s:
    print(x)
# %%
# Remember this name
full_name = '''wolfeschlegelsteinhausenbergerdorffwelchevoralternwarengewissenhaftschaferswesse
nschafewarenwohlgepflegeundsorgfaltigkeitbeschutzenvonangreifendurchihrraubgierigfe
indewelchevoralternzwolftausendjahresvorandieerscheinenvanderersteerdemenschderraum
schiffgebrauchlichtalsseinursprungvonkraftgestartseinlangefahrthinzwischensternarti
graumaufdersuchenachdiesternwelchegehabtbewohnbarplanetenkreisedrehensichundwohinde
rneurassevonverstandigmenschlichkeitkonntefortpflanzenundsicherfreuenanlebenslangli
chfreudeundruhemitnichteinfurchtvorangreifenvonandererintelligentgeschopfsvonhinzwi
schensternartigraum'''
#TODO: What is the last character in this name?
print(full_name[-1])
print(full_name[-10:])
print(full_name[+1] )

#%%
print('''
NESTED LOOPING:
Let's assume that we want to group the alphabet characters in that name by the 
number of their occurrence.
Write a nested for loop to calculate the many occurrences of every alphabet in 
there. 
''')
#%%
# Answer here:
full_name = '''wolfeschlegelsteinhausenbergerdorffwelchevoralternwarengewissenhaftschaferswesse
nschafewarenwohlgepflegeundsorgfaltigkeitbeschutzenvonangreifendurchihrraubgierigfe
indewelchevoralternzwolftausendjahresvorandieerscheinenvanderersteerdemenschderraum
schiffgebrauchlichtalsseinursprungvonkraftgestartseinlangefahrthinzwischensternarti
graumaufdersuchenachdiesternwelchegehabtbewohnbarplanetenkreisedrehensichundwohinde
rneurassevonverstandigmenschlichkeitkonntefortpflanzenundsicherfreuenanlebenslangli
chfreudeundruhemitnichteinfurchtvorangreifenvonandererintelligentgeschopfsvonhinzwi
schensternartigraum'''

alphabet = "abcdefghijklmnopqrstuvwxyz"

for alphabet in alphabet:
    alphabetCount = 0
    for character in full_name:
        if character == alphabet:
            alphabetCount += 1
    print("The number of", alphabet.upper()+ "'s is: ", alphabetCount)

# %%
