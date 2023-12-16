# Sam Wisnoski
# 10/17/2023
# Think Python Chapter 10


import random


# Chapter 10.1 
print('\n\nChapter 10.1 \n')

# these are all lists
[10, 20, 30, 40]
['crunchy frog', 'ram bladder', 'lark vomit']
['spam', 2.0, 5, [10, 20]]
# a list within another list is nested

# more lists with variables!
cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [42, 123]
empty = []
print(cheeses, numbers, empty)



# Chapter 10.2
print('\n\nChapter 10.2 \n')

print(numbers)
numbers[1] = 5
print(numbers)
print('Edam' in cheeses)
print('Swiss' in cheeses)



# Chapter 10.3 
print('\n\nChapter 10.3 \n')

for cheese in cheeses:
    print(cheese)

for i in range(len(numbers)):
    numbers[i] = numbers[i] *2 
print(numbers)

for x in []:
    print('This never happens.')


# Chapter 10.4 
print('\n\nChapter 10.4 \n')

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

d = [1, 2, 3] * 3
print(d)



# Chapter 10.6
print('\n\nChapter 10.6 \n')

t = ['a', 'b', 'c']
t.append('d')
print(t)


t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)


t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)



# Chapter 10.7
print('\n\nChapter 10.7 \n')

def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

# this function does the same thing
sum(numbers)

stringlist = ['a', 'b', 'c', 'd', 'e']
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.upper())
    return res

print(capitalize_all(stringlist))

stringlist2 = ['D', 'A', 'b', 'c', 'D', 'e']
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

print(only_upper(stringlist2))



# Chapter 10.8
print('\n\nChapter 10.8 \n')

t = ['a', 'b', 'c', 'd']
x = t.pop(1)
# only works with one value
print(t)
print(x)

t = ['a', 'b', 'c', 'd']
del t[1:3]
print(t)

# if you know the element you want to remove (but not the index), you can use remove:
t = ['a', 'b', 'c', 'd']
t.remove('b')
print(t)


# Chapter 10.9
print('\n\nChapter 10.9 \n')

# you can convert a string to a list of characters 
string = 'Sam Prevette'
stringlist = list(string)
print(stringlist)

# split splits into words
stringsplit = string.split()
print(stringsplit)

# you can add delimiter as an argument to split words
# by specifc things, such as a hyphen or 'a'

string = 'spam-sham-slam'
print(string.split('-'))
print(string.split('a'))

# join is the opposite of split (duh)

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
print(delimiter.join(t))



# Chapter 10.10
print('\n\nChapter 10.10 \n')

a = [1, 2, 3]
b = a
print(b is a)
b[0] = 42
print(b)
print(a)


# Chapter 10.15
print('\n\nChapter 10.15 \n')



# Exercise 10.1
print('\n\nExercise 10.1 \n')

def nested_sum(gist):
    total = 0
    for x in gist:
        total += sum(x)
    return total

print(nested_sum([[20, 10], [30], [40, 50, 60]]))



# Exercise 10.2
print('\n\nExercise 10.2 \n')

def cumsum(gist):
    fist = gist[:]
    for x in range(len(gist)):
        fist[x]= sum(gist[0:x])
    return fist

print(cumsum([1, 2, 3]))



# Exercise 10.3
print('\n\nExercise 10.3 \n')

def middle(gist):
    del gist[len(gist)-1]
    del gist[0]
    return gist

print(middle([1,2,3,4]))



# Exercise 10.4
print('\n\nExercise 10.4 \n')

def chop(gist):
    gist.pop(len(gist)-1)
    gist.pop(0)

fist = [1,2,3,4]
print(chop(fist))
print(fist)



# Exercise 10.5
print('\n\nExercise 10.5 \n')

def is_sorted(gist):
    fist = gist[:]
    fist.sort()
    return fist == gist

print(is_sorted([1,2,3,4,6,5]))
print(is_sorted([1,2,3,4,5,6]))



# Exercise 10.6
print('\n\nExercise 10.6 \n')

def is_anagram(word1, word2):
    word1 = list(word1); word2 = list(word2)
    for i in word1: 
        if i not in word2: 
            return False
        else: 
            word2.remove(i)
    return word2 == []

print(is_anagram('popopopopop', 'balloon'))
print(is_anagram('the eyes', 'they see'))


# Exercise 10.7
print('\n\nExercise 10.7 \n')

def has_duplicate(gist):
    fist = gist[:]
    for i in gist:
        fist.remove(i)
        if i in fist:
            return True
    return False

mist = [1,2,4,5,6,7,8,'a','a']
print(has_duplicate([1,2,3,4,5,6]))
print(has_duplicate(mist))
print(mist)


# Exercise 10.8
print('\n\nExercise 10.8 \n')

count = 0
trials = 1000
for i in range(1000):
    x = []
    for i in range(23):
        x.append(random.randint(1,365))
    if has_duplicate(x):
        count += 1

percentage = count/trials
print(percentage)


# Exercise 10.9
print('\n\nExercise 10.9 \n')

fin = open('words.txt', 'r')

def wordlist():
    x = []
    for line in fin:
        x.append(line)
    return x

def wordlist2(): 
    x = []
    for line in fin:
        x = x+[line]
    return x

#print(wordlist2())


# Exercise 10.10
print('\n\nExercise 10.10 \n')

with open('words.txt') as f:
    content = f.read().splitlines() 

def in_bisect(word, list):
    if word == content[int(len(content)/2)]:
        return True
    if word < content[int(len(content)/2)]:
        list = list[0:int(len(content)/2)]
    if word > content[int(len(content)/2)]:
        list = list[int(len(content)/2):int(len(content))]
    return word in list

print(in_bisect('aaa', content))
print(in_bisect('aa', content))


# Exercise 10.11
print('\n\nExercise 10.11 \n')

def reverse_pair(gist, word):
    word2 = word[::-1]
    return in_bisect(word2, gist)

for word in content:
    if reverse_pair(content, word):
        print(word, word[::-1])

