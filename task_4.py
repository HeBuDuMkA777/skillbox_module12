print('Задача 4. Текстовый редактор')

# Продолжаем разрабатывать новый текстовый редактор.
# Теперь нам поручили написать для него код, который считает, сколько раз в тексте встречается любая выбранная буква
# или цифра (а не только буква «ы», как было в задаче 3 урока «Цикл for: итерирование по строке»).

# Что нужно сделать
# Напишите функцию count_letters(), которая принимает на вход текст и подсчитывает, какое в нём количество цифр K и букв N.
# Функция должна вывести на экран информацию о найденных буквах и цифрах в определённом формате.

# Пример
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищем? л
# Количество цифр 0: 2
# Количество букв л: 1

def count_letters(text, num, sym):
    print(f"Количество цифр {num}: {text.count(num)}\nКоличество букв {sym}: {text.count(sym)}")

text = input("Введите текст: ")
number = input("Какую цифру ищем? ")
symbol = input("Какую букву ищем? ")
count_letters(text, number, symbol)