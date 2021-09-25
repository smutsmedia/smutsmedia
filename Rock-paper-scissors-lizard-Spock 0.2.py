print 'Lets paly rock, paper, scissors, lizard, Spock'
# Rock-paper-scissors-lizard-Spock template
print ''

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

computer = 0
player = 0

# helper functions

def name_to_number(name):


    if name == 'rock':
        name = 0
    elif name == 'Spock':
        name = 1
    elif name == 'paper':
        name = 2
    elif name == 'lizard':
        name = 3
    elif name == 'scissors':
        name = 4
    #else print 'Invalid input'
    
    return name
    
    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    
    if number == 0:
        number = 'rock'
    elif number == 1:
        number = 'spock'
    elif number == 2:
        number = 'paper'
    elif number == 3:
        number = 'lizard'
    elif number == 4:
        number = 'scissors'
    #else print 'Invalid input'
    
    return number

    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    global computer, player

    # print a blank line to separate consecutive games
    print ''
    
    # print out the message for the player's choice
    print 'Player chooses',  player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_choice = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randint(0, 4)
    
    # convert comp_number to comp_choice using the function number_to_name()
    # print out the message for computer's choice
    print 'Computer chooses', number_to_name(comp_number)
    
    # compute difference of comp_number and player_number modulo five
    num = (comp_number - player_choice) % 5
    # use if/elif/else to determine winner, print winner message
    if (num == 1) or (num == 2):
        print number_to_name(comp_number), 'Beats ', number_to_name(player_choice) ,'Computer wins!'
        computer = computer + 1
    if (num == 3) or (num == 4):
        print number_to_name(player_choice), 'Beats', number_to_name(comp_number),'Player wins!'
        player = player + 1
    if (num == 0):
        print number_to_name(comp_number), 'and', number_to_name(player_choice),'are the same so Player and Computer tie!'
 


while True:
    input = raw_input('Please Pick one:  ')
    if input == 'done': break 
    if input =='Rock' : input = 'rock'
    if input =='Paper' : input = 'paper'
    if input =='Scissors' : input = 'scissors'
    if input =='Lizard' : input = 'lizard'
    if input =='spock' : input = 'Spock'
    rpsls(input)
    print 'Player =', player
    print 'Computer =', computer
    print ''
    continue
print 'Computer =', computer
print 'Player =', player
if computer > player:
    print 'Computer wins the game'
if player > computer:
    print 'Player wins the game'
if player == computer:
    print 'Thier is no winner'


