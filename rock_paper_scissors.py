# This program will play a rock/paper/scissors game between one player and the computer
import random

def play():
    print("Welcome to Rock, Paper, Scissors!")
    computer_rounds_won = 0
    player_rounds_won = 0
    while True:
        try:
            number_of_rounds = int(input('\nHow many rounds would you like to play? (Must be an odd number): '))
            if number_of_rounds % 2 == 0:
                print("Number entered is even. Please enter an odd number.")
                continue
            break
        except ValueError:
            print("Please enter an odd number.")
    x = 0
    while x < number_of_rounds:
        print('Playing game # {}'.format(x))
        hand_list = ['rock', 'paper', 'scissors']
        computer_hand = random.choice(hand_list)
        player_hand = input('\nType rock, paper, or scissors: ').lower()
        if player_hand == computer_hand:
            print("Tied. Both players chose {}".format(player_hand))
            continue
        elif player_hand == "rock" and computer_hand == "paper":
            print("Computer wins.")
            computer_rounds_won += 1
            x += 1
        elif player_hand == "rock" and computer_hand == "scissors":
            print("Player wins.")
            player_rounds_won += 1
            x += 1
        elif player_hand == "scissors" and computer_hand == "rock":
            print("Computer wins.")
            computer_rounds_won += 1
            x += 1
        elif player_hand == "scissors" and computer_hand == "paper":
            print("Player wins.")
            player_rounds_won += 1
            x += 1
        elif player_hand == "paper" and computer_hand == "scissors":
            print("Computer wins.")
            computer_rounds_won += 1
            x += 1
        elif player_hand == "paper" and computer_hand == "rock":
            print("Player wins.")
            player_rounds_won += 1
            x += 1
    print("Final score: Player: {}  Computer: {}".format(player_rounds_won, computer_rounds_won))


play()
