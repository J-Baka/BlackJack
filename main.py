import art
import random

print(art.logo)

user_card = []
comp_card = []

comp_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    dealer = random.randint(0, len(comp_deck) - 1)
    comp_card.append(comp_deck[dealer])
    print(f"The dealer's first card is {comp_card[0]}")
    dealer = random.randint(0, len(user_deck) - 1)
    user_card.append(user_deck[dealer])
    print(f"Your first card is {user_card[0]}")


def user_turn():
    dealer = random.randint(0, len(user_deck) - 1)
    end_turn = False
    i = 0
    total = user_card[i]
    while not end_turn:
        user_choice = input("Would you like to draw another card? Type 'Yes' or 'No': ")
        if user_choice == "Yes":
            i += 1
            user_card.append(user_deck[dealer])
            print(f"You drew {user_card[i]}")
            total = total + user_card[i]
            if total < 21:
                print(f"Your total is {total}")
            elif total == 21:
                print("BlackJack!!")
                end_turn = True
            else:
                print("You drew more than 21.")
                end_turn = True
        elif user_choice == "No":
            end_turn = True
    return total


def comp_turn():
    dealer = random.randint(0, len(comp_deck) - 1)
    end_turn = False
    i = 0
    total = comp_card[i]
    while not end_turn:
        i += 1
        comp_card.append(comp_deck[dealer])
        print(f"The computer drew {comp_card[i]}")
        total = total + comp_card[i]
        if total <= 16:
            print(f"The House's total is {total}")
        elif 16 < total < 21:
            print(f"The House's total is {total}")
            end_turn = True
        elif total == 21:
            print("BlackJack!!")
            end_turn = True
        else:
            print("The House drew more than 21.")
            end_turn = True
    return total


def game_outcome(total1, total2):
    if total1 == 21 and total2 == 21:
        print("Both players got BlackJack!! The House Wins!!")
    elif total2 == 21:
        print("The House got BlackJack!! They Win!!")
    elif total1 == 21:
        print("You got BlackJack!! Congratulations!!")
    elif total2 < total1 < 21:
        print("You win!!")
    elif total1 < total2 < 21:
        print("The House Wins!!")
    elif total1 == total2:
        print("It's a Draw!!")
    elif total1 > 21:
        print("The House wins!!")
    elif total1 < 21 and total2 > 21:
        print("You win!!")


def blackjack():
    game_end = False
    while not game_end:
        deal_card()

        user_total = user_turn()
        comp_total = comp_turn()
        print(f"Your total is {user_total} & the House's total is {comp_total}")
        game_outcome(user_total, comp_total)
        user_choice = input("Would you like to play again? 'Yes' or 'No': ")
        if user_choice == "Yes":
            user_card.clear()
            comp_card.clear()
            blackjack()
        elif user_choice == "No":
            print("Thanks for playing!!! Goodbye")
        game_end = True


blackjack()


