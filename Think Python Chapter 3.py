# Sam Wisnoski
# 9/22/2023
# Think Python Chapter 3

# Chapter 3
print('\n\nChapter 3 \n')

def repeat_lyrics():
     print_lyrics()
     print_lyrics()

def print_lyrics():      
     print("You do the walk")
     print("You do the walk of life")

repeat_lyrics()

def print_twice(bruce):
     print(bruce)
     print(bruce)

print_twice("spam " *8)
b = "ahhh! a bee!"
print_twice(b)


def print_twice(bruce):
    print(bruce)    
    print(bruce)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)

# Exercise 3.1
print('\n\nExercise 3.1 \n')

def right_justify(s):
    print("                                                         "+ s)

right_justify('monty')

# Exercise 3.2
print('\n\nExercise 3.2 \n')

def do_twice(f, a):
    f(a)
    f(a)

def print_spam():
    print('spam')

do_twice(print_twice, 'spam')

def do_four(h, b):
    do_twice(h, b)
    do_twice(h, b)

do_four(print_twice, 'spam')

# Exercise 3.3
print('\n\nExercise 3.3 \n')
def grid():
    print('+ - - - - + - - - - +')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('+ - - - - + - - - - +')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('+ - - - - + - - - - +')

grid()

def mega_grid():
    print('+ - - - - + - - - - +')
    print('|    |    |    |    |')
    print('| - - - - | - - - - |')
    print('|    |    |    |    |')
    print('+ - - - - + - - - - +')
    print('|    |    |    |    |')
    print('| - - - - | - - - - |')
    print('|    |    |    |    |')
    print('+ - - - - + - - - - +')

mega_grid()

