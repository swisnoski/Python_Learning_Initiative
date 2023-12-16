# Sam Wisnoski
# 10/18/2023
# Think Python Chapter 11


# Chapter 11.1 
print('\n\nChapter 11.1 \n')

eng2sp = dict()
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'
print(eng2sp)
print(eng2sp['one'])
print(len(eng2sp))
print('uno' in eng2sp)
print('one' in eng2sp)

vals = eng2sp.values()
print(vals)


# Chapter 11.2
print('\n\nChapter 11.2 \n')

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print(histogram('sam wisno'))
print(histogram('hahaahahahahahaha'))

h = histogram('a')
print(h.get('a', 0))
print(h.get('c', 0))


# Chapter 11.3
print('\n\nChapter 11.3 \n')

def print_hist(h):
    for c in h:
        print(c, h[c])

h = histogram('parrot')
print_hist(h)

for key in sorted(h):
    print(key, h[key])


# Chapter 11.4
print('\n\nChapter 11.4 \n')

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

# the raise commands creates an error, in this case, lookuperror 

key = reverse_lookup(h, 2)
print(key)
#key = reverse_lookup(h, 3)



# Chapter 11.5
print('\n\nChapter 11.5 \n')

# this maps values to keys 
# the new values are lists
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

# note, keys should be immutable 

print(histogram(h))
print(invert_dict(h))



# Chapter 11.6
print('\n\nChapter 11.6 \n')

known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

print(fibonacci(3))



# Chapter 11.7
print('\n\nChapter 11.7 \n')

been_called = False

def example2a():
    been_called = True

example2a()
print(been_called)

def example2b():
    global been_called
    been_called = True

example2b()
print(been_called)


print(known)

def example4():
    known[2] = 4

example4()
print(known)

def example5():
    global known
    known = dict()

example5()
print(known)



# Chapter 11.10
print('\n\nChapter 11.10 \n')


# Exercise 11.1
print('\n\nChapter 11.1 \n')

with open('words.txt') as f:
    content = f.read().splitlines() 

words = dict()
def wordsdic(gist):
    for word in gist:
        words[word] = word

wordsdic(content)

print('in' in words)
# this way of seaching is signifigantly faster 



# Exercise 11.2
print('\n\nChapter 11.2 \n')

def invert_dict2(d):
	inverse = dict()
	for key in d:
		val = d[key]
		inverse.setdefault(val, []).append(key) # searched online to get this answer and it's same as the author's 
	return inverse
	
print(invert_dict2(h))



# Exercise 11.3
print('\n\nChapter 11.3 \n')

# memorization does not allow us to evaluate the function with 
# bigger arguments, since we reach maximum recursion 



# Exercise 11.4
print('\n\nChapter 11.4 \n')

def has_duplicate(d):
    d = invert_dict2(d)
    for key in d:
        if len(d[key]) > 1:
            return True
    return False 

print(has_duplicate(eng2sp))
print(has_duplicate(h))



# Exercise 11.5
print('\n\nChapter 11.5 \n')

def rotate_word(word, int): 
    t = [''] * len(word); w = 0; word_final = ''
    for i in word:
        l = ord(i)+int
        if i.isupper():
            if l>90:  l = l-26
            if l<65:  l = l+26
        if i.islower(): 
            if l>122: l = l-26
            if l<97:  l = l+26
        l = chr(l)
        t[w] = i.replace(i, l)
        word_final = word_final + t[w]
        w = w+1
    return word_final

def rotate_wordlist(gist):
    for word in gist: 
        num = 1; 
        while num < 26: 
            rword = rotate_word(word, num)
            if rword in gist:
                print(word + ' ' + rword)
            num += 1 
    
rotate_wordlist(content)



# Exercise 11.6
print('\n\nChapter 11.6 \n')

# This exercise was meant to be completed with downloads from the thinkpython website, which no longer exists




