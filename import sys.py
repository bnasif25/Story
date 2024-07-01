import random

def create_deck():
    """Create a deck of 52 cards."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_card(deck):
    """Deal a card from the deck."""
    return deck.pop()

def calculate_score(hand):
    """Calculate the score of a hand."""
    score = 0
    ace_count = 0
    value_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
                 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    
    for card in hand:
        score += value_map[card['rank']]
        if card['rank'] == 'Ace':
            ace_count += 1

    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1

    return score

def display_hand(player, hand):
    """Display the hand of a player."""
    print(f"{player}'s hand: ", end='')
    for card in hand:
        print(f"{card['rank']} of {card['suit']}", end=', ')
    print()

def blackjack():
    """Main game loop for Blackjack."""
    print("Welcome to Blackjack!")
    print("Instructions:")
    print("1. Try to get as close to 21 as possible without going over.")
    print("2. Face cards are worth 10 points.")
    print("3. Aces are worth 1 or 11 points.")
    print("4. You can choose to 'hit' to take another card or 'stand' to hold your current total.")
    print("5. The dealer must hit until they have at least 17 points.")
    
    deck = create_deck()
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        display_hand("Player", player_hand)
        print(f"Player's score: {player_score}")

        if player_score == 21:
            print("Blackjack! You win!")
            game_over = True
            continue
        elif player_score > 21:
            print("You bust! Dealer wins!")
            game_over = True
            continue
        
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        
        if action == 'hit':
            player_hand.append(deal_card(deck))
        elif action == 'stand':
            while dealer_score < 17:
                dealer_hand.append(deal_card(deck))
                dealer_score = calculate_score(dealer_hand)
            
            display_hand("Dealer", dealer_hand)
            print(f"Dealer's score: {dealer_score}")

            if dealer_score > 21:
                print("Dealer busts! You win!")
            elif dealer_score > player_score:
                print("Dealer wins!")
            elif dealer_score < player_score:
                print("You win!")
            else:
                print("It's a tie!")
            game_over = True
        else:
            print("Invalid action. Please choose 'hit' or 'stand'.")
    
    print("Game over. Thanks for playing!")

# Run the game
blackjack()
