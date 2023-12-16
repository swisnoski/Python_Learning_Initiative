# Sam Wisnoski
# 10/16/2023
# Think Python Chapter 9


# Chapter 9.1 
print('\n\nChapter 9.1 \n')

fin = open('words.txt', 'r')
print(fin.readline())
print(fin.readline(27000))

def print_whole():
    for line in fin:
        print(line.strip())

#print_whole()


# Chapter 9.2 
print('\n\nChapter 9.2 \n')

# Exercise 9.1 
print('\n\nExercise 9.1 \n')

def print_20plus():
    for line in fin:
        if len(line.strip()) > 20:
            print(line.strip())

#print_20plus()


# Exercise 9.2 
print('\n\nExercise 9.2 \n')

def has_no_e(): 
    for line in fin:
        if line.strip().count('e') == 0: 
            print(line.strip())

#has_no_e()


# Exercise 9.3
print('\n\nExercise 9.3 \n')

def avoids(letters): 
    for line in fin:
        if letters not in line.strip(): 
            print(line.strip())

#avoids('murgy')


# Exercise 9.4
print('\n\nExercise 9.4 \n')

def uses_only(word, letters): 
    for i in word:
        if i not in letters:
            return False 
    return True

#for line in fin:
#    if uses_only(line.strip(), 'acefhlo'): 
#        print(line.strip())


# Exercise 9.5
print('\n\nExercise 9.5 \n')

def uses_all(word, letters): 
    for i in letters:
        if i not in word:
            return False 
    return True

#for line in fin:
#    if uses_all(line.strip(), 'aeiouy'): 
#    print(line.strip())


# Exercise 9.6 
print('\n\nExercise 9.6 \n')

def is_abercedarian(word):
    for i in range(len(word)-1): 
         if word[i] >= word[i+1]: 
             return False
    return True

#for line in fin:
#    if is_abercedarian(line.strip()): 
#        print(line.strip())


# Chapter 9.3 
print('\n\nChapter 9.3 \n')

# another way to define uses_all
def uses_all2(word, required):
    return uses_only(required, word)


# Chapter 9.4
print('\n\nChapter 9.4 \n')

#Other ways to write is_abecedarian
def is_abecedarian2(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

def is_abecedarian3(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian3(word[1:])

def is_abecedarian4(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i+1
    return True



# Chapter 9.6 
print('\n\nChapter 9.1 \n')

# Exercise 9.7
print('\n\nExercise 9.7 \n')

def tripledoubleletter(word):
    for i in range(len(word)):
        if len(word) < 6:
            return False
        if (word[i] == word[i+1]) & (word[i+2] == word[i+3]) & (word[i+4] == word[i+5]):
            return True
        if i == len(word)-6: 
            return False 

#for line in fin:
#    if tripledoubleletter(line.strip()): 
#        print(line.strip())



# Exercise 9.8
print('\n\nExercise 9.8 \n')

def is_palindrome(word):
    return word[:] == word[::-1]

def convert(num):
    if num <10: 
        return '00000'+str(num)
    if num < 100: 
        return '0000'+str(num)
    if num < 1000: 
        return '000'+str(num)
    if num < 10000: 
        return '00'+str(num)
    if num < 100000: 
        return '0'+str(num)
    else: 
        return str(num) 

def puzzler6digits(sixdig):
    sixdig = convert(sixdig)
    if is_palindrome(sixdig[2:6]):
        sixdig = convert(int(sixdig) + 1)
        if is_palindrome(sixdig[1:6]):
            sixdig = convert(int(sixdig) + 1)
            if is_palindrome(sixdig[1:5]):
                sixdig = convert(int(sixdig) + 1)
                if is_palindrome(sixdig[0:6]):
                    return True
    return False
    
for number in range(999999):
    if number > 100000:
        if puzzler6digits(number):
            print(number)


# Exercise 9.9
print('\n\nExercise 9.9 \n')

def is_reverse(word1, word2):
    return word1[:] == word2[::-1]

def doubledigit(age):
    if age <10: 
        return '0'+str(age)
    else: 
        return str(age)

def agepuzzler(age):
    childage = 0
    momage = age
    count = 0
    while momage <120:
        if is_reverse(str(momage),doubledigit(childage)):
            count = count+1
        childage = childage+1; momage = momage+1
    if count == 8:
        print(age)

for age in range(100):
    agepuzzler(age)
    