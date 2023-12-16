# Sam Wisnoski
# 9/28/2023
# Think Python Chapter 5

import math
import time
import turtle

#Chapter 5.1
print('\n\nChapter 5.1 \n')

minutes = 105
hours = minutes // 60
print(hours)

remainder = minutes % 60 
print(remainder)

print(str(hours) + ' hours ' + str(remainder) + ' minutes')


#Chapter 5.2
print('\n\nChapter 5.2 \n')

x = 7
y = 9

x == y    # x is equal to y 
x != y    # x is not equal to y
x > y     # x is greater than y
x < y     # x is less than y
x >= y    # x is greater than or equal to y
x <= y    # x is less than or equal to y


#Chapter 5.3 
print('\n\nChapter 5.3 \n')

x%2 == 0 or x%3 == 0    #true if n is divisible by 2 or 3
x>0 and x<10            #true if x is greater than zero and x is less than 10
not (x>y)               #true if x is not greater than y 


#Chapter 5.4
print('\n\nChapter 5.4 \n')

if x>0:
    print('x is positive')

if x<0:
    pass #used as a placeholder 


#Chapter 5.5
print('\n\nChapter 5.5 \n')

if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')


#Chapter 5.6
print('\n\nChapter 5.6 \n')

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')


#Chapter 5.7 
print('\n\nChapter 5.7 \n')

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')


#Chapter 5.8 
print('\n\nChapter 5.8 \n')

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(10)


#Chapter 5.10
print('\n\nChapter 5.10 \n')

def recurse():
    recurse()
#recurse()


#Chapter 5.11
print('\n\nChapter 5.11 \n')

color= 'n'
speed= 'n'
name = input('\n\nWhat... is your name? \n')
n = 0; 

if name == 'Arthur, King of the Britons':
    color = input('What... is your favorite color? \n')
else:
    print('Death!')
    n = 1

if color == 'Blue!' and n == 0:
    speed = input('What...is the airspeed velocity of an unladen swallow? \n')
else:
    print('Death!')
    n=1



if speed == 'What do you mean, an African or a European swallow?' and n == 0:
    pass
else:
    print('Death!\n\n')
    n=1

if n==0:
    print('Bridge Passed!\n\n')


#Exercise 5.1 
print('\n\nExercise 5.1 \n')

totseconds = time.time()
x = totseconds/86400
secs = totseconds%86400
hrs = secs/3600
mins = (hrs*60)%60
secs = (mins*60)%60
print(str(int(hrs)) + ' hours ' + str(int(mins)) + ' mins ' + str(int(secs)) + ' secs')
print(str(int(x)) + ' days since epoch\n\n')


#Exercise 5.2
print('\n\nExercise 5.2 \n')

def check_fermat(a, b, c, n):
    if int(a)**int(n) + int(b)**int(n) == int(c)**int(n):
        print('Holy smokes, Fermat was wrong!\n\n')
    else:
        print('No, that doesn’t work.\n\n')

def is_fermat():
    print('Try to prove Fermat wrong! Find values for positive integers such that a^n + b^n = c^n!')
    a,b,c,n = input('Enter values for a, b, c, and n: ').split()
    a = int(a); b = int(b); c = int(c); n =int(n)
    check_fermat(a, b, c, n)

#is_fermat()


#Exercise 5.4
print('\n\nExercise 5.4 \n')

def recurse(n, s):
    '''In order to use this function, n must be an integer greater than 0'''
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

#recurse(4, 0)


#Exercise 5.6
print('\n\nExercise 5.6 \n')

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

fred = turtle.Turtle()
#draw(fred, 10, 10)


def koch(t, length):
    t.fd(length)
    t.lt(60)
    t.fd(length)
    t.rt(120)
    t.fd(length)
    t.lt(60)
    t.fd(length)

def koch2(t, length):
    koch(t, length)  
    t.lt(60)
    koch(t, length)
    t.rt(120)
    koch(t, length)
    t.lt(60)
    koch(t, length)

def koch3(t, length):
    koch2(t, length)  
    t.lt(60)
    koch2(t, length)
    t.rt(120)
    koch2(t, length)
    t.lt(60)
    koch2(t, length)

def koch4(t, length):
    koch3(t, length)  
    t.lt(60)
    koch3(t, length)
    t.rt(120)
    koch3(t, length)
    t.lt(60)
    koch3(t, length)

koch4(fred, 3)



