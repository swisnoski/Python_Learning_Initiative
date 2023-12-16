# Sam Wisnoski
# 11/26/2023
# Think Python Chapter 18 Exercise 3

from __future__ import print_function, division

from Card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        pairs = []
        for val in self.ranks.values():
            if val >= 2:
                pairs.append(val)
        if len(pairs) >= 1:
            return True
        return False
    
    def has_two_pair(self):
        """Returns True if the hand has two pair, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        pairs = []
        for val in self.ranks.values():
            if val >= 2:
                pairs.append(val)
        if len(pairs) >= 2:
            return True
        return False
    
    def has_three_of_a_kind(self):
        """Returns True if the hand has a three of a kind, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        threes = []
        for val in self.ranks.values():
            if val >= 3:
                threes.append(val)
        if len(threes) >= 1:
            return True
        return False
    
    def has_four_of_a_kind(self):
        """Returns True if the hand has a four of a kind, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        pairs = []
        for val in self.ranks.values():
            if val >= 4:
                pairs.append(val)
        if len(pairs) >= 1:
            return True
        return False
    
    def has_full_house(self):
        """Returns True if the hand has a full house, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        threes = []
        twos = []
        for val in self.ranks.values():
            if val == 3:
                threes.append(val)
            if val == 2:
                twos.append(val)
        if len(threes) >= 1 and len(twos) >= 1:
            return True
        return False
    
    def has_straight(self):
        """Returns True if the hand has a straight, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        keys = []
        for key in self.ranks.keys():
            keys.append(key)
            if key == 1:
                keys.append(14)
        keys.sort()
        count = 1
        for i in range(1, len(keys)):
            if keys[i] - keys[i - 1] == 1:
                self.cards[i-1].suit
                count += 1
                if count >= 5:
                    return True 
            else:
                count = 1  
        return False
    
    def has_straight_flush(self):
        """Returns True if the hand has a straight flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        self
        keys = []
        for key in self.ranks.keys():
            keys.append(key)
            if key == 1:
                keys.append(14)
        keys.sort()
        count = 1
        for i in range(1, len(keys)):
            if keys[i] - keys[i - 1] == 1:
                count += 1
                if count >= 5:
                    if self.cards[i].suit == self.cards[i-1].suit == self.cards[i-2].suit == self.cards[i-3].suit == self.cards[i-4].suit:
                        return True 
            else:
                count = 1  
        return False
    def classify(self):
        if self.has_straight_flush():
            return 'Straight Flush'
        if self.has_four_of_a_kind():
            return "Four of a Kind"
        if self.has_full_house():
            return "Full House"
        if self.has_flush():
            return "Flush"
        if self.has_straight():
            return "Straight"
        if self.has_three_of_a_kind():
            return "Three of a Kind"
        if self.has_two_pair():
            return "Two Pair"
        if self.has_pair():
            return "Pair"
        return "High Card"



if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print(hand.classify())
        print('')

