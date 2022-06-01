import random

choices = ['R', 'P', 'S']

def computerPlay():
    computerSelection = random.choice(choices)
    return computerSelection

def playRound(playerSelection, computerSelection):
    if (playerSelection == 'R') and computerSelection == 'S':
        print('You win, Rock beats Scissors')
    elif playerSelection == 'R' and computerSelection == 'P':
        print('You lose, Paper beats Rock')
    elif playerSelection == 'P' and computerSelection == 'R':
        print ('You win, Paper beats Rock')
    elif playerSelection == 'P' and computerSelection == 'S':
        print ('You lose, Scissors beats Paper')
    elif playerSelection == 'S' and computerSelection == 'P':
        print ('You win, Scissors beats Paper')
    elif playerSelection == 'S' and computerSelection == 'R':
        print ('You lose, Rock beats Scissors')
    elif playerSelection == 'R' and computerSelection == 'R':
        print('Tie')
    elif playerSelection == 'P' and computerSelection == 'P':
        print('Tie')
    elif playerSelection == 'S' and computerSelection == 'S':
        print('Tie')
    else:
        print('Invalid input')

playerSelection = str(input('Rock, paper or scissors?'))
computerSelection = computerPlay()

if computerSelection == 'R':
    print('Computer played Rock')
elif computerSelection == 'P':
    print('Computer played Paper')
else:
    print('Computer played Scissors')

