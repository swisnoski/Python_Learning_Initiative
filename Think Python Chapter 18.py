# Sam Wisnoski
# 11/26/2023
# Think Python Chapter 18

import random 

# Chapter 18.1
print('\n\nChapter 18.1 \n')

class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
    
    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False
        # suits are the same... check ranks
        return self.rank < other.rank




# Chapter 18.2
print('\n\nChapter 18.2 \n')

queen_of_diamonds = Card(1, 12)
jack_of_hearts = Card(2,11)
print(jack_of_hearts)



# Chapter 18.3
print('\n\nChapter 18.3 \n')

# Practising modifying the time class with lt 
'''
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
    def __lt__ (self,other):
        t1 = (self.hour, self.minute, self.second)
        t2 = (other.hour, other.minute, other.second)
        return t1<t2
'''
    
print(queen_of_diamonds.__lt__(jack_of_hearts))



# Chapter 18.4
print('\n\nChapter 18.4 \n')

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):   # This "deals" a card from the bottom of the deck
        return self.cards.pop()
    def add_card(self, card):   # This adds a card to the bottom of the deck
        self.cards.append(card)
    def shuffle(self):   # And this card shuffles the deck 
        random.shuffle(self.cards)
    def sort(self):
        self.cards.sort()
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
    def deal_hands(self, numhands, numbercards):
        list_of_hands = []
        for i in range(numhands):
            t = ('Hand',str(i+1))
            name = ' '.join(t)
            hand = Hand(name)
            self.move_cards(hand, numbercards)
            list_of_hands.append(hand)
        return list_of_hands






# Chapter 18.5
print('\n\nChapter 18.5 \n')

deck = Deck()
print(deck, '\n\n\n')



# Chapter 18.6
print('\n\nChapter 18.6 \n')

deck.shuffle()
print(deck, '\n\n\n')
deck.sort()
print(deck)



# Chapter 18.7
print('\n\nChapter 18.7 \n')

class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


hand = Hand('new hand')
print(hand.cards)
print(hand.label)

deck.shuffle()
card = deck.pop_card()
hand.add_card(card)
print(hand)
print('\n\n')

deck.move_cards(hand, 6)
hand.sort()
print(hand)



# Chapter 18.12
print('\n\nChapter 18.12 \n')


# Exercise 18.1
print('\n\nExercise 18.1 \n')

'''
- Pong HAS-A list of pings
- Ping HAS-A pong
- Ping IS-A kind of PingPongParent
- Pong IS-A kind of PingPongParent
- Ping has dependancy with Pong (__init__)
- Pong has dependancy with Ping (add_ping)
'''



# Exercise 18.2
print('\n\nExercise 18.2 \n')

# Added the "deal-hands" method in deck 

newdeck = Deck()
newdeck.shuffle()
for i in newdeck.deal_hands(7,7):
    print(i)
    print('')




# Exercise 18.3
print('\n\nExercise 18.3 \n')

#completed in seperate code