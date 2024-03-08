string_list = ['cat', 'horse', 'dog', 'crocodile', 'elephant', 'snake']

def max_length(string_list):
    max_word_length = 0  # Задаем базовое значение для длины строки
    for i, word in enumerate(string_list):
        word_length = len(word)
        if word_length > max_word_length:
            max_word_length = word_length  # Обновляем базовое значение длины строки по мере прохождения списка
    return max_word_length

# Выводим результат
max_word_length = max_length(string_list)
print("Длина самого длинного слова из таблицы:", max_word_length)
