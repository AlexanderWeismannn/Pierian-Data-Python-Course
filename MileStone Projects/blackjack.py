
import random

#Decleration of the deck suits, ranks and a dictionary of associated int values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

#used as part of the hit / stand loop
playing = True


#CLASSES

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

#intialize and create an array of all cards
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
#prints out all the cards in the deck (FOR TESTING PURPOSES)
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "This deck has:" + deck_comp

    #suffles the deck randomly
    def shuffle(self):
        random.shuffle(self.deck)

    #deals 1 card
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:

    def __init__(self):
        self.cards = [] #array to store cards
        self.value = 0#total value of those cards
        self.aces = 0#number of aces in the hand held

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


#FUNCTION DEFINITIONS

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry, you have to bet an integer! ")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed ", chips.total)
            else:
                break


def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Would you like to Hit or Stand [h] or [s]: ")

        if x[0].lower() == "h":
            hit(deck,hand)

        elif x[0].lower() == "s":
            print("Player Stands. Dealer is playing...")
            playing = False

        else:
            print("Sorry, try again please        ")
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep = "\n")

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

#ALL GAME OUTCOMES:
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

#GAMEPLAY LOOP

while True:
    print("Welcome to Weismann's Blackjack")

    #CREATE THE DEALER, PLAYER, CARDS, AND BET

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    #have the player go until they stay or go over
    while playing:

            hit_or_stand(deck,player_hand)
            show_some(player_hand,dealer_hand)

            if player_hand.value >  21:
                player_busts(player_hand,dealer_hand,player_chips)
                break
    #If the player didnt bust then the dealer will go
    if player_hand.value <= 21:

        while dealer_hand.value <= 17:
            hit(deck,dealer_hand)

        #show both hands after and determine the winner
        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)


    print("Player's winnings stand at:",player_chips.total)

    play_again = input("Would you like to play again? Yes(y) or No(n) ")
    if play_again[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
