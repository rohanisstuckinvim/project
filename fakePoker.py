import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

def draw_cards(deck):
    hand = []
    for i in range(5):
        random_card = random.choice(deck)
        deck.remove(random_card)
        hand.append(random_card)
    return hand

def rank_hand(hand):
    """Return a value indicating the ranking of a hand."""
    pass

def determine_winner(player1, player2):
    """Return the winning player."""
    pass

# Main game loop
player1 = draw_cards(deck)
player2 = draw_cards(deck)

winner = determine_winner(player1, player2)

if winner == player1:
    print("Player 1 wins with a hand of ", player1)
else:
    print("Player 2 wins with a hand of ", player2)
