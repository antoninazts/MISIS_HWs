import re
from datetime import datetime, date, timedelta


def calculate_lsm(list_of_nums: list) -> int:
    lsm = max(list_of_nums)
    while True:
        suit = 0
        for x in list_of_nums:
            if lsm % x != 0:
                lsm += 1
                break
            suit += 1
        if suit == len(list_of_nums):
            return lsm


def calculate_hcf(list_of_nums: list) -> int:
    hcf = min(list_of_nums)
    while True:
        suit = 0
        for x in list_of_nums:
            if x % hcf != 0:
                hcf -= 1
                break
            suit += 1
        if suit == len(list_of_nums):
            return hcf


def amount_of_sentences_with_digits(text: str) -> int:
    amount = 0
    list_of_sentences = text.split(". ")
    for sentence in list_of_sentences:
        if re.search("\d+", sentence) is not None:
            amount += 1
    return amount


def draw_k_frame(s: str): 
    print("-" * (len(s) + 2))
    print(s.center(len(s) + 2, "|"))
    print("-" * (len(s) + 2))
    # todo все работает, только ты не подаешь по условию задачи символ k в параметрах
    # чтобы именно этот символ рисовал рамку


def letter_statistics(s: str):
    result = {letter: 0 for letter in list(s.lower())}
    for letter in list(s.lower()):
        result[letter] += 1
    for keys, values in result.items():
        print(f"{keys}: {values}")


def caesar_cipher(s: str) -> str: # todo нет дешифровщика
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    encrypted_s = ""
    shift = 1 # todo добавил бы в аргумент метода, чтобы контролировать насколько хочу сместить
    s = s.upper()
    for letter in s:
        if letter in alphabet:
            i = (alphabet.find(letter) + shift) % len(alphabet)
            encrypted_s += alphabet[i]
        else:
            encrypted_s += letter
    return encrypted_s


def neg_pos_lists(*args):
    pos_args = list()
    neg_args = list()
    for arg in args:
        if arg >= 0:
            pos_args.append(arg)
        else:
            neg_args.append(arg)
    return sorted(pos_args), sorted(neg_args, reverse=True)


def palindrome_or_not(s: str) -> bool:
    palindrome_bool = False
    counter = 0
    for i in range(1, len(s) // 2 + 1):
        if s[i - 1] != s[-i]:
            return palindrome_bool
        else:
            if counter < len(s) // 2 - 1:
                counter += 1
            else:
                palindrome_bool = True
                return palindrome_bool
# todo все отлично работает, но как мне кажется чуть громоздко,
# нужно разбирать зачем нужен counter при первом взгляде на код, примеры ниже более кратки
#      def is_palindrome(a: str):
#          palindrome_bool = False
#          for i in range(0, (len(a) // 2)):
#             if a[i] == a[len(a) - i - 1]:
#                 palindrome_bool = True
#              else:
#                  return False
#         return flag
#  или так
#     def is_palindrome(a: str):
#         flag = False
#         for i in range(1, (len(a) // 2) + 1):
#             if a[i - 1] == a[-i]:
#                 flag = True
#             else:
#                 return False
#         return flag


def number_search() -> int:
    range_of_nums = [x for x in range(1, 101)]
    left_pointer = 0
    right_pointer = len(range_of_nums)
    middle = (left_pointer + right_pointer) // 2   #todo можно один раз объявить в цикле, что не писать многократно
    answer = 0                                     #todo не используется переменная, она не нужна за пределами цикла
    print(f'''
        Вы загадываете число от 1 до 100 (включительно). Компьютер спрашивает у вас 
        «Твое число равно, меньше или больше, чем число N?»,  
        где N — число, которое хочет проверить компьютер.
        Вы отвечаете одним из трёх чисел:
        1 — равно, 2 — больше, 3 — меньше
    ''')
    while True:
        answer = int(input(f"Твое число равно, меньше или больше, чем число"
                           f" {range_of_nums[middle]}? "))
        if answer == 1:
            return range_of_nums[middle]
        else:
            if answer == 2:
                left_pointer = middle
                middle = (left_pointer + right_pointer) // 2
            else:
                right_pointer = middle
                middle = (left_pointer + right_pointer) // 2


def from_10_to_16(number):
    decimal_number = int(number)
    hexadecimal_digits = "0123456789ABCDEF"
    hexadecimal_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_digit = hexadecimal_digits[remainder]
        hexadecimal_number = hexadecimal_digit + hexadecimal_number
        decimal_number //= 16
    return hexadecimal_number


def from_10_to_2(number):
    decimal_number = int(number)
    binary_number_list = []
    binary_number = ""
    while decimal_number > 0:
        binary_number_list.append(decimal_number % 2)
        decimal_number //= 2
    for el in binary_number_list:
        binary_number += str(el)
    return binary_number


def from_10_to_8(number):
    decimal_number = int(number)
    octal_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 8
        octal_number = str(remainder) + octal_number
        decimal_number = decimal_number // 8
    return octal_number


def from_2_to_10(number):
    binary_number_list = list(number)
    decimal_number = 0
    power = len(binary_number_list) - 1
    for el in binary_number_list:
        decimal_number += int(el) * 2 ** power
        power -= 1
    return decimal_number


def from_16_to_10(number):
    hexadecimal_number = number
    decimal_number = 0
    power = 0
    for i in range(len(hexadecimal_number) - 1, -1, -1):
        digit = hexadecimal_number[i]
        if digit.isdigit():
            value = int(digit)
        else:
            value = ord(digit.upper()) - ord('A') + 10
        decimal_number += value * (16 ** power)
        power += 1
    return decimal_number


def from_8_to_10(number):
    octal_number = int(number)
    decimal_number = 0
    power = 0
    while octal_number != 0:
        digit = octal_number % 10
        decimal_number += digit * (8 ** power)
        power += 1
        octal_number //= 10
    return decimal_number


def convert_systems():                                            #todo не поодерживает все системы счисления от 2 до 16
    system_from = int(input("из какой системы? (числом 2/8/10/16) "))
    system_to = int(input("в какую систему? (числом 2/8/10/16) "))
    number = str(input("значение: "))
    if system_from == 10 and system_to == 16:
        print(f"Шестнадцатеричное число: {from_10_to_16(number)}")
    elif system_from == 10 and system_to == 2:
        print(f"Двоичное число: {from_10_to_2(number)}")
    elif system_from == 10 and system_to == 8:
        print(f"Восьмеричное число: {from_10_to_8(number)}")
    elif system_from == 2 and system_to == 10:
        print(f"Десятичное число: {from_2_to_10(number)}")
    elif system_from == 2 and system_to == 16:
        print(f"Шестнадцатеричное число: {from_10_to_16(from_2_to_10(number))}")
    elif system_from == 2 and system_to == 8:
        print(f"Восьмеричное число: {from_10_to_8(from_2_to_10(number))}")
    elif system_from == 16 and system_to == 10:
        print(f"Десятичное число: {from_16_to_10(number)}")
    elif system_from == 16 and system_to == 2:
        print(f"Двоичное число: {from_10_to_2(from_16_to_10(number))}")
    elif system_from == 16 and system_to == 8:
        print(f"Восьмеричное число: {from_10_to_8(from_16_to_10(number))}")
    elif system_from == 8 and system_to == 10:
        print(f"Десятичное число: {from_8_to_10(number)}")
    elif system_from == 8 and system_to == 2:
        print(f"Двоичное число: {from_10_to_2(from_8_to_10(number))}")
    elif system_from == 8 and system_to == 16:
        print(f"Шестнадцатеричное число: {from_10_to_16(from_8_to_10(number))}")
    else:
        return 0


def magic_date_generate():
    start_date = date(1900, 1, 1)
    end_date = date(1999, 12, 31)
    delta = end_date - start_date
    magic_dates = [start_date + timedelta(x) for x in range(delta.days + 1) if
                   (start_date + timedelta(x)).day * (start_date + timedelta(x)).month == (
                           start_date + timedelta(x)).year % 100]
    return magic_dates


""" ***** вызовы функций ***** """
"""
# НОК
nums_lsm = [3, 15, 4, 5]
print(calculate_lsm(nums_lsm))
# НОД
nums_hcf = [36, 12, 144, 18]
print(calculate_hcf(nums_hcf))

# Количество предложений с цифрами
text_with_digits = "Магическими называются даты, в которых произведение дня и месяца составляет " \
                   "последние две цифры года. Например, 10 июня 1960 года – магическая дата, " \
                   "поскольку 10 ´ 6 = 60. Напишите функцию, определяющую, является ли введенная" \
                   "дата магической. Используйте написанную функцию в главной программе для " \
                   "отображения всех магических дат в 20 веке."
print(amount_of_sentences_with_digits(text_with_digits))

# рамка вокруг фразы
draw_k_frame(" а теперь получилась рамка? ")

# количество повторений символов в предложении
str_for_statictics = "Для введенного предложения выведите статистику символ = количество. Регистр букв не учитывается."
letter_statistics(str_for_statictics)

# шифрование Цезаря
print(caesar_cipher("Используя шифр Цезаря"))

# разбиение аргументов на положительный и отрицательный списки
print(neg_pos_lists(-1, 3, 2, 9, -19, -7, 7))

# палиндром или нет?
print(palindrome_or_not("anna"))

# поиск числа за 7 шагов
print(f"Вы загадали число {number_search()}")

# конвертор системам исчисления
convert_systems()

# генератор списка магических дат
print(*magic_date_generate(), sep="\n")
"""
