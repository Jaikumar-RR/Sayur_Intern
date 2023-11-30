# Problem #2
# You have 6 x 6 game board where each cell is shown as a *
# This is a two player dice game. The die has numbers 1 to 6.
# Each player rolls the dice twice. First roll is row number, second roll is col number.
# After the player rolls the dice, in the (row,col) enter the player's initial. 
# If the player  A rolls the dice and  if  player B already has their initial in the same row,col
# add a point to A and change the initial to A. 

# Player who gets 5 points first wins the game.
# Print the board each time after the user rolls and also print the current score.
# Use functions

import random 

def initialize_board():
    return [['\u25A1\u0335' for _ in range(6)] for _ in range(6)]

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def update_board(board, row, col, player):
    if board[row][col] == '\u25A1\u0335':
        board[row][col] = player
    else:
        if board[row][col] != player:   
            board[row][col] = player
            return True
    return False

def check_winner(score):
    return any(score[player] >= 5 for player in score)

def Two_player_game():
    board = initialize_board()
    players = ['A', 'B']
    score = {player: 0 for player in players}

    while not check_winner(score):
        for player in players:
            print(f"Player {player}'s turn:")
            input("Press Enter to roll the dice...")
            
            row, col = roll_dice()
            print(f"Row: {row}, Col: {col}")
            
            updated = update_board(board, row - 1, col - 1, player)
            if updated:
                score[player] += 1

            print_board(board)
            print(f"Score - Player A: {score['A']}  Player B: {score['B']}")

    winner = [player for player, points in score.items() if points >= 5][0]
    print(f"Player {winner} wins!")

Two_player_game()

