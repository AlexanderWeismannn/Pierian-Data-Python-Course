#using random to "Shuffle deck" at te beginning of the game
import random
import time
#strings of all suit types
suits = ("Hearts","Diamonds","Clubs", "Spades")
#strings of all number in a suit
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
#dictionary of the strings coressponding to ints
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}
#switch to control while loop of the game
playing = True

#THE CARD CLASS
#contains an intitializing method and a print method which returns the rank and suit
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return  self.rank + " of " + self.suit
#THE DECK CLASS
#contains an intialization, print, shuffle and deal method
class Deck:
    #intializes the deck object with a list of cards
    def __init__(self):
        self.deck =  []#empty list to store all cards in the DECK
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))#creates a card

    def __str__(self):
        #prints all cards on the stack
        deck_comp = ""#empty string
        for card in self.deck:
            deck_comp += "\n" + card.__str__()#will create a list of all cards currently in the deck_comp
        return "The Deck Contains: " + deck_comp

    def shuffle(self):
        #uses built in randomizer for lists to shuffle the deck
        random.shuffle(self.deck)#using the built in shuffle method to randomize the deck

    def deal(self):
        #pops and returns the card from the top of the list
        single_card = self.deck.pop()#pops a card off of the deck stack to deal
        return single_card

#THE HAND CLASS
#contains an intializer, and add_card, and adjust_for_ace method
class Hand:
    #intializes the Hand object with a cards, value, and number of aces
    def __init__(self):
        self.cards = []#list of cards currently held in the hand
        self.value = 0#total value of the cards in the players hands
        self.aces = 0#indicated the number of acces held in the users hands

    #Adds a card to the hand as well as checks if the card is an ace
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1 #adds to the counter if there is an Ace

    #checks if the value of the ace can stay at 11 or be adjusted to 1
    def adjust_for_ace(self):
        while self.value > 21 + self.aces:
            self.value -= 10
            self.aces -= 1
#The CHIPS CLASS
#contains an intializer, a win_be, and a lose_bet method
class Chips:

    def __init__(self):
        self.total = 100#user starts with 100 points/chips to bet with
        self.bet = 0#the var for the user inputed bet

    def win_bet(self):
        self.total = self.total + self.bet

    def lose_bet(self):
        self.total = self.total - self.bet

#checks the player's bet to make sure it is an int and doesnt exceed their number of chips
def take_bet(player_bet):
    #do until a bet is placed
    while True:
        #takes in user input
        try:
            player_bet.bet = int(input("How many chips would you like to bet: "))
        #Throws an error if the input is not and int
        except ValueError:
            print("Sorry, you can't bet that!")
        else:
        #Checks that the inpur is <= to the total # of chips the player has
            if player_bet.bet > player_bet.total:
                print("Sorry, you are betting more chips than you actually have")
            else:
                #bet was succesfully placed
                break

#adds a card the the players hand
def hit(deck,hand):
#makes an hand object calling the add card method using the deck.deal() as input
#checks for ace
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    #loop until the player stands
    while True:
        choice = input("Hit or Stand? [h] or [s] ")
        if(choice[0] == "h"):
             hit(deck,hand)

        elif(choice[0] == "s"):
             print("Player stands, dealer's turn")
             playing = False
        else:
             print("Unknown command, please try again.")
             continue
        break

#shows the second card in the dealer's hand and the whole player's hand
def show_some(player,dealer):
    print("\n DEALER'S HAND:")
    print("<cards hidden>")
    print('',dealer.cards[1])
    time.sleep(2)
    #*player.cards [shows every item in the collection]
    print("\nPLAYER'S HAND:", *player.cards, sep = "\n")
    time.sleep(2)

def show_all(player,dealer):
    print("\nDEALER'S HAND:",*dealer.cards,sep = "\n")
    print("DEALER'S HAND =", dealer.value )
    time.sleep(2)
    print("\nPLAYER'S HAND:",*player.cards,sep = "\n")
    print("PLAYER'S HAND =", player.value )
    time.sleep(2)

def player_busts(player,dealer,chips):
    print("You Lose :( ")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("You WIN :) ")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer LOSES :)")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer WINS :(")
    chips.lose_bet()

def push(player,dealer):
    print("TIE, its a push!")

print("Welcome to Weismann's Blacjack:")
print("Shuffling the deck . . .")
time.sleep(2)
print("Handing out chips . . . ( 100 )")
time.sleep(2)

#
#MAKE SURE TO PUT IT IN THE RIGHT LOOP
#
while True:
    #creating the deck object for use and shuffling
    deck = Deck()
    deck.shuffle()

    #creating the player hand w/ two cards
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    #creating the dealer hand w/ two cards
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #create a player chips base
    player_chips = Chips()



    #taking player bet
    take_bet(player_chips)

    #showing partial cards
    show_some(player_hand,dealer_hand)

    while playing:
        #keep asking the player if they want to hit or spend
        hit_or_stand(deck, player_hand)
        #show the updated hand
        show_some(player_hand, dealer_hand)
        #check for playevalue going over 21 and busting
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    #if the player didnt bust the dealer will hit until they reach 17 or go over
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

            #now show the dealers full unhidden hand along with the players
        show_all(player_hand,dealer_hand)

        # all outcomes after dealer has chosen their cards
        # V          V           V           V           V

        #Dealer busts from having a hand > 21
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

            #Dealer doesnt bust but loses to players hand
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

            #Dealer doesnt bust and wins to players hand
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        #Dealer and player tie
        else:
            push(dealer_hand,player_hand)


    #Round has ended, ask if they want to play again
    print("\n The player's winnings stand at ",player_chips.total)
    play_again = input("Would you like to play again? 'y' or 'n': ")

    if play_again[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
