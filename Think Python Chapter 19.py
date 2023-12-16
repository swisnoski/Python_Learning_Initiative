# Sam Wisnoski
# 11/30/2023
# Think Python Chapter 18

import math

# Chapter 19.1
print('\n\nChapter 19.1 \n')

x = 10

if x > 0:
    y = math.log(x)
else:
    y = float('nan')

# can be rewritten using the conditional expression
y = math.log(x) if x > 0 else float('nan')



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# can be rewritten using the conditional expression
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)




# Chapter 19.2
print('\n\nChapter 19.2 \n')


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

#We can write this more concisely using a list comprehension:
def capitalize_all(t):
    return [s.capitalize() for s in t]



def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

#We can write this more concisely using a list comprehension:
def only_upper(t):
    return [s for s in t if s.isupper()]



# Chapter 19.3
print('\n\nChapter 19.3 \n')

#Generator expressions are similar to list comprehensions, but with parentheses instead of square brackets:
g = (x**2 for x in range(5))
for val in g:
    print(val)




# Chapter 19.4
print('\n\nChapter 19.4 \n')

print(any([False, False, True]))
print(any([False, False, False]))
print(all([False, True, True]))
print(all([True, True, True]))


# often used in generator expressions

print(any(letter == 't' for letter in 'monty'))


def avoids(word, forbidden):
    return not any(letter in forbidden for letter in word)



# Chapter 19.5
print('\n\nChapter 19.5 \n')

def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

# Can be rewritten with sets
def subtract(d1, d2):
    return set(d1) - set(d2)




def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False

# Can be rewritten with sets
def has_duplicates(t):  
    return len(set(t)) < len(t)


# Chapter 19.11
print('\n\nChapter 19.11 \n')


# Exercise 19.1
print('\n\nExercise 19.1 \n')

#Final Exercise!!! Finally OMG I never thought I would make it 

#Goal: rewits this function with nested conditional expressions

def binomial_coeff(n, k):
    """
    Compute the binomial coefficient "n choose k".

    n: number of trials
    k: number of successes

    returns: int
    """

    if k == 0:
        return 1
    if n == 0:
        return 0
    
    res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    return res


def binomial_coeff2(n, k):
    """Compute the binomial coefficient "n choose k".
    
    n: number of trials
    k: number of successes
    returns: int
    """
    return 1 if k == 0 else 0 if n == 0 else binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)


n = 18
k = 9
print(binomial_coeff(n,k))
print(binomial_coeff2(n,k))