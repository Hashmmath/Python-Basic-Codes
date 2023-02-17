'''When you run this program, it will roll a dice and print 
a random face for the dice ten times, with a short interval 
between each face. The dice faces are defined as ASCII art 
in the dice_faces list. You can modify the ASCII art to change 
the appearance of the dice faces.'''

import random
import time

# Define a list of dice faces
dice_faces = ['''
 _______
|       |
|   O   |
|_______|
''', '''
 _______
| O     |
|       |
|_______|
''', '''
 _______
| O     |
|   O   |
|_______|
''', '''
 _______
| O   O |
|       |
|_______|
''', '''
 _______
| O   O |
|   O   |
|_______|
''', '''
 _______
| O   O |
| O   O |
|_______|
''']

# Define the function for rolling the dice
def roll_dice():
    for i in range(10):
        # Generate a random dice face
        dice_face = random.choice(dice_faces)
        # Print the dice face
        print(dice_face)
        # Wait for a short interval before printing the next dice face
        time.sleep(0.1)

# Call the roll_dice() function
roll_dice()
