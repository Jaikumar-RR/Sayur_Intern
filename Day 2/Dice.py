# Problem #3
# Its is a single player game where the user starts with 0 points. User keeps rolling the 
# dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
#  added. If the number is odd, then if the number is 1,3 then the user has to jump. 
#  If the number is 5, then 3 points are added. The game ends when the user has 50 points.
import random

def roll_dice():

    return random.randint(0, 6)

def gain_points(points, amount):
    points += amount
    return points

def play_game():
    points = 0

    while points < 50:
        input("Press Enter to roll the dice...")
        dice_roll = roll_dice()

        if dice_roll == 0:
            print("Oops! You rolled a 0. Game over!")
            break
        elif dice_roll % 2 == 0:
            points = gain_points(points, 2)
            print(f"You rolled {dice_roll}. You gained 2 points. Total points: {points}")
        else:
            if dice_roll in (1, 3):
                print(f"You rolled {dice_roll}. You have to jump!")
            elif dice_roll == 5:
                points = gain_points(points, 3)
                print(f"You rolled {dice_roll}. You gained 3 points. Total points: {points}")

    if points >= 50:
        print("Congratulations! You've reached 50 points. You win!")

# Start the game
play_game()

