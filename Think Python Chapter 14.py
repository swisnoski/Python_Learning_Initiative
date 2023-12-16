# Sam Wisnoski
# 11/04/2023
# Think Python Chapter 14



# Chapter 14.2
print('\n\nChapter 14.2 \n')

fout = open('output.txt', 'w')

line1 = "I'm starvin', darlin', let me put my lips to somethin'\n"
line2 = "Let me wrap my teeth around the world\n"
line3 = "Start carvin', darlin', I want to smell the dinner cookin'\n"
line4 = "I want to feel the edges start to burn\n"
fout.write(line1+line2+line3+line4)

fout.close()



# Chapter 14.3
print('\n\nChapter 14.3 \n')

print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))



# Chapter 14.4
print('\n\nChapter 14.4 \n')

import os

cwd = os.getcwd()
print(cwd)
print(os.path.exists('output.txt'))
print(os.path.abspath('output.txt'))
print(os.path.isdir('output.txt'))
print(os.path.isdir('C:/Users\swisnoski\OneDrive - Olin College of Engineering\Freshman Semester 1\Python Passionate Pursuit'))
print(os.path.isfile('output.txt'))
print(os.listdir('C:/Users\swisnoski\OneDrive - Olin College of Engineering\Freshman Semester 1\Python Passionate Pursuit'))

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

walk('C:/Users\swisnoski\OneDrive - Olin College of Engineering\Freshman Semester 1\QEA 1\Homework')



# Chapter 14.5
print('\n\nChapter 14.5 \n')


try:
    fin = open('bad_file')
except:
    print('Something went wrong.')



# Chapter 14.6
print('\n\nChapter 14.6 \n')

import dbm

db = dbm.open('captions', 'c')
db['cheese.png'] = 'Photo of Big Cheesy.'
print(db['cheese.png'])
db['cheese.png'] = 'Photo of Big Cheesy doing a silly walk.'
print(db['cheese.png'])

for key in db.keys():
    print(key, db[key])

db.close()



# Chapter 14.7
print('\n\nChapter 14.7 \n')

import pickle


q = [1, 2, 3]
r = pickle.dumps(q)
print(r)
s = pickle.loads(r)
print(s)

print(q == s)
print(q is s)
# same value, DIFFERENT object



# Chapter 14.8
print('\n\nChapter 14.8 \n')

command = 'dir'
fp = os.popen(command)
print(fp)



# Chapter 14.9
print('\n\nChapter 14.9 \n')
 
import wc
wc.linecount('Think Python Chapter 14.py')



# Chapter 14.12
print('\n\nChapter 14.12 \n')


# Exercise 14.1
print('\n\nExercise 14.1 \n')


# First Attempt
def sed1(patstr, repstr, fl1, fl2 = 'created_file.txt'):

    with open(fl1) as f:
        fin = f.read().splitlines() 
    fout = open(fl2, 'w')

    check = []
    check2 = []
    check3 = []

    for i in fin:
        for letter in i:
            check.append(letter)

    for letter in patstr:
        check2.append(letter)

    for letter in repstr:
            check3.append(letter)

    for i in range(len(check)+50):
        if check[i:(i+len(patstr))] == check2:
            check[i:(i+len(patstr))] = check3


    fin = ''.join(check)

    print(check)

    for i in fin:
        fout.write(i)
    
# Second attempt w/ internet help
def sed(pattern, replacement, fl1, fl2 = 'created_file.txt'):
    try:
        with open(fl1, 'r') as source:
            content = source.read()
            modified_content = content.replace(pattern, replacement)

        fout = open(fl2, 'w')
        fout.write(modified_content)

        print("Replacement completed. Result written to " + str(fl2))
    except FileNotFoundError:
        print("File not found or unable to read/write the files.")

sed('Pasta', 'PAHHHSTA', 'PastaMasta.txt')



# Exercise 14.2
print('\n\nExercise 14.2 \n')

# Completed on seperate file



# Exercise 14.3
print('\n\nExercise 14.3 \n')


import hashlib

# I got the code for md5sum from the internet and only partially understand it 

def md5sum(path):
    md5_hash = hashlib.md5()

    p = open(path, 'rb')
    data = p.read(8192)

    md5_hash.update(data)
    return md5_hash.hexdigest()

def walk(dirname):
    file_list = []
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            file_list.append(path)
        else:
            j = walk(path)
            file_list.append(j[0])
    return file_list

def step1(direct):
    file_list = walk(direct)
    gist = []
    for i in file_list:
        if i.endswith('.txt'):
            gist.append(i)

    mlist = []
    for j in gist:
        if md5sum(j) in mlist:
            print(j + ' is a duplicate!')
        else:
            mlist.append(md5sum(j))

step1('C:/Users\swisnoski\OneDrive - Olin College of Engineering\Freshman Semester 1\Python Passionate Pursuit')

print('\n\n')


