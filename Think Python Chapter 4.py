# Sam Wisnoski
# 9/28/2023
# Think Python Chapter 4

#Chapter 4.1 
print('\n\nChapter 4.1 \n')

import math
import turtle
bob = turtle.Turtle()
print(bob)
#bob.fd(100)
#bob.rt(90)
#bob.fd(100)
#bob.rt(90)
#bob.fd(100)
#bob.rt(90)
#bob.fd(100)

# fd,bk,rt,lt are methods, associated with bob
# a method is similar to a function but with different syntax
# each turtle is also holding a pen which can be up or down (pu, pd)
# fd = forward, bk = backward, lt = left turn, rt = right turn
# fd & bk -> pixels;   lt & rt -> degrees


#Chapter 4.2
print('\n\nChapter 4.2 \n')

#for i in range(4):
    #print('Hello!')

#for i in range(4):
    #bob.fd(100)
    #bob.lt(90)


#Chapter 4.3
print('\n\nChapter 4.3 \n')

#square with turtle 't' and side length 'length'
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 50)

#polygon with turtle 't', side length 'length', and side number 'n'
def polygon(t, n, length):
    deg = 360/n
    j = int(n)
    for i in range(n):
        t.fd(length)
        t.lt(deg)

#polygon(bob, 7, 100)   

#circle with turtle 't' and radius 'r'
def circle(t, r):
    len = (r*math.pi)/180
    polygon(bob, 360, len)

#circle(bob, 100)

#arc with turtle 't', radius 'r', and angle 'angle'
def arc(t, r, angle):
    len = (r*math.pi)/180
    for i in range(angle):
        t.fd(len)
        t.rt(1)

#arc(bob, 100, 180)


#Chapter 4.4
print('\n\nChapter 4.4 \n')

alice = turtle.Turtle()
#square(alice, 200)


#Chapter 4.6
print('\n\nChapter 4.6 \n')

def circle2(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference /n
    polygon(t, n, length)   

#circle2(alice, 100)
#circle2(bob, 20)


#Chapter 4.7
print('\n\nChapter 4.7 \n')

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polyline2(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.rt(angle)

def polygon2(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc2(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle3(t, r):
    """blah blah blah makes a circle"""
    arc(t, r, 360)


# Exercise 4.2
print('\n\nExercise 4.2 \n')

def flower(t, petals):
    for i in range(petals):
        deg = 360/petals
        arc2(t, 100, deg)
        t.lt((180-deg))
        arc2(t, 100, deg)

#flower(bob, 8)


# Exercise 4.3
print('\n\nExercise 4.3 \n')

def pies(t, slices, len):
    deg = 360/slices
    for i in range(slices):
        t.fd(len)
        t.lt((180-deg)/2)
        t.lt(deg)
        t.fd(len/(2*math.sin(math.pi/slices)))
        t.bk(len/(2*math.sin(math.pi/slices)))
        t.rt((180-deg)/2)

#pies(bob, 12, 30)


# Exercise 4.5
print('\n\nExercise 4.5 \n')
bob.speed(20)

def spiral(t, big):
    len=0
    for i in range(big):
        t.fd(len)
        t.lt(10)
        len = len+.2

spiral(bob, 400)



turtle.mainloop()









