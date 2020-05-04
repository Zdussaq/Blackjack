from Dealer import Dealer
import unittest

class UnitTestDealer_DealHand(unittest.TestCase):
    def setUp(self):
        self.dealer = Dealer()

    def test_succsesful_deal(self):
        self.dealer.deal_hand()
        self.assertEqual(len(self.dealer.cards), 2)
        #do not check the player card count here because that belongs in the integration tests

if __name__ == '__main__':
    unittest.main()