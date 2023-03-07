'''This implementation uses dictionaries to define the 
positions of snakes and ladders on the board. The roll_dice() 
function generates a random integer between 1 and 6, 
simulating a dice roll. The game loop alternates between the 
two players, rolling the dice, updating their positions, and 
checking for snakes and ladders. The game ends when one of 
the players reaches or passes position 100.'''


import random

# Initialize player positions
player1_pos = 0
player2_pos = 0

# Define snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Define the dice roll function
def roll_dice():
    return random.randint(1, 6)

# Define the game loop
while True:
    # Player 1 turn
    input("Player 1's turn, press enter to roll dice")
    dice_roll = roll_dice()
    print("Player 1 rolled a", dice_roll)
    player1_pos += dice_roll
    
    if player1_pos in snakes:
        print("Player 1 hit a snake! Sliding down to", snakes[player1_pos])
        player1_pos = snakes[player1_pos]
    
    if player1_pos in ladders:
        print("Player 1 found a ladder! Climbing up to", ladders[player1_pos])
        player1_pos = ladders[player1_pos]
    
    if player1_pos >= 100:
        print("Player 1 wins!")
        break
    
    print("Player 1 is now at position", player1_pos)
    
    # Player 2 turn
    input("Player 2's turn, press enter to roll dice")
    dice_roll = roll_dice()
    print("Player 2 rolled a", dice_roll)
    player2_pos += dice_roll
    
    if player2_pos in snakes:
        print("Player 2 hit a snake! Sliding down to", snakes[player2_pos])
        player2_pos = snakes[player2_pos]
    
    if player2_pos in ladders:
        print("Player 2 found a ladder! Climbing up to", ladders[player2_pos])
        player2_pos = ladders[player2_pos]
    
    if player2_pos >= 100:
        print("Player 2 wins!")
        break
    
    print("Player 2 is now at position", player2_pos)