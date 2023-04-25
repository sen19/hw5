import random

MORSE_CODES = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}
words = ['code', 'bit', 'soul', 'next']
answers = []


def morse_encode(words):
    '''
    переводит слова на английском языке в последовательности точек и тире.
    :param words:
    :return: строка Морзе
    '''
    word_encoded = []

    for letter in words:
        word_encoded.append(MORSE_CODES.get(letter, ''))

    return ' '.join(word_encoded)


def get_word():
    '''
    получает случайное слово из списка

    :return: строка слова
    '''

    return random.choice(words)


def print_statistics(answers):
    '''
    на основе списка answers выводит статистику типа [True, False, True, False, True]
    :param answers:
    :return: возвращает список верности ответов
    '''
    answers_total = len(answers)
    answers_correct = sum(answers)
    answers_incorrect = answers_total - answers_correct

    print(f'Всего задачек: {answers_total}\n'
          f'Отвечено верно: {answers_correct}\n'
          f'Отвечено неверно: {answers_incorrect}\n')


def main():
    print('Сегодня мы потренируемся расшифровывать азбуку Морзе')
    print('Нажмите ENTER и начнем')
    input()

    for i in range(1, len(words)+1):

        current_word = get_word()
        current_encoded = morse_encode(current_word)

        print(f'Слово {i} {current_encoded}')


        user_input = input()

        if user_input.lower() == current_word:
            print(f'Верно, {current_word}!')
            answers.append(True)
        else:
            print(f'Неверно, {current_word}!')
            answers.append(False)

    print_statistics(answers)


main()

