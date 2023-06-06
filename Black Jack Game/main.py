import random

class Card:
    def __init__(self):
        

class Deck:
    def __init__(self):
        suits = ["spades", "clubs", "hearts", "daimonds"]
        ranks = [{"rank" : "A", "value" : 11}, {"rank" : "2", "value" : 2},{"rank" : "3", "value" : 3},{"rank" : "4", "value" : 4},{"rank" : "5", "value" : 5},{"rank" : "6", "value" : 6},{"rank" : "7", "value" : 7},{"rank" : "8", "value" : 8},{"rank" : "9", "value" : 9},{"rank" : "10", "value" : 10},{"rank" : "J", "value" : 10},{"rank" : "Q", "value" : 10},{"rank" : "K", "value" : 10}]
        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append([suit, rank])

    def shuffle(self): 
        if len(self.cards)>1:
            random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.card)>0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

deck1 = Deck()    
deck2 = Deck()
deck2.shuffle()
print(deck2.cards)
