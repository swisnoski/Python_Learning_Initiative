# Sam Wisnoski
# 10/28/2023
# Think Python Chapter 12


# Chapter 12.1 
print('\n\nChapter 12.1 \n')

# Syntactically, a tuple is a comma-separated list of values:
t = 'a', 'b', 'c', 'd', 'e'
print(t)

# OR 

t = tuple('lupins')
print(t)
print(t[0:3])

t = ('A',) + t[1:]
print(t)

#The relational operators work with tuples and other sequences; Python 
# starts by comparing the first element from each sequence. If they are 
# equal, it goes on to the next elements, and so on, until it finds 
# elements that differ. Subsequent elements are not considered (even 
# ifthey are really big).

print((0, 1, 2000000) < (0, 3, 4))



# Chapter 12.2
print('\n\nChapter 12.2 \n')

addr = 'monty@python.org'
uname, domain = addr.split('@')
 
# splits the addr into a tuple with two variables, uname and domains



# Chapter 12.3
print('\n\nChapter 12.3 \n')

# Strictly speaking, a function can only return one value, but if the 
# value is a tuple, the effect is the same as returning multiple values.

t = divmod(7, 3)
print(t)
# Returns a tuple



# Chapter 12.4
print('\n\nChapter 12.4 \n')

# Functions can take a variable number of arguments. A parameter name that 
# begins with * gathers arguments into a tuple. For example, printall takes
# any number of arguments and prints them:

def printall(*args):
    print(args)

printall(1, 13, 123, 123, 'asda', 'heeheehaha')

# The complement of gather is scatter. If you have a sequence of values
# and you want to pass it to a function as multiple arguments, you can 
# use the * operator. For example, divmod takes exactly two arguments; 
# it doesn’t work with a tuple:

t = (7, 3)
print(divmod(*t))


# Chapter 12.5
print('\n\nChapter 12.5 \n')

s = 'abc'
t = [0, 1, 2]
for pair in zip(s, t):
    print(pair)

print(list(zip(s,t)))
print(list(zip('Anne', 'Elk')))

t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print(number, letter)

for index, element in enumerate('abc'):
    print(index, element)


# Chapter 12.6
print('\n\nChapter 12.6 \n')

# dict to tuple
d = {'a':0, 'b':1, 'c':2}
t = d.items()
print(t)

# tuple to dict
t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)
print(d)

l = dict(zip('abc', range(3)))
print(l)


# Chapter 12.10
print('\n\nChapter 12.10 \n')


# Exercise 12.1
print('\n\nExercise 12.1 \n')

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def most_frequent(stwing):
    d = histogram(stwing)
    t = d.items()
    l = [(0, 0)]
    for i in t:
        for g in range(len(l)):
            if i[1] >= l[g][1]:
                l.insert(g,i)
                break
    l.pop()
    return l 

print(most_frequent('The Nellie, a cruising yawl, swung to her anchor without a flutter of the sails, and was at rest. The flood had made, the wind was nearly calm, and being bound down the river, the only thing for it was to come to and wait for the turn of the tide.'))


# Exercise 12.2
print('\n\nExercise 12.2 \n')

with open('words.txt') as f:
    content = f.read().splitlines() 




#def createlist():
#    wist = []
#    for i in content:
#        l = most_frequent(i)
#        if l in wist:
#            wist.append(l)
#    return wist

#for i in content:
#    gist = createlist()
#    if most_frequent(i) in gist:
#        print(i)

from collections import defaultdict

def all_anagram(s):
	d = defaultdict(list)
	for i in s:
		signature = ''.join(sorted(i)) 
		d[signature].append(i)

	return d

def print_anagram_in_order(s):
	d = all_anagram(s)
	l = []
	for signature, words in d.items():
		if len(words) > 1:
			l.append((len(words),words))
	l.sort(reverse=True)
	for x in l:
		print(x)
          
#print_anagram_in_order(content)


# Exercise 12.3
print('\n\nExercise 12.3 \n')

def pair_distance(a, b):
	assert len(a) == len(b) 
	ctr = 0
	for c1, c2 in zip(a,b): 
		if c1 != c2:
			ctr += 1
	return ctr

def find_metathesis(s):
	d = all_anagram(s)
	for v in d.values():
		for a in v:
			for b in v:
				if a < b and pair_distance(a,b) == 2:
					print (a, b)
					
#find_metathesis(content)

