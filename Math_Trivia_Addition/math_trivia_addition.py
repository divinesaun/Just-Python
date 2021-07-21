import random


def run_game():
    level_dif = input('Welcome To Math Trivia (Addition Edition)\n'
                      '(E) - For Easy, (M) - For Medium, (H) - For Hard\n\nEnter Difficulty: ')

    def addition_edition(num_quests, one, two, ident):
        score = 0

        for attempts in range(1, num_quests + 1):
            a = random.randint(one, two)
            b = random.randint(one, two)
            try:
                if ident == 5:
                    if attempts == 10:
                        quest = int(input('{}. {:>3d}\n  +{:>4d}\n{:>5s}'.format(attempts, a, b, '')))
                    else:
                        quest = int(input('{}. {:>4d}\n  +{:>4d}\n{:>5s}'.format(attempts, a, b, '')))
                elif attempts >= 10:
                    quest = int(input('{}. {:>4d}\n  +{:>5d}\n{:>5s}'.format(attempts, a, b, '')))
                else:
                    quest = int(input('{}. {:>4d}\n  +{:>4d}\n{:>4s}'.format(attempts, a, b, '')))
                # Just decorating how the code will look in the terminal

                if quest == (a + b):
                    print('\nYour Answer Is Correct\n')
                    score += 1
                else:
                    print(f'\nYour Answer Is Wrong\nThe Correct Answer Is {a + b}\n')
            except SyntaxError:
                print('Invalid Input ---: Please Enter A Number\n')
            except ValueError:
                print('Invalid Input ---: Please Enter A Number\n')

        print(f'\nYou Got {score}/{num_quests}')

    level_dif = level_dif.lower()

    if level_dif == 'e':
        addition_edition(10, 10, 49, 5)
    elif level_dif == 'm':
        addition_edition(20, 100, 300, 4)
    elif level_dif == 'h':
        addition_edition(25, 200, 499, 4)
    else:
        print('Invalid Input ---: Please Rerun The Program')


run_game()
