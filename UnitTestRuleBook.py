from RuleBook import Rulebook
import unittest

class UnitTestRuleBook_CheckBust(unittest.TestCase):
    def test_check_bust_false(self):
        score = "20"
        self.assertFalse(Rulebook.check_bust(score))

    def test_check_bust_true(self):
        score = "22"
        self.assertTrue(Rulebook.check_bust(score))

    def test_check_bust_zero(self):
        score = "0"
        self.assertFalse(Rulebook.check_bust(score))

    def test_check_bust_ace_false(self):
        score = "15 or 25"
        self.assertFalse(Rulebook.check_bust(score))

    def test_check_bust_ace_true(self):
        score = "25 or 35"
        self.assertTrue(Rulebook.check_bust(score))

class UnitTestRuleBook_StringToScore(unittest.TestCase):
    #sts = string_to_score
    def test_sts_zero(self):
        self.assertEqual(0, Rulebook.string_to_score("0"))

    def test_sts_large_val(self):
        self.assertEqual(50, Rulebook.string_to_score("50"))

    def test_sts_ace_val(self):
        self.assertEqual(21, Rulebook.string_to_score("11 or 21"))

    def test_sts_ace_low_val(self):
        self.assertEqual(18, Rulebook.string_to_score("18 or 28"))

class UnitTestRuleBook_CheckPlayerWin(unittest.TestCase):
    #cpw = check_player_win
    def test_cpw_player_win(self):
        self.assertTrue(Rulebook.check_player_win("5", "21"))

    def test_cpw_player_not_win(self): #can be tie or loss.
        self.assertFalse(Rulebook.check_player_win("21", "10"))

    def test_cpw_player_tie(self):
        self.assertFalse(Rulebook.check_player_win("21", "21"))

    def test_cpw_player_win_ace(self):
        self.assertTrue(Rulebook.check_player_win("20", "11 or 21"))

class UnitTestRuleBook_CheckDealerWin(unittest.TestCase):
    #cdw = check_dealer_hit
    def test_cdw_player_win(self):
        self.assertTrue(Rulebook.check_dealer_win("21", "2"))

    def test_cdw_player_not_win(self): #can be tie or loss.
        self.assertFalse(Rulebook.check_dealer_win("2", "10"))

    def test_cdw_player_tie(self):
        self.assertFalse(Rulebook.check_dealer_win("21", "21"))

    def test_cdw_player_win_ace(self):
        self.assertTrue(Rulebook.check_dealer_win("11 or 21", "11"))

class UnitTestRuleBook_CheckDealerHit(unittest.TestCase):
    #cdh = check_dealer_hit
    def test_cdh_dealer_hit(self):
        self.assertTrue(Rulebook.check_dealer_hit("15"))

    def test_cdh_dealer_not_hit(self):
        self.assertFalse(Rulebook.check_dealer_hit("17"))

    def test_cdh_dealer_hit_ace(self):
        self.assertTrue(Rulebook.check_dealer_hit("3 or 13"))

    def test_cdh_dealer_not_hit_ace(self):
        self.assertFalse(Rulebook.check_dealer_hit("10 or 20"))

class UnitTestRuleBook_CheckHandValue(unittest.TestCase):
    def test_chv(self):
        self.assertEqual(Rulebook.check_hand_value(['3', '5']), "8")

    def test_chv_ace(self):
        self.assertEqual(Rulebook.check_hand_value(['3', 'A']), "4 or 14")

    def test_chv_hidden_card(self):
        self.assertEqual(Rulebook.check_hand_value(['3', '6'], True), "6")

    def test_chv_hidden_ace(self):
        self.assertEqual(Rulebook.check_hand_value(['A', '6'], True), "6")

    def test_chv_shown_ace(self):
        self.assertEqual(Rulebook.check_hand_value(['3', 'A'], True), "1 or 11")


if __name__ == "__main__":
    unittest.main()