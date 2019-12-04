# Embaralhar cartas

import random

playing = False

chip_pool = 100

bet = 1

restart_phrase = "Press 'd' to shuffle again or press 'q' to leave."

suits = ('H', 'D','C','S')

ranking = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')

card_val = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.suit+self.rank
    def grab_suit(self):
        return self.suit
    def grab_rank(self):
        return self.rank
    def draw(self):
        print(self.suit+self.rank)
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def __str__(self):
        hand_comp = ""

        for card in self.cards:
            card.name = card.__str__()
            hand_comp += " " + card_name
            return "The hand has {1}".format(1==hand_comp)

    def card_add(self,card):
        self.cards.append(card)

        if card_rank == 'A':
            self.ace = True
        self.value += card_val[card_rank]

    def calc_val(self):
        if (self.ace == 'True' and self.value < 12):
            return self.value + 10
        else:
            return self.value

    def draw(self,hidden):
        if hidden == True and playing == True:
            starting_card = 1
        else:
            starting_card = 0
        for x in range (starting_card, len(self.cards)):
           self.cards[x].draw()

class Deck:

    def __init__(self):
        self.deck= []

        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)


    def deal(self):
        single_card = self.deck.pop()
        return single_card

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += " " + car.__str__()

            return "The deck has " + deck_comp

def make_bet():
    global bet
    bet = 0

    print("What amount of chips would you like to bet? (Enter whole integer please)")

    while bet == 0:
        bet_comp = input()
        bet_comp = int(bet_comp)

        if bet_comp >= 1 and bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print("Invalid bet. You have only "+ str(chip_pool) + " chips remaining.")

def deal_cards():
    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet

    deck = Deck()
    deck.shuffle()

    make_bet()

    player_hand = Hand()
    dealer_hand = Hand()

    # 2 cartas para o jogador
    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    # 2 cartas para o Dealer
    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = "Hit or stand: Press 'h' or 's'"

    chip_pool -= bet

    playing = True
    game_step()
