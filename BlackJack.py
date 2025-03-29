#############################################################################
# Copyright © 2024 Daniel Smith                                             #               
#                                                                           #
#                                                                           #
# Licensed under the Apache License, Version 2.0 (the "License");           #
# you may not use this file except in compliance with the License.          #
# You may obtain a copy of the License at                                   #
#                                                                           #
#     http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                           #
# Unless required by applicable law or agreed to in writing, software       #
# distributed under the License is distributed on an "AS IS" BASIS,         #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
# See the License for the specific language governing permissions and       #
# limitations under the License.                                            #
#############################################################################


import random

class Card:
    def __init__(self, s, r):
        self.suit = s
        self.rank = r


    def get_suit_as_string(self):
        if self.suit == 1:
            return "D"
        elif self.suit == 2:
            return "C"
        elif self.suit == 3:
            return "H"
        elif self.suit == 4:
            return "S"
        else:
            return "Invalid Suit"

    def get_rank_as_string(self):
        if self.rank == 1:
            return "A"
        elif self.rank == 11:
            return "J"
        elif self.rank == 12:
            return "Q"
        elif self.rank == 13:
            return "K"
        else:
            return str(self.rank)

    def get_card_as_string(self):
        string_rank = self.get_rank_as_string()
        string_suit = self.get_suit_as_string()
        string_card = string_rank + string_suit
        return string_card

    def get_score(self):
        score = 0
        if self.rank < 11 and self.rank > 1:
            score = self.rank
        elif self.rank == 1:
            score = 11
        elif self.rank == 11 or self.rank == 12 or self.rank == 13:
            score = 10
            
        return score

    

class Player:
    def __init__(self, h, i, start_cash):
        self.id_code = i
        self.hand = h
        self.score = 0
        self.cash = start_cash
        
    def draw_card(self, card):
        self.hand.append(card)

    def get_hand(self):
        # Returns a sting that shows the players hand
        string = "Hand: "
        for i in range(len(self.hand)):
            card = self.hand[i]
            string = string + card.get_card_as_string()
            if i < (len(self.hand) - 1):
                string = string + " , "
        return string

    def get_first_hand_card(self):
        # Method only used for the dealer, so players know the face up card of the dealer
        string = "Dealer: "
        card = self.hand[0]
        string = string + card.get_card_as_string()
        return string

    def get_hand_value(self):
        value = 0
        #Sum up all the values of the cards
        for i in range(0, len(self.hand)):
            card = self.hand[i]
            value += card.get_score()
        #Check for aces if the total is too high (if player has ace, ace is counted as one instead of eleven

        if value > 21:
            for i in range(0, len(self.hand)):
                card = self.hand[i]
                #Only true if card is an ace. Reduce total by ten
                if card.get_score() == 11:
                    value -= 10;
                    
        return value

    def get_id(self):
        return self.id_code


def clear():
    print("\n\n\n\n\n\n\n")

def print_with_wrap(text):
    for i in range(len(text)// 21 + 1):
        substring = text[(21 * i):(21 * i)+21]
        print(substring)

def display_instructions():
    print_with_wrap("How to play Blackjack")
    print_with_wrap("The computer will    play as the dealer")
    input("EXE to continue: ")
    clear()
    print_with_wrap("You will all be delt a starting hand of   two cards")
    input("EXE to continue: ")
    clear()
    print_with_wrap("You will be able to  see the dealers firstcard but one of her  cards will remain    hidden")
    input("EXE to continue: ")
    clear()
    print_with_wrap("You can either draw  an additional card,  or stop drawing cardsand hold")
    input("EXE to continue: ")
    clear()
    print_with_wrap("Get as close to 21 aspossible")
    print_with_wrap("If you go over 21 youlose")
    input("EXE to continue: ")
    clear()
    print_with_wrap("Values are as follows")
    input("EXE to continue: ")
    clear()
    print_with_wrap("1-10 Card Rank")
    input("EXE to continue: ")
    clear()
    print_with_wrap("Jack Queen & King 10")
    input("EXE to continue: ")
    clear()
    print_with_wrap("Ace 11, unless being eleven puts you over 21, in which case it becomes 1")
    input("EXE to continue: ")
    clear()

def get_int_input(message):
    print_with_wrap(message)
    valid_input = False
    while not valid_input:
        try:
           user_input = int(input())
           valid_input = True
        except ValueError:
            print_with_wrap("Invalid Input")

    return user_input

def shuffle_deck(deck):
    print_with_wrap("Shuffling Deck...")
    for i in range(len(deck) - 1):
        card_to_swap = random.randint(i + 1, len(deck) - 1)
        temp = deck[card_to_swap]
        deck[card_to_swap] = deck[i]
        deck[i] = temp

        
        
def main():    
    deck = []
    run_program = True
    play_game = False
    number_of_cards_drawn = 0;
    
    #Create the deck
    print_with_wrap("Generating Deck...")
    for suit in range(1, 5):
        for rank in range(1, 14):
            card = Card(suit, rank)
            deck.append(card)

    
    shuffle_deck(deck)
        
    while (run_program):
        clear()
        print_with_wrap("Welcome to Blackjack Press 1 to play 2 to see the instructions 3 to exit: ")
        user_response = input()
        clear()
        if user_response == "1":
            play_game = True
        elif user_response == "2":
            display_instructions()
        elif user_response == "3":
            run_program = False
        else:
            print_with_wrap("Invalid Response \n")
            
        
        while (play_game == True):
            ##GAME SETUP##
            
            #Determine how amny players and create the player objects for each
            number_of_players = 0
            while number_of_players < 1 or number_of_players > 10:
                number_of_players = get_int_input("Enter the number of  players that want to play (1-10)")
                clear()

            #Shuffles cards if there is less than 4 cards per player
            if number_of_cards_drawn > (len(deck) - (4 * (number_of_players + 1))):
                shuffle_deck(deck)
                number_of_cards_drawn = 0;
            
            #Deal two starting cards to the players and dealer (player id 0 denotes the dealer)
            print_with_wrap("Dealing Cards...\n\n")
            players = []
            for i in range(number_of_players + 1):
                # Creates a player and gives them two cards, and id number (i) and £500 starting cash (not included in current version)
                player = Player([deck[number_of_cards_drawn], deck[number_of_cards_drawn + 1]], i, 500);
                players.append(player)
                number_of_cards_drawn += 2



            ##GAME PLAYING##
            print("\n----------------------\n")
            number_of_players_bust = 0
            
            #Runs the loop for every player
            for i in range(1, len(players)):

                player = players[i]
                clear()
                print_with_wrap("Pass the calculator  to player " + str(player.get_id()))
                print_with_wrap("EXE to continue: ")
                input()
                clear()
                print_with_wrap("Player " + str(player.get_id()) + "'s turn ")
                print_with_wrap((players[0]).get_first_hand_card() + " , ??")
                
                player_done = False
                
                #Runs until the player stops drawing or goes over 21
                while player_done == False:
                    print_with_wrap(player.get_hand())
                    print_with_wrap("Hand Value: " + str(player.get_hand_value()))
                    print_with_wrap("1 to draw 2 to hold:")
                    user_response = input()
                    clear()
                    if user_response == "1":
                        card = deck[number_of_cards_drawn]
                        print_with_wrap("You drew a " + card.get_card_as_string())
                        player.draw_card(card)
                        number_of_cards_drawn += 1
                        
                    elif user_response == "2":
                        player_done = True
                        
                    else:
                        print_with_wrap("Invalid input")


                    if player.get_hand_value() > 21:
                        print_with_wrap("You went bust!")
                        player_done = True
                        number_of_players_bust += 1

                    if player_done == True:
                        print_with_wrap("EXE to continue to the next player")
                        input()
                        clear()

            #Dealer's turn
            print_with_wrap("Dealer's turn ")
            player = players[0]
            print_with_wrap(player.get_hand())
            print_with_wrap("\nDealer: " + str(player.get_hand_value()))
            dealer_hand_value = 0
            dealer_won = False
            
            print_with_wrap("EXE to contine")
            input()
            clear()

            if number_of_players_bust == len(players) - 1:
                dealer_won = True
                print_with_wrap("All players are bust!")
            

            if dealer_won == False:
                #Dealer must draw cards until their total is at least 17
                while player.get_hand_value() < 17:
                    card = deck[number_of_cards_drawn]
                    print_with_wrap("Dealer Draw: " + card.get_card_as_string())
                    player.draw_card(card)
                    print_with_wrap("Dealer Hand: " + str(player.get_hand_value()))
                    print_with_wrap("EXE to contine")
                    input()
                    clear()
                    number_of_cards_drawn += 1

                if player.get_hand_value() > 21:
                    print_with_wrap("The dealer went bust!")
                else:
                    dealer_hand_value = player.get_hand_value()


            #Determine which player has won
            winning_players = []
            highest_hand_value = 0

            for i in range(len(players)):
                player = players[i]
                player_hand_value = player.get_hand_value()
                if player_hand_value <= 21:
                    if player_hand_value > highest_hand_value:
                        winning_players = [player]
                        highest_hand_value = player_hand_value
                    elif player_hand_value == highest_hand_value:
                        winning_players.append(player)

            if dealer_hand_value >= highest_hand_value:
                dealer_won = True

            if dealer_won:
                print_with_wrap("The dealer (computer)has won. Better luck next time")
                        
            else:
                if len(winning_players) > 1:
                    string = "Tie Between: "
                    for i in range(len(winning_players)):
                        player = winning_players[i]
                        string += "Player " + str(player.get_id())
                        if i < (len(winning_players) - 1):
                            string += " , "
            
                    print (string)
                    
                else:
                    print_with_wrap("Player " + str((winning_players[0]).get_id()) + " wins!")

            print_with_wrap("EXE to contine")
            input()
            clear()

            #Allow the user to exit the game after their game is finished
            print_with_wrap("Press 1 to exit.     EXE to play again")
            user_response = input()
            clear()
            if user_response == "1":
                play_game = False
            

main()


