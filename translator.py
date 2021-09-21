import os
from googletrans import Translator


if __name__ == '__main__':
    translator = Translator()
    os.chdir('data')

    # Чтение слов из файла
    words = []
    with open('in.txt', 'r') as f:
        words = f.readlines()

    # Убирание переносов строк в конце каждого слова
    for i in range(len(words)):
        word = words[i]
        word = word[0: len(word) - 1]
        words[i] = word

    # Перевод списка слов с английского на русский
    result = translator.translate(words, src='en', dest='ru')

    # Нахождение длины самого длинного слова в списке для перевода, понадобиться для карсивого вывода
    longest_word_len = len(max(words, key=len))

    # Уведичение длины слов для более красивого вывода
    for i in range(len(words)):
        while len(words[i]) != longest_word_len:
            words[i] += ' '

    # Вывод слов и их перерводов в файлик
    with open('out.txt', 'w') as f:
        for i in range(len(words)):
            f.write(f'{words[i]} --> {result[i].text}\n')
