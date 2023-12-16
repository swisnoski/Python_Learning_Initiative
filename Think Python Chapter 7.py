# Sam Wisnoski
# 10/9/2023
# Think Python Chapter 7

import math

# Chapter 7.3
print('\n\nChapter 7.3 \n')

def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0: 
            n = n / 2
        else: 
            n = n*3 + 1
    print('1')

countdown(3)
sequence(9)


# Chapter 7.4
print('\n\nChapter 7.4 \n')

def take_input():
    while True:
        line = input('> ')
        if line == 'done':
            break
        print(line)
    print('Done!')

#take_input()


# Exercise 7.1
print('\n\nExercise 7.1 \n')

epsilon = 0.00000000000000001

#a is number being sqrted, x is estimate  
def mysqrt(a,x):
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return x

def test_square_root():
    print("a    mysqrt(a)   math.sqrt(a)   diff")
    print("-    ---------   ------------   ----")
    for i in range(1, 26):
        print(str(i) + '    ' +str(mysqrt(i,i/2)) + '   ' + str(math.sqrt(i)) + '   ' + str(math.sqrt(i)-mysqrt(i,i/2)))

test_square_root()


# Exercise 7.2
print('\n\nExercise 7.2 \n')

def eval_loop():
    while True:
        line = input("Please enter a problem to be evaluated, or type 'done' to exit program: \n> ")
        if line == 'done':
            break
        x = eval(line)
        print(eval(line))
    print('Done!')
    return x

#eval_loop()


# Exercise 7.3 
print('\n\nExercise 7.3 \n')

def estimate_pi():
    x = 0; i = 0; y = 0
    while abs(y-math.pi) > 1e-15:
        x = x+((math.factorial(4*i)*(1103+26390*i))/(((math.factorial(i))**4)*(396**(4*i))))
        i = i+1
        y = 1/(x*(2*math.sqrt(2))/9801)
    return y

print(estimate_pi())
print(math.pi)



