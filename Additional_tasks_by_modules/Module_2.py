import random

# Задачи на if

def is_leap_year(year):
    # Если год делится на 4 и не делится на 100, или делится на 400, то он високосный
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def calculate_delivery_cost(weight):
    # Стоимость доставки основана на весе посылки
    if weight <= 2:
        return 50
    elif weight <= 10:
        # Для веса свыше 2 кг, добавляется 20 рублей за каждый дополнительный килограмм
        return 50 + (weight - 2) * 20
    else:
        # Для посылок более 10 кг стоимость фиксированная
        return 200


# Задачи на while

def find_primes_less_than_N(N):
    primes = []  # Список для хранения простых чисел
    number = 2   # Начинаем с первого простого числа
    while number < N:
        is_prime = True  # Предполагаем, что число простое
        for divisor in range(2, int(number ** 0.5) + 1):
            # Если число делится без остатка, оно не простое
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)  # Добавляем простое число в список
        number += 1
    return primes

def guess_the_number():
    number_to_guess = random.randint(1, 100)  # Загадываем число
    guess = None  # Переменная для хранения попытки пользователя
    attempts = 0  # Счетчик попыток
    while guess != number_to_guess:
        guess = int(input("Угадайте число от 1 до 100: "))
        attempts += 1
        # Даем подсказку пользователю
        if guess < number_to_guess:
            print("Загаданное число больше!")
        elif guess > number_to_guess:
            print("Загаданное число меньше!")
    # Пользователь угадал число
    print(f"Поздравляем! Вы угадали число с {attempts} попыток!")


# Задачи на for
def multiplication_table(number):
    # Вывод таблицы умножения для заданного числа
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
def sum_of_series(N):
    # Возвращает сумму числового ряда от 1 до N
    return sum(range(1, N+1))

# Задачи на функции

def celsius_to_fahrenheit(celsius):
    # Конвертирует температуру из Цельсия в Фаренгейты
    return celsius * 1.8 + 32
def calculate_bmi(height, weight):
    # Рассчитывает и возвращает индекс массы тела
    bmi = weight / (height ** 2)
    return bmi
