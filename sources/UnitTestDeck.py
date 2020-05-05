from Deck import Deck
import unittest

class UnitTestDeck_DrawCard(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        return super().setUp()

    def test_draw_card(self):
        result = self.deck.draw_card()
        self.assertEqual(type(result), str)
    
    def test_draw_all_cards(self):
        for i in range(52):
            self.deck.draw_card()

        with self.assertRaises(IndexError): self.deck.draw_card()

class UnitTestDeck_ReshuffleDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        return super().setUp()

    def test_reshuffle_deck(self):
        self.deck.draw_card()
        self.deck.reshuffle_deck()
        self.assertEqual(self.deck.cards_remaining(), 52)

    def test_reshuffle_full_deck(self):
        self.deck.reshuffle_deck()
        self.assertEqual(self.deck.cards_remaining(), 52)

    def test_reshuffle_empty_deck(self):
        for i in range(52):
            self.deck.draw_card()
        self.deck.reshuffle_deck()
        self.assertEqual(self.deck.cards_remaining(), 52)

class UnitTestDeck_CardsRemaining(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        return super().setUp()

    def test_full_deck(self):
        self.assertEqual(self.deck.cards_remaining(), 52)

    def test_partial_deck(self):
        self.deck.draw_card()
        self.deck.draw_card()
        self.deck.draw_card()
        self.assertEqual(self.deck.cards_remaining(), 49)

    def test_empty_deck(self):
        for i in range(52):
            self.deck.draw_card()
        self.assertEqual(self.deck.cards_remaining(), 0)

if __name__ == '__main__':
    unittest.main()