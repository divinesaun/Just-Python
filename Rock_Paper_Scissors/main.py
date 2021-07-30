import random


def rock_paper_scissors():
    player = input('Welcome To Rock Paper Scissors Game\n(R) - For Rock, (P) - For Paper, (S) - For Scissors\n\n'
                   'Enter Your Username: ')

    if player == '':
        player = 'Player1'

    player_score = 0
    computer_score = 0

    for rounds in range(1, 4):
        print(f'\nROUND {rounds}')

        quest = input('\nRock  Paper  Scissors: ')
        computer = random.choices([1, 2, 3])
        quest = quest.lower()

        if quest == 'r':
            if computer == [1]:
                print(f'\n{player} Played Rock -- Computer Played Rock\nIt\'s a draw')
                player_score += 1
                computer_score += 1
            elif computer == [2]:
                print(f'\n{player} Played Rock -- Computer Played Paper\nComputer Won')
                computer_score += 3
            else:
                print(f'\n{player} Played Rock -- Computer Played Scissors\n{player} Won')
                player_score += 3

        elif quest == 'p':
            if computer == [1]:
                print(f'\n{player} Played Paper -- Computer Played Rock\n{player} Won')
                player_score += 3
            elif computer == [2]:
                print(f'\n{player} Played Paper -- Computer Played Paper\nIt\'s a draw')
                computer_score += 1
                player_score += 1
            else:
                print(f'\n{player} Played Paper -- Computer Played Scissors\nComputer Won')
                computer_score += 3

        elif quest == 's':
            if computer == [1]:
                print(f'\n{player} Played Scissors -- Computer played Rock\nComputer Won')
                computer_score += 3
            elif computer == [2]:
                print(f'\n{player} Played Scissors -- Computer Played Paper\n{player} Won')
                player_score += 3
            else:
                print(f'\n{player} Played Scissors -- Computer Played Scissors\nIt\'s a draw')
                computer_score += 1
                player_score += 1
        else:
            print('Invalid Input ---: (R) - For Rock, (P) - For Paper, (S) - For Scissors')
            computer_score += 3

    print(f'\nRESULTS:\n'
          f'  {player} - {player_score}\n'
          f'  Computer - {computer_score}')


rock_paper_scissors()
