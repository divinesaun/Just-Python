import random


def guess_the_number(finish_range):
    print(f'\nWelcome To Guess The Number Game\n\nChoose A Number Between 0 and {finish_range}')
    true_num = random.randint(0, finish_range)
    for attempts in range(4, 0, -1):
        try:
            quest = int(input('Guess The Number: '))
            if quest == true_num:
                print('Congratulations, You Have Won!')
                break
            elif (quest != true_num) and ((attempts - 1) == 0):
                print(f'\nSorry, You have lost. The correct number was {true_num}')
            elif quest > true_num:
                print(f'\nYou number is too high!\nYou have {attempts - 1} attempt(s) left.\n')
            elif quest < true_num:
                print(f'\nYour number is too low!\nYou have {attempts - 1} attempt(s) left.\n')
        except SyntaxError:
            print('\nInvalid Input ---: Please Enter A NUMBER\n')
        except ValueError:
            print('\nInvalid Input ---: Please Enter A NUMBER\n')
