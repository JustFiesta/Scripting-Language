import random

def deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    suits = ['c', 'd', 'h', 's']
    
    deck_of_cards = []
    
    for rank in ranks:
        for suit in suits:
            card = (rank, suit)
            deck_of_cards.append(card)
    
    return deck_of_cards

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def deal(deck, n):
    if len(deck) < 5 * n:
        raise ValueError("Za mało kart w talii dla podanej liczby graczy")

    hands = []
    for i in range(n):
        player_hand = []
        for j in range(5):
            card = deck.pop(0) 
            player_hand.append(card)
        hands.append(player_hand)
    return hands

deck_of_cards = deck()
shuffled_deck = shuffle_deck(deck_of_cards)
hands = deal(shuffled_deck, 5) 
for i, hand in enumerate(hands):
    print(f"Gracz {i+1}: {hand}")