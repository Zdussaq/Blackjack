from RuleBook import Rulebook

class Player:
    def __init__(self):
        self.__cards = []

    def add_card(self, card : str):
        self.__cards.append(card)

    def get_cards(self):
        return self.__cards

    def get_score(self):
        return Rulebook.check_hand_value(self.get_cards())

    def collect_cards(self):
        self.__cards = []

    def get_number_cards(self):
        return len(self.__cards)