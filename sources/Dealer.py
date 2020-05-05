from Deck import Deck
from Player import Player
from ModelView import ModelView
from RuleBook import Rulebook
import string
import random

class Dealer:
    def __init__(self):
        self.deck = Deck()
        #instantiate player and dealer deck
        self.player = Player()
        self.cards = []
        self.hand_hidden = True
        
    def play(self):
        if self.deck.cards_remaining() < 26:
            self.deck.reshuffle_deck()
        self.deal_hand()
        self.update_view()
        self.get_player_move()
        self.hand_hidden = True
        self.make_dealer_move()
        self.end_hand()
        self.get_continue()

    def get_continue(self):
        print("Play Again? [Y/N]")
        option = input()
        if option.upper() == "Y":
            self.play()

    def get_player_move(self):
        print("Hit? [Y/N]")
        option = input()
        if option.upper() == "Y":
            self.player.add_card(self.deck.draw_card())
            if not Rulebook.check_bust(Rulebook.check_hand_value(self.player.get_cards())):
                self.update_view()
                self.get_player_move()
            else:
                self.end_hand()

    def update_view(self, custom_message=""):
        ModelView.update_view(self.cards, self.player.get_cards(),
                                Rulebook.check_hand_value(self.cards, self.hand_hidden),
                                Rulebook.check_hand_value(self.player.get_cards()),
                                self.hand_hidden, custom_message)

    def make_dealer_move(self):
        if len(self.cards) == 0:
            return
        if Rulebook.check_dealer_hit(Rulebook.check_hand_value(self.cards)):
            self.cards.append(self.deck.draw_card())
            if Rulebook.check_bust(Rulebook.check_hand_value(self.cards)):
                self.end_hand()
                return
            self.update_view()
            self.make_dealer_move()

    def deal_hand(self):
        self.hand_hidden = True
        for _ in range(2):
            self.player.add_card(self.deck.draw_card())
            self.cards.append(self.deck.draw_card())

    def end_hand(self):
        if len(self.cards) == 0:
            return
        self.hand_hidden = False
        message = ""

        #case for player bust:
        if Rulebook.check_bust(Rulebook.check_hand_value(self.player.get_cards())):
            message = "Player busts! Dealer wins."
        #case for dealer bust:
        elif Rulebook.check_bust(Rulebook.check_hand_value(self.cards)):
            message = "Dealer busts! Player wins."
        #case for player beating dealer:
        elif Rulebook.check_player_win(Rulebook.check_hand_value(self.cards),
                                        Rulebook.check_hand_value(self.player.get_cards())):
            message = "Player wins!"
        #case for dealer beating player:
        elif Rulebook.check_dealer_win(Rulebook.check_hand_value(self.cards),
                                        Rulebook.check_hand_value(self.player.get_cards())):
            message = "Dealer wins!"
        #case for tie
        else:
            message = "Tie!"

        self.update_view(message)

        #Reset cards
        self.cards = []
        self.player.collect_cards()
        
if __name__=='__main__':
    dealer = Dealer()
    dealer.play()