import random

choices = ['R', #for rock
           'P', #for paper
           'S'  #for scissors
           ]  

def computerPlay():
    computerSelection = random.choice(choices)
    return computerSelection

def playRound(playerSelection, computerSelection):
    if (playerSelection == 'R') and computerSelection == 'S':
        print('You played Rock and Computer played Scissors')
        print('You win, Rock beats Scissors')
    elif playerSelection == 'R' and computerSelection == 'P':
        print('You played Rock and Computer played Paper')
        print('You lose, Paper beats Rock')
    elif playerSelection == 'P' and computerSelection == 'R':
        print('You played Paper and Computer played Rock')
        print ('You win, Paper beats Rock')
    elif playerSelection == 'P' and computerSelection == 'S':
        print('You played Paper and Computer played Scissors')
        print ('You lose, Scissors beats Paper')
    elif playerSelection == 'S' and computerSelection == 'P':
        print('You played Scissors and Computer played Paper')
        print ('You win, Scissors beats Paper')
    elif playerSelection == 'S' and computerSelection == 'R':
        print('You played Scissors and Computer played Rock')
        print ('You lose, Rock beats Scissors')
    elif playerSelection == 'R' and computerSelection == 'R':
        print('You played Rock and Computer also played Rock')
        print('It\'s a Tie!')
    elif playerSelection == 'P' and computerSelection == 'P':
        print('You played Paper and Computer also played Paper')
        print('It\'s a Tie')
    elif playerSelection == 'S' and computerSelection == 'S':
        print('You played Scissors and Computer also played Scissors')
        print('It\'s a Tie')
    else:
        print('Invalid input')

# values for the gameplay
def gameplay():
    global playerSelection, computerSelection
    playerSelection = str(input('Rock, Paper or Scissors? (R for Rock, P for Paper, S for Scissors)'))
    computerSelection = computerPlay()
    playRound(playerSelection, computerSelection)

rounds = 5
score_count = 0

def game():
    for i in range(rounds):
        i += 1
        gameplay()  

game()
