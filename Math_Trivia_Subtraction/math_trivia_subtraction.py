import random


def run_game():
    level_dif = input('Welcome To Math Trivia (Subtraction Edition)\n'
                      '(E) - For Easy, (M) - For Medium, (H) - For Hard\n\nEnter Difficulty: ')

    def subtraction_edition(num_quests, one, two, three, four, ident):
        score = 0
        attempts = 1
        while attempts < (num_quests + 1):
            a = random.randint(one, two)
            b = random.randint(three, four)

            if a > b:
                try:

                    if ident == 5:
                        if attempts == 10:
                            quest = int(input('{}. {:>3s}\n  -{:>4s}\n{:>5s}'.format(attempts, str(a), str(b), '')))
                        else:
                            quest = int(input('{}. {:>4s}\n  -{:>4s}\n{:>5s}'.format(attempts, str(a), str(b), '')))
                    elif attempts >= 10:
                        quest = int(input('{}. {:>4s}\n  -{:>5s}\n{:>5s}'.format(attempts, str(a), str(b), '')))
                    else:
                        quest = int(input('{}. {:>4s}\n  -{:>4s}\n{:>4s}'.format(attempts, str(a), str(b), '')))

                    if quest == (a - b):
                        print('\nYour Answer Is Correct\n')
                        score += 1
                    else:
                        print(f'\nYour Answer Is Wrong\nThe Correct Answer Is {a - b}\n')
                except SyntaxError:
                    print('Invalid Input ---: Please Enter A Number\n')
                except ValueError:
                    print('Invalid Input ---: Please Enter A Number\n')

                attempts += 1
            else:
                attempts += 0

        print(f'\nYou Got {score}/{num_quests}')

    level_dif = level_dif.lower()

    if level_dif == 'e':
        subtraction_edition(10, 60, 99, 50, 89, 5)
    elif level_dif == 'm':
        subtraction_edition(20, 350, 500, 120, 490, 4)
    elif level_dif == 'h':
        subtraction_edition(25, 700, 999, 300, 989, 4)
    else:
        print('Invalid Input ---: Please Rerun The Program')


run_game()
