from typing import List

class Rulebook:
    #returns true if value is over 21
    @staticmethod
    def check_bust(score : str) -> bool:
        if "or" in score:
            handValues = score.split(" or ")
            if int(handValues[0]) > 21:
                return True
            else:
                return False
        elif int(score) > 21:
            return True
        return False

    @staticmethod
    def string_to_score(score : str) -> int:
        if "or" in score:
            handValues = score.split(" or ")
            if int(handValues[1]) > 21:
                return int(handValues[0])
            else:
                return int(handValues[1])
        return int(score)

    @staticmethod
    def check_player_win(dealer_score : str, player_score : str):
        if (Rulebook.string_to_score(dealer_score) < 
            Rulebook.string_to_score(player_score)):
            return True
        return False

    @staticmethod
    def check_dealer_win(dealer_score : str, player_score : str):
        if (Rulebook.string_to_score(dealer_score) > 
            Rulebook.string_to_score(player_score)):
            return True
        return False   

    @staticmethod
    def check_dealer_hit(score : str) -> bool:
        if Rulebook.string_to_score(score) > 16:
            return False
        return True

    @staticmethod
    def check_hand_value(cards : List[str], dealer_card_hidden = False) -> str:
        ace_low_val = 0
        ace_high_val = 0
        for i in range(len(cards)):
            if i == 0 and dealer_card_hidden:
                continue
            elif cards[i] == 'A':
                ace_high_val += 11
                ace_low_val += 1
            elif cards[i] == 'J':
                ace_high_val += 10
                ace_low_val += 10
            elif cards[i] == 'Q':
                ace_high_val += 10
                ace_low_val += 10
            elif cards[i] == 'K':
                ace_high_val += 10
                ace_low_val += 10
            elif cards[i] == 'J':
                ace_high_val += 10
                ace_low_val += 10
            else:
                parseVal = int(cards[i])
                if (parseVal < 2 or parseVal > 10):
                    raise ValueError("Bad or inccorect card value passed.")
                ace_high_val += parseVal
                ace_low_val += parseVal
        if ace_high_val is not ace_low_val:
            return str(ace_low_val) + " or " + str(ace_high_val)
        return str(ace_low_val)