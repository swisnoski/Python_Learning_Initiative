# Sam Wisnoski
# 10/9/2023
# Think Python Chapter 8


# Chapter 8.1 
print('\n\nChapter 8.1 \n')

fruit = 'banana'
letter = fruit[1]
print(letter)
letter = fruit[0]
print(letter)
print(fruit[0:6])


# Chapter 8.2 
print('\n\nChapter 8.2 \n')

print(len(fruit))
last = fruit[len(fruit)-1]
print(last)
print(fruit[-1])
print(fruit[-2])


# Chapter 8.3
print('\n\nChapter 8.3 \n')

game = ' Elden Ring '
index = 0
while index < len(game):
    letter = game[index]
    print(letter)
    index = index + 1

for letter in fruit:
    print(letter)

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)


# Chapter 8.4
print('\n\nChapter 8.4 \n')

print(fruit[:3])
print(fruit[3:])
print(fruit[3:3])
print(fruit[:])


# Chapter 8.6 
print('\n\nChapter 8.6 \n')

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find('the lazy dog jumps over the quick brown fox', 'c'))


# Chapter 8.7
print('\n\nChapter 8.7 \n')

def count(word, letter):
    count = 0
    for i in word:
        if i == letter:
            count = count + 1
    return count

print(count('banana', 'a'))


# Chapter 8.8
print('\n\nChapter 8.8 \n')

fruit = 'banana'
print(fruit.upper())
game = 'ELDEN RING'
print(game.lower())

print(game.find('E'))
print(fruit.find('na'))


# Chapter 8.9
print('\n\nChapter 8.9 \n')

print('a' in fruit) 
print('a' in game) 

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('samuel wisnoski', 'rohan bendapudi')


# Chapter 8.10
print('\n\nChapter 8.10 \n')

def alphabetize(word1, word2):
    if word1.lower() < word2.lower():
        print(word1 + ' comes before ' + word2)
    elif word1.lower() > word2.lower(): 
        print(word2 + ' comes before ' + word1)
    else:
        print('THIS IS THE SAME WORD!!!')

alphabetize('Backpack', 'Meatball')


# Chapter 8.11
print('\n\nChapter 8.11 \n')

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1 
    while j > -1:
        if word1[i] != word2[j]:
            return False 
        i = i+1
        j = j-1
    return True

print(is_reverse('pots','stop'))
print(is_reverse('pots','tops'))


# Exercise 8.1 
print('\n\nExercise 8.1 \n')

word = 'go hang a salami im a lasagna hog'
print(word.lstrip('go hang a '))
print(word.replace('a','b'))


# Exercise 8.2
print('\n\nExercise 8.2 \n')

fruit = 'banana'
print(fruit.count('a'))


# Exercise 8.3 
print('\n\nExercise 8.3 \n')

word = 'gohangasalamiimalasagnahog'
print(word[:] == word[::-1])


# Exercise 8.4 
print('\n\nExercise 8.4 \n')

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# This function only checks the first letter

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# This function doesn't return actual T/F, also c is 
# not a variable so it will always return true

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
# This function only checks the last letter

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# This fuction functions correctly 

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
# This function returns false for a single
# uppercase letter

print('\n\n\n')
print(any_lowercase1('Fred'))
print(any_lowercase2('FRED'))
print(any_lowercase3('freD'))
print(any_lowercase4('FReD'))
print(any_lowercase5('freD'))
print('\n\n')


# Exercise 8.5 
print('\n\nExercise 8.5 \n')

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

print(rotate_word('cheer', 7))
    
    

