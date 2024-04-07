# Create a Python application that displays a random tip from a collection of tips stored in a text file.
import random


def display_random_tip():
    with open('tips.txt', 'r') as f:
        lines = f.readlines()
        random_line = random.choice(lines)
    return random_line


random_tips_displayed = display_random_tip()
print(random_tips_displayed)
