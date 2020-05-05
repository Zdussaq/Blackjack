from typing import List

class ModelView:
    @staticmethod
    def update_view(dealer_hand : List[int], player_hand : List[int],
                    dealer_score : str, player_score : str,
                    dealer_hand_hidden = True, custom_message = ""):
        deal_len = len(dealer_hand)
        print("--------------------- Dealer Hand ---------------------", flush=True)
        print("Dealer Score: " + dealer_score)
        printstr = ""
        for i in range(deal_len):
            printstr += "-----  "
        print(printstr)
        printstr = ""
        for i in range(deal_len):
            printstr += "|   |  "
        print(printstr)
        printstr = ""
        for i in range(deal_len):
            if i == 0 and dealer_hand_hidden:
                printstr += "|   |  "
            else:
                printstr += "| " + str(dealer_hand[i]) + " |  "
        print(printstr)
        printstr = ""
        for i in range(deal_len):
            printstr += "|   |  "
        print(printstr)
        printstr = ""
        
        for i in range(deal_len):
            printstr += "-----  "
        print(printstr)
        printstr = ""
            
        print("--------------------- Player Hand ---------------------")
        print("Player Score: " + player_score)
        play_len = len(player_hand)
        printstr = ""
        for i in range(play_len):
            printstr += "-----  "
        print(printstr)
        printstr = ""
        for i in range(play_len):
            printstr += "|   |  "
        print(printstr)
        printstr = ""
        for i in range(play_len):
            printstr += "| " + str(player_hand[i]) + " |  "
        print(printstr)
        printstr = ""
        for i in range(play_len):
            printstr += "|   |  "
        print(printstr)
        printstr = ""
        for i in range(play_len):
            printstr += "-----  "
        print(printstr)
        print(custom_message)
        