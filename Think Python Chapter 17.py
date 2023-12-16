# Sam Wisnoski
# 11/21/2023
# Think Python Chapter 17

import copy

# Chapter 17.2
print('\n\nChapter 17.2 \n')


def print_time(t):   # This is a FUNCTION
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


class Time:   # This is a CLASS
    """Represents the time of day.

    attributes: hour, minute, second
    """
    def time_to_int(self):  # This is a METHOD
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    def incrementgood(self, seconds):
        self2 = copy.deepcopy(self)
        self2.second += seconds

        self2.minute += self2.second/60 - self2.second%60/60
        self2.second = self2.second%60

        self2.hour += self2.minute/60 - self2.minute%60/60
        self2.minute = self2.minute%60

        if self2.hour>12:
            self2.hour = self2.hour%12
        return self2
    def is_after(self, other):
        print("Self time:", self.time_to_int())
        print("Other time:", other.time_to_int())
        return self.time_to_int() > other.time_to_int()
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def print_time(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    def __radd__(self, other):
        return self.__add__(other)


        # Use self for methods because conventions idk who knows why


start2 = Time()
start2.hour = 11
start2.minute = 59
start2.second = 31

Time.print_time(start2)  # This is dot notation, work with any object that has the correct atributes
start2.print_time() #This is method syntax, only works since start2 is a instance of Time

print(start2.time_to_int())



# Chapter 17.3
print('\n\nChapter 17.3 \n')

start2.print_time()
end = start2.incrementgood(333) # The object gets assigned to the fist parameter, while the argument gets assigned to the second
end.print_time()


# Chapter 17.4
print('\n\nChapter 17.4 \n')

print(end.is_after(start2))



# Chapter 17.5
print('\n\nChapter 17.5 \n')

time = Time()
time.print_time()
time = Time(9,49,10)
time.print_time()




# Chapter 17.6
print('\n\nChapter 17.6 \n')

print(time) # No longer need print_time!!


class Point:
    """Represents a point in 2-D space."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(%d,%d)' % (self.x, self.y)
    def __add__(self, other):
        self2 = copy.deepcopy(self)
        self2.x += other.x
        self2.y += other.y
        return self2
    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)
    def add_point(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    def add_tuple(self, tuple):
        x = self.x + tuple[0]
        y = self.y + tuple[1]
        return Point(x,y)
    def __radd__(self, other):
        return self.__add__(other)

    
point = Point(5,7)
print(point)



# Chapter 17.7
print('\n\nChapter 17.7 \n')

start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)  #Using the __add__ method and the __str__ method

point1 = Point(5,1)
point2 = Point(7,19)
print(point1 + point2)



# Chapter 17.8
print('\n\nChapter 17.8 \n')

print(start + duration)
print(start + 1337)
print(1337 + start)

print(point1 + point2)
print(point1 + (11,67))
print((11,67) + point1)



# Chapter 17.13
print('\n\nChapter 17.13 \n')


# Exercise 17.1
print('\n\nExercise 17.1 \n')


def int_to_time_seconds(seconds):
    second = TimeSeconds(seconds)
    return second


class TimeSeconds:   # This is a CLASS
    """Represents the time of day in seconds since midnight.

    attributes: second
    """
    def __init__(self, second=0):
        self.second = second
    def __str__(self):
        if self.second>43200:
            self.second = self.second%43200
        hour = self.second//3600
        minute = (self.second%3600) //60
        second = self.second % 60 
        return '%.2d:%.2d:%.2d' % (hour, minute, second)
    def incrementgood(self, seconds):
        self2 = copy.deepcopy(self)
        self2.second += seconds
        if self2.second>43200:
            self2.second = self2.second%43200
        return self2
    def is_after(self, other):
        print("Self time:", self.second)
        print("Other time:", other.second)
        return self.second > other.second
    def __add__(self, other):
        if isinstance(other, TimeSeconds):
            return self.add_time(other)
        else:
            return self.increment(other)
    def add_time(self, other):
        seconds = self.second + other.second
        return int_to_time_seconds(seconds)
    def increment(self, seconds):
        seconds += self.second
        return int_to_time_seconds(seconds)
    def __radd__(self, other):
        return self.__add__(other)


seconds_since_midnight = TimeSeconds(12345)
seconds_since_midnight_late = TimeSeconds(32123)
print(seconds_since_midnight)
print(seconds_since_midnight_late)
print(seconds_since_midnight.incrementgood(12345))
print(seconds_since_midnight.is_after(seconds_since_midnight_late))

print(seconds_since_midnight_late+seconds_since_midnight)
print(seconds_since_midnight+ 1337)
print(1337 + seconds_since_midnight)



# Exercise 17.2
print('\n\nExercise 17.2 \n')

class Kangaroo:   # This is a CLASS

    def __init__(self, pouch_contents=[]):
        self.pouch_contents = pouch_contents
    def put_in_pouch(self, other):
        self.pouch_contents.append(other)
    def __str__(self):
        return f'Kangaroo with pouch contents: {self.pouch_contents}'
    
kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch(roo)
print(kanga)
print(roo)
