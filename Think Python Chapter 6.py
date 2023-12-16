# Sam Wisnoski
# 10/4/2023
# Think Python Chapter 6

import math

# Chapter 6.1 
print('\n\nChapter 6.1 \n')

def area(radius):
    return math.pi * radius**2

print(area(9))

def absolute_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x
    
print(absolute_value(-25.9))
print(abs(-25.9))


# Chapter 6.2
print('\n\nChapter 6.2 \n')

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y1-y2)**2)

print(distance(1,2,1,9))

def hypotenuse(leg1, leg2):
    return math.sqrt(leg1**2 + leg2**2)

print(hypotenuse(3,4))


# Chapter 6.3
print('\n\nChapter 6.3 \n')

def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

print(circle_area(0,0,1,1))


# Chapter 6.4
print('\n\nChapter 6.4 \n')

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
    
def is_divisible2(x, y):
    return x % y == 0

print(is_divisible2(9,1))


# Chapter 6.5
print('\n\nChapter 6.5 \n')

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(20))


# Chapter 6.7
print('\n\nChapter 6.7 \n')

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(3))


# Chapter 6.8
print('\n\nChapter 6.8 \n')

def factorial2(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial2('fredrick'))


# Exersize 6.1
print('\n\nExercise 6.1 \n')

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))


# Exersize 6.2
print('\n\nExercise 6.2 \n')

def ack(m,n): 
    if m==0:
        return n+1
    if m>0 and n==0:
        return ack(m-1,1)
    if m>0 and n>0:
        return ack(m-1, ack(m,n-1))

print(ack(3,4))


# Exersize 6.3
print('\n\nExercise 6.3 \n')

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) == 0:
        print('Palindrome!')
        return True
    if first(word)==last(word):
        return is_palindrome(middle(word))  
    else:
        print('Not a palindrome!')
        return False  

is_palindrome('gohangasalami!imalasagnahog')
print(is_palindrome('gohangasalami!imalasagnahog'))


# Exercise 6.4
print('\n\nExercise 6.4 \n')

def is_power(a,b):
    if b == 0:
        print('Not a power!')
        return False
    if a/b == 1 or a==1:
        print('Is power!')
        return True
    elif a%b != 0: 
        print('Not a power!')
        return False
    else:
        is_power((a/b), b)

print(is_power(1,1))


# Exercise 6.5
print('\n\nExercise 6.5 \n')

def gcd(a,b):
    if a+b == a:
        return a 
    else:
        return gcd(b, a%b)

print(gcd(99, 121))




