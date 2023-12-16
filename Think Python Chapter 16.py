# Sam Wisnoski
# 11/20/2023
# Think Python Chapter 16


# Chapter 16.1
print('\n\nChapter 16.1 \n')

class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time2 = Time()
time2.hour = 10
time2.minute = 59
time2.second = 30


def print_time(t):
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))

print_time(time)
print_time(time2)

def is_after(t1,t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

print(is_after(time,time2))



# Chapter 16.2
print('\n\nChapter 16.2 \n')

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
print_time(done)



# Chapter 16.3
print('\n\nChapter 16.3 \n')

def incrementbad(time, seconds):
    time.second += seconds
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1


def incrementgood(time, seconds):
    time.second += seconds

    time.minute += time.second/60 - time.second%60/60
    time.second = time.second%60

    time.hour += time.minute/60 - time.minute%60/60
    time.minute = time.minute%60

    if time.hour>12:
       time.hour = time.hour%12


print_time(time)
incrementgood(time,9045)
print_time(time)



# Chapter 16.7
print('\n\nChapter 16.7 \n')

# Exercise 16.1
print('\n\nExercise 16.1 \n')

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def mul_time(t,num):
    seconds = time_to_int(t)*num
    return int_to_time(seconds)

def pace(finish, dist):
    return mul_time(finish,1/dist)

print_time(time)
print_time(mul_time(time,2))
print_time(pace(time,26.3))



# Exercise 16.2
print('\n\nExercise 16.2 \n')

import datetime

now = datetime.datetime.now()
date, time = now.date(), now.time()
print(date)

def weekday():
    y = datetime.datetime.today().weekday()
    if y == 0:
        print('Sunday')
    if y == 1:
        print('Monday')
    if y == 2:
        print('Tuesday')
    if y == 3:
        print('Wednesday')
    if y == 4:
        print('Thursday')
    if y == 5:
        print('Friday')
    if y == 6:
        print('Saturday')

weekday()

def birthday_countdown():
    # get user birthday
    birthday = [2005,12,25]#input('\n\nEnter your Birthday in YYYY-MM-DD format: ').split('-')
    if len(birthday) is not 3:
        print('Entry invalid, please input birthday correctly')
        return
    now = datetime.datetime.now(); 

    n = 1
    age = now.year - int(birthday[0]) 
    if  ((now.month, now.day) < (int(birthday[1]), int(birthday[2]))):
        age -= 1
        n = 0
    print("\nYour age is: ", age, ' years')

    next_birthday = datetime.datetime(now.year+n, int(birthday[1]), int(birthday[2])) - now
    hours = next_birthday.seconds//3600
    minutes = (next_birthday.seconds % 3600) // 60
    seconds = next_birthday.seconds % 60

    print('\nYour next birthday is in ', next_birthday.days, ' days ', hours, ' hours ', minutes, ' minutes ', seconds, ' seconds ')


birthday_countdown()
    

birthdaysam = '2005-03-02'
birthdaydave = '1974-05-16'

def doubleday (bday1, bday2):
    bday1 = bday1.split('-');bday2 = bday2.split('-')
    bday1 = datetime.datetime(int(bday1[0]), int(bday1[1]), int(bday1[2]))
    bday2 = datetime.datetime(int(bday2[0]), int(bday2[1]), int(bday2[2]))
    if bday1>bday2:
        diff = bday1-bday2
        doubleday = bday1+diff
    else:
        diff = bday2-bday1
        doubleday = bday2+diff

    print('\nYour double day is: ',  doubleday.date(),'\n')


doubleday(birthdaysam,birthdaydave)