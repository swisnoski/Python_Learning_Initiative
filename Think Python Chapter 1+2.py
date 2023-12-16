# Sam Wisnoski
# 9/21/2023
# Think Python Chapter 1+2


# Chapter 1
print('\n\nChapter 1\n')

print('hello')
a =7**7
print(a)

type(2)


# Chapter 2
print('\n\nChapter 2\n')

miles = 26.2
print (miles *1.61)

# Exercise 2.1
print('\n\nExercise 2.1\n')

x = 5
x = x + 1 
print (x)
x = y = 1


# Exercise 2.2 
print('\n\nExercise 2.2\n')

pi = 3.14159265
r = 5
v = (4/3)*pi*r**3
print(v)

price = 24.95 
bsprice = price*.4*60 
shipping = 3 + 59*.75

total_price = bsprice+shipping
print(total_price)

runtime_sec = 2*(8*60 + 15) + 3*(7*60 + 12)
runtime_mins = runtime_sec/60 
time = 52+runtime_mins -60
ntime = int(time)
stime = str(ntime)
print("time is 7:" + stime) 