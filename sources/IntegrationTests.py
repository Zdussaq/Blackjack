import unittest
from Dealer import Dealer

#Dealer will be entry point for integration tests
#Top down approach used here.
class DealerEntryIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.dealer = Dealer()

    def test_player_card_addition(self):
        """This test will ensure that the dealer properly deals to the player"""
        self.dealer.deal_hand()
        self.assertEqual(self.dealer.player.get_number_cards(), 2)

    def test_end_hand_resets_cards(self):
        """This will ensure that when the game is wrapped up, 
        the player hand is properly cleared by the dealer."""
        self.dealer.deal_hand()
        self.dealer.end_hand()
        self.assertEqual(self.dealer.player.get_number_cards(), 0)
    
# There isn't much in terms of integration tests here as I don't have a lot of interaction between each class
# Certainly data isn't touched much between them save for the dealer interacting with and altering the Player's cards
# I feel as though more could have existed has I created a class higher than the dealer and had things more layered.
# The big mistake I made was creating the code without the thought of creating integration tests and instead just creating
# a simple OOP. 

if __name__ == "__main__":
    unittest.main()