# Sam Wisnoski
# 11/01/2023
# Think Python Chapter 13



# Chapter 13.1 
print('\n\nChapter 13.1 \n')


# Exercise 13.1
print('\n\nExercise 13.1 \n')

import string

with open('heart_of_darkness.txt') as hod:
    contenthod = hod.read()

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

contenthod = contenthod.split()
modified_contenthod = []
for word in contenthod:
    word = word.lower()
    word = remove_punctuation(word)
    modified_contenthod.append(word)

#print(modified_contenthod)



# Exercise 13.2
print('\n\nExercise 13.2 \n')

with open('frankenstein.txt','r', encoding='utf-8') as f:
    contentf = f.read()

contentf = contentf.split()
modified_contentf = []
for word in contentf:
    word = word.lower()
    word = remove_punctuation(word)
    modified_contentf.append(word)

#print(modified_contentf)

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

#print(most_frequent(modified_contentf))




# Exercise 13.3
print('\n\nExercise 13.3 \n')

l = (most_frequent(modified_contentf))
print(l[:20])



# Exercise 13.4
print('\n\nExercise 13.4 \n')


def missingwords(wordlist, booklist):
    missinglist = []
    for i in wordlist:
        if i not in booklist:
            if i not in missinglist:
                missinglist.append(i)
    print(missinglist)

#missingwords(['hahaha', 'the'], modified_contentf)



# Chapter 13.2
print('\n\nChapter 13.2 \n')

import random

x = random.random()
y =  random.randint(5, 10)
z = random.choice([1,2,3])
print(x, y, z)



# Exercise 13.5
print('\n\nExercise 13.5 \n')

def choose_from_histogram(histogram):
    sum = 0
    for i in histogram:
        sum = sum + histogram[i]
    print(sum)
    for i in histogram:
        print (str(i), str(histogram[i]) + "/" + str(sum))


#choose_from_histogram(histogram(modified_contentf))


# Chapter 13.6
print('\n\nChapter 13.6 \n')


# Exercise 13.6
print('\n\nExercise 13.6 \n')

with open('words.txt') as f:
    words = f.read().splitlines() 

words.append('i')
words.append('a')

#missingwords(modified_contentf, words)



# Chapter 13.7
print('\n\nChapter 13.7 \n')


# Exercise 13.7
print('\n\nExercise 13.7 \n')

# to make this easier but slightly more jank, im just going to sum all of the words, generate a random number between 1 and sum, and then index that number 

def cumsum(gist):
    fist = gist[:]
    for x in range(len(gist)):
        fist[x]= sum(gist[0:x])
    return fist

def chooserandomword(content):
    hist = histogram(content)
    sum = cumsum(list(hist.values()))
    y =  random.randint(0, sum[-1])
    print(modified_contentf[y])
# i don't know why it wanted me to do it differently in the book

# or why not just 
print(random.choice(modified_contentf))
chooserandomword(modified_contentf)


# Chapter 13.8
print('\n\nChapter 13.8 \n')



# Exercise 13.8
print('\n\nExercise 13.8 \n')

modified_modified_contentf = ' '.join(modified_contentf)

def markov(text, prefix_length=2):
    text = text.split()
    markov_dict = {}

    for i in range(len(text) - prefix_length):
        prefix = tuple(text[i:(i + prefix_length)])
        suffix = text[i + prefix_length]

        if prefix in markov_dict:
            markov_dict[prefix].append(suffix)
        else:
            markov_dict[prefix] = [suffix]
    
    return markov_dict
    
def generate_markov(markov_dict, max_words=50):
    first = random.choice(list(markov_dict.keys()))
    sentence = list(first)

    for i in range(max_words):
        next = (markov_dict[tuple(sentence[(i):(2+i)])])
        sentence.append(next[0])
    
    print(' '.join(sentence))

# generate_markov(markov(modified_modified_contentf))



# Chapter 13.9
print('\n\nChapter 13.9 \n')

import math
import matplotlib.pyplot as plt
import numpy as np

x = np.zeros(100)
y = np.zeros(100)

k = (most_frequent(modified_contentf))
for i in range(100):
    #print(k[i:i+1][0][0], math.log(int(k[i:i+1][0][1])), math.log(i+1))
    x[i] = math.log(int(k[i:i+1][0][1]))
    y[i] = math.log(i+1)

plt.plot(x,y)
plt.show()

