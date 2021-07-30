from game_logic import guess_the_number


def start_guessing():
    level_dif = input('(E) - For Easy, (M) - For Medium, (H) - For Hard\nEnter Difficulty: ')

    level_dif = level_dif.lower()
    if level_dif == 'e':
        guess_the_number(10)
    elif level_dif == 'm':
        guess_the_number(20)
    elif level_dif == 'h':
        guess_the_number(30)
    else:
        print('\nInvalid Input! ---: Please Rerun The Program')


start_guessing()
