# Sam Wisnoski
# 11/05/2023
# Think Python Chapter 15

import math
import copy

# Chapter 15.1
print('\n\nChapter 15.1 \n')

class Point:
    """Represents a point in 2-D space."""

blank = Point()



# Chapter 15.2
print('\n\nChapter 15.2 \n')

blank.x = 3.0
blank.y = 4.0

x = blank.x

print(blank)
print(blank.x)
print(x)

print('(%g, %g)' % (blank.x, blank.y))
distance = math.sqrt(blank.x**2 + blank.y**2)
print(distance)



def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

print_point(blank)



# Chapter 15.3
print('\n\nChapter 15.3 \n')


class Rectangle:
    """Represents a rectangle.
    attributes: width, height, corner.
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0



# Chapter 15.4
print('\n\nChapter 15.4 \n')


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

print_point(find_center(box))



# Chapter 15.5
print('\n\nChapter 15.5 \n')

box.width = box.width + 50
box.height = box.height + 100

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

print(box.width, box.height)
grow_rectangle(box, 100, 200)
print(box.width, box.height)



# Chapter 15.6
print('\n\nChapter 15.6 \n')

box2 = copy.copy(box)
print(box2 is box)
print(box2.corner is box.corner)

box3 = copy.deepcopy(box)
print(box3 is box)
print(box3.corner is box.corner)

def move_rectangle(rect, movex, movey):
    rect2 = copy.deepcopy(rect)
    rect2.corner.x += movex
    rect2.corner.y += movey
    return rect2



# Chapter 15.9
print('\n\nChapter 15.9 \n')

# Exercise 15.1
print('\n\nExercise 15.1 \n')

class Circle:
    """Represents a circle in 2-D space.
    attributes: center, radius
    """

circle = Circle()
circle.center = Point()
circle.center.x = 150
circle.center.y = 100
circle.radius = 100


def point_in_circle(circle, point):
    distance = math.sqrt((circle.center.x-point.x)**2 + (circle.center.y-point.y)**2)
    if distance <= circle.radius:
        return True

point5 = Point()
point5.x = 1200
point5.y = 200

point7 = Point()
point7.x = 200
point7.y = 80

print(point_in_circle(circle, point5))
print(point_in_circle(circle, point7))


def rect_in_circle(circle, rect):
    rect2 = copy.deepcopy(rect)
    distance = math.sqrt((circle.center.x-rect2.corner.x)**2 + (circle.center.y-rect2.corner.y)**2)
    if distance >= circle.radius:
        return 
    
    distance = math.sqrt((circle.center.x-rect2.corner.x-rect2.width)**2 + (circle.center.y-rect2.corner.y)**2)
    if distance >= circle.radius:
        return 
    
    distance = math.sqrt((circle.center.x-rect2.corner.x)**2 + (circle.center.y-rect2.corner.y-rect2.height)**2)
    if distance >= circle.radius:
        return 
    
    distance = math.sqrt((circle.center.x-rect2.corner.x-rect2.width)**2 + (circle.center.y-rect2.corner.y-rect2.height)**2)
    if distance >= circle.radius:
        return 
    
    return True

def rect_circle_overlap(circle, rect):
    rect2 = copy.deepcopy(rect)
    if point_in_circle(circle, rect2.corner):
        return True

    rect2.corner.x += rect2.width
    if point_in_circle(circle, rect2.corner):
        return True

    rect2.corner.y += rect2.height
    if point_in_circle(circle, rect2.corner):
        return True
    
    rect2.corner.x -= rect2.width
    if point_in_circle(circle, rect2.corner):
        return True
    
    return

box5 = Rectangle()
box5.width = 100
box5.height = 40
box5.corner = Point()
box5.corner.x = 100
box5.corner.y = 80

box7 = Rectangle()
box7.width = 150
box7.height = 100.0
box7.corner = Point()
box7.corner.x = 0.0
box7.corner.y = 0.0

print(rect_in_circle(circle, box5))
print(rect_in_circle(circle, box7))

print(rect_circle_overlap(circle, box5))




# Exercise 15.2
print('\n\nExercise 15.2 \n')

import turtle
bob = turtle.Turtle()
print(bob)

def draw_rect(t, rect):
    t.pu()
    t.setpos(rect.corner.x,rect.corner.y)
    t.pd()
    t.seth(90)
    t.fd(rect.height)
    t.rt(90)
    t.fd(rect.width)
    t.rt(90)
    t.fd(rect.height)
    t.rt(90)
    t.fd(rect.width)

draw_rect(bob, box5)
draw_rect(bob, box7)

def draw_circle(t, circle):
    t.pu()
    t.setpos(circle.center.x,circle.center.y*2)
    t.pd()
    t.circle(circle.radius)

draw_circle(bob,circle)


