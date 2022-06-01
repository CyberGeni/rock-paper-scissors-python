import random

rounds = int(input('How many rounds do you want to play?'))

choices = ['R', #for rock
           'P', #for paper
           'S'  #for scissors
           ]  

def computerPlay():
    computerSelection = random.choice(choices)
    return computerSelection

def playRound(playerSelection, computerSelection):
    if (playerSelection == 'R') and computerSelection == 'S':
        print('Player (Rock) : CPU (Scissors)')
        print('You win, Rock beats Scissors')
    elif playerSelection == 'R' and computerSelection == 'P':
        print('Player (Rock) : CPU: (Paper)')
        print('You lose, Paper beats Rock')
    elif playerSelection == 'P' and computerSelection == 'R':
        print('Player (Paper) : CPU (Rock)')
        print ('You win, Paper beats Rock')
    elif playerSelection == 'P' and computerSelection == 'S':
        print('Player (Paper) : CPU (Scissors)')
        print ('You lose, Scissors beats Paper')
    elif playerSelection == 'S' and computerSelection == 'P':
        print('Player (Scissors) : CPU (Paper)')
        print ('You win, Scissors beats Paper')
    elif playerSelection == 'S' and computerSelection == 'R':
        print('Player (Scissors) : CPU (Rock)')
        print ('You lose, Rock beats Scissors')
    elif playerSelection == 'R' and computerSelection == 'R':
        print('Player (Rock) : CPU (Rock)')
        print('It\'s a Tie!')
    elif playerSelection == 'P' and computerSelection == 'P':
        print('Player (Paper) : CPU (Paper)')
        print('It\'s a Tie')
    elif playerSelection == 'S' and computerSelection == 'S':
        print('Player (Scissors) and CPU (Scissors)')
        print('It\'s a Tie')
    else:
        print('Invalid input')
        gameplay()

# values for the gameplay
def gameplay():
    global playerSelection, computerSelection
    playerSelection = str(input('Rock, Paper or Scissors? (R for Rock, P for Paper, S for Scissors)'))
    computerSelection = computerPlay()
    
    playRound(playerSelection, computerSelection)

def game():
    for i in range(rounds):
        print('Round ' + str(i + 1))
        i += 1
        gameplay()  
    else:
        print('_________________________________________________Game Over!!!____________________________________________________ \n Thanks for playing (inserts smiley face emoji)')
game()
