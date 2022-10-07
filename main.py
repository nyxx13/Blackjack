import random
from art import logo
print(logo)


def deal_card():
    cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21:
        return 0
    if 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score,computer_score):
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose!, Opponent has BlackJack!"
    elif player_score == 0:
        return "You Win! You got BlackJack!"
    elif player_score > 21:
        return "You Lose! You went over!"
    elif computer_score > 21:
        return "You Win! Opponent went over!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You Lose!"

def play_game():
    print(logo)
    player_cards = []
    computer_cards = []
    game_over = False

    for x in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    while game_over == False:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, Score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score > 21 or player_score == 0 or computer_score == 0:
            game_over == True

        cont = input("Draw another card? (y/N)")
        if cont == 'y':
            player_cards.append(deal_card())
        else:
            game_over = True

    while computer_score != 0 and computer_score < 21:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"   Your final hand: {player_cards}, final score: {player_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? (y/N): ") == "y":
  clear()
  play_game()