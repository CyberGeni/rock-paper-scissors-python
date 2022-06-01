import random

choices = ['R', 'P', 'S']

def computerPlay(): 
    print(random.choice(choices))

def playRound(playerSelection, computerSelection):
    if playerSelection == 'R' and computerSelection == 'S':
        print ('You win, Rock beats Scissors')
    elif playerSelection == 'R' and computerSelection == 'P':
        print ('You lose, Paper beats Rock')
    elif playerSelection == 'P' and computerSelection == 'R':
        print ('You win, Paper beats Rock')
    elif playerSelection == 'P' and computerSelection == 'S':
        print ('You lose, Scissors beats Paper')
    elif playerSelection == 'S' and computerSelection == 'P':
        print ('You win, Scissors beats Paper')
    elif playerSelection == 'S' and computerSelection == 'R':
        print ('You lose, Rock beats Scissors')
    else:
        print ('Invalid input, try again')

playerSelection = str(input('Rock, Paper, or Scissors? (R for Rock, P for Paper, S for Scissors) '))
computerSelection = computerPlay()

print(playRound(playerSelection, computerSelection))