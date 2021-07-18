import random


def run_game():
    level_dif = input('Welcome To Math Trivia (Division Edition)\n'
                      '(E) - For Easy, (M) - For Medium, (H) - For Hard\n\nEnter Difficulty: ')

    def division_edition(num_quests, one, two, three, four, ident):
        score = 0
        attempts = 1
        while attempts < (num_quests + 1):
            a = random.randint(one, two)
            b = random.randint(three, four)

            if (a > b) and (a % b == 0):
                try:
                    if ident == 5:
                        if attempts == 10:
                            quest = int(input('\n{}. {:>3s}\n{:>8s}\n{:>7s}\n\n= {:>2s}'.format(attempts,
                                                                                                str(a),
                                                                                                '----',
                                                                                                str(b),
                                                                                                '')))
                        else:
                            quest = int(input('\n{}. {:>4s}\n{:>8s}\n{:>7s}\n\n= {:>2s}'.format(attempts,
                                                                                                str(a),
                                                                                                '----',
                                                                                                str(b),
                                                                                                '')))
                    elif attempts >= 10:
                        quest = int(input('\n{}. {:>4s}\n{:>8s}\n{:>7s}\n\n= {:>2s}'.format(attempts,
                                                                                            str(a),
                                                                                            '----',
                                                                                            str(b),
                                                                                            '')))
                    else:
                        quest = int(input('\n{}. {:>4s}\n{:>8s}\n{:>7s}\n\n= {:>2s}'.format(attempts,
                                                                                            str(a),
                                                                                            '-----',
                                                                                            str(b),
                                                                                            '')))
                    # Just decorating how the code will look in the terminal

                    if quest == (a / b):
                        print('\nYour Answer Is Correct\n')
                        score += 1
                    else:
                        print(f'\nYour Answer Is Wrong\nThe Correct Answer Is {a / b}\n')
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
        division_edition(10, 9, 50, 2, 25, 5)
    elif level_dif == 'm':
        division_edition(20, 18, 72, 7, 25, 4)
    elif level_dif == 'h':
        division_edition(25, 27, 250, 12, 25, 4)
    else:
        print('Invalid Input ---: Please Rerun The Program')


run_game()
