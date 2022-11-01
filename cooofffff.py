import random
active = True
Score = 0
while active:
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    user_choice = input('Enter you choice!: ')

    #Start game
    if user_choice == 'Rock' and computer_choice == 'Rock':
        print(f'Computer chooses {computer_choice}')
        print('Its a tie! ')
        print(Score)
    elif user_choice == 'Rock' and computer_choice == 'Paper':
        print(f'Computer chooses {computer_choice}')
        print('You lost!')
        Score -= 1
        print(Score)
    elif user_choice == 'Rock' and computer_choice == 'Scissors':
        print(f'Computer chooses {computer_choice}')
        print('You win!')
        Score += 1
        print(Score)
    elif user_choice == 'Paper' and computer_choice == 'Rock':
        print(f'Computer chooses {computer_choice}')
        print('You win!')
        Score += 1
        print(Score)
    elif user_choice == 'Paper' and computer_choice == 'Paper':
        print(f'Computer chooses {computer_choice}')
        print('Its a draw')
        print(Score)
    elif user_choice == 'Paper' and computer_choice == 'Scissors':
        print(f'Computer chooses {computer_choice}')
        print('You lose!')
        Score -= 1
        print(Score)
    elif user_choice == 'Scissors' and computer_choice == 'Rock':
        print(f'Computer chooses {computer_choice}')
        print('You lose!')
        Score -= 1
        print(Score)
    elif user_choice == 'Scissors' and computer_choice == 'Paper':
        print(f'Computer chooses {computer_choice}')
        print('You win!')
        Score += 1
        print(Score)
    elif user_choice == 'Scissors' and computer_choice == 'Scissors':
        print(f'Computer chooses {computer_choice}')
        print('Its a draw!')
        print(Score)

