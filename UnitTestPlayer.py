from Player import Player
import unittest

class UnitTestPlayer_AddCard(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        return super().setUp()
        
    def test_add_card_empty_hand(self):
        self.player.add_card('2')
        self.player.add_card('2')
        self.assertEqual(self.player.get_number_cards(), 2)

    def test_add_many_cards(self):
        for _ in range(100):
            self.player.add_card('2')

class UnitTestPlayer_get_cards(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.player.add_card('5')
        self.player.add_card('5')
        return super().setUp()
        
    def test_get_cards(self):
        self.assertEqual(['5', '5'], self.player.get_cards())

    def test_get_empty_cards(self):
        self.player.collect_cards()
        self.assertEqual([], self.player.get_cards())

class UnitTestPlayer_CollectCards(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        return super().setUp()

    def test_collect_cards(self):
        self.player.add_card('2')
        self.player.collect_cards()
        self.assertEqual(self.player.get_cards(), [])

    def test_collect_cards_empty(self):
        self.player.collect_cards()
        self.assertEqual(self.player.get_cards(), [])

class UnitTestPlayer_GetNumberCards(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        return super().setUp()

    def test_collect_cards(self):
        self.player.add_card('2')
        self.player.collect_cards()
        self.assertEqual(self.player.get_cards(), [])

    def test_collect_cards_empty(self):
        self.player.collect_cards()
        self.assertEqual(self.player.get_cards(), [])

if __name__ == "__main__":
    unittest.main()