import random

class Deck:
    def __init__(self):
        #Because suit doesn't matter in blackjack - it is kept out for simplicity.
        self.__cards = [
            'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
            'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
            'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
            'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
        ]

    #Will return one random card from the deck
    def draw_card(self) -> str:
        if len(self.__cards) == 0:
            raise IndexError("Out of cards!")
        return self.__cards.pop(random.randint(0, len(self.__cards) - 1))
        
    #Returns number of cards currently in the deck
    def cards_remaining(self) -> int:
        return len(self.__cards)

    def reshuffle_deck(self):
        #Because suit doesn't matter in blackjack - it is kept out for simplicity.
        self.__cards = [
            'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
            'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
            'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
            'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
        ]