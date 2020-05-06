# This Python file uses the following encoding: utf-8
import random


def print_number_of_lives():
    symbol_of_heart = u"\u2764"
    print(symbol_of_heart * lives)


def check_this_letter_not_guessed_yet(clue, attempt):
    if clue.count(attempt) == 0:
        return True
    else:
        return False


def attempt_to_guess_letter():
    global number_of_guessed_letters, number_of_unknown_letters, attempt
    print_number_of_lives()
    print('Угадай букву в слове')
    attempt = input()[0].lower()
    if check_this_letter_not_guessed_yet(clue, attempt):
        number_of_guessed_letters += secret_word.count(attempt)
        number_of_unknown_letters = len(secret_word) - number_of_guessed_letters


def guess_letter_correctly():
    global secret_word, clue
    flag = 0
    if check_this_letter_not_guessed_yet(clue, attempt):
        for i in range(len(secret_word)):
            if attempt == secret_word[i]:
                clue[i] = attempt
                flag += 1

                if flag == secret_word.count(attempt):
                    print(clue)
                    return True
    else:
        print("Такая буква уже есть")
        print(clue)
        return True

    return False


def fail():
    global lives
    if lives != 1:
        lives -= 1
        print('Такой буквы здесь нет. Попробуйте еще раз')
    else:
        lives = 0
        print("Вы проиграли=(")
        print("Загаданое слово {}".format(secret_word))
        print("Сыграем еще раз? Да/Нет")
        return repeat_game(input())


def repeat_game(answer):
    global continue_game
    if answer.lower() == "да":
        continue_game = True

    elif answer.lower() == "нет":
        continue_game = False
    return continue_game


def check_word_is_guessed():
    global number_of_unknown_letters, number_of_guessed_letters, is_guessed
    if number_of_unknown_letters != 0:
        print("Угадано {} букв. Осталось угадать {} букв".format(number_of_guessed_letters,
                                                                 number_of_unknown_letters))
        return False
    else:
        print("Ура! Вы отгадали слово")
        print("Сыграем еще раз? Да/Нет")
        repeat_game(input().lower())
        is_guessed = True
        return True, is_guessed


def number_of_lives_by_chosen_difficulty():
    print("Выберите сложность (1, 2 или 3):\n 1 Легкий \n 2 Средний \n 3 Сложный")
    answer = int(input())
    if answer == 1:
        lives = 9
    elif answer == 2:
        lives = 5
    elif answer == 3:
        lives = 3
    else:
        print("Некорректный ответ")
        lives = 0
    return lives


words = ['машина', 'круг', 'мяч', 'привет', 'конфета ', 'брат', 'миска', 'крыса', 'девочка', 'мальчик', 'буря', 'гроза']


continue_game = True
while continue_game:
    lives = number_of_lives_by_chosen_difficulty()
    is_guessed = False
    attempt = ''

    secret_word = random.choice(words)
    secret_word_length = len(secret_word)
    number_of_unknown_letters = secret_word_length
    clue = ["?"] * secret_word_length
    print(clue)

    while lives > 0 and not is_guessed:

        number_of_guessed_letters = secret_word_length - number_of_unknown_letters

        attempt_to_guess_letter()


        if not check_word_is_guessed():
            if not guess_letter_correctly():
                if fail():
                    break
        else:
            break