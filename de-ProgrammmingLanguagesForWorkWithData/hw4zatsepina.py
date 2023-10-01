""" точки и прямоугольники """


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.P = (point_b.x - point_a.x + point_b.y - point_a.y) * 2
        self.S = (point_b.x - point_a.x) * (point_b.y - point_a.y)

    def contains(self, point_c: Point):
        return self.point_a.x <= point_c.x <= self.point_b.x and self.point_a.y <= point_c.y <= self.point_b.y


a = Point(2, 1)
b = Point(5, 3)
rectangle1 = Rectangle(a, b)
print(rectangle1.P, rectangle1.S)
c = Point(3, 2)
print(rectangle1.contains(c))

""" счетчик """


class DecimalCounter:
    def __init__(self, current):
        self.current = current

    def get_current(self):
        return self.current

    def increment(self, i: int):
        self.current += i

    def decrement(self, i: int):
        if self.current - i >= 0:
            self.current -= i
        else:
            self.current = 0


i = DecimalCounter(3)
print(i.get_current())
i.increment(1)
print(i.get_current())
i.decrement(13)
print(i.get_current())

""" часы """


class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.current_time = "%02d:%02d:%02d" % (self.hours, self.minutes, self.seconds)

    def time_plus_min(self):
        if self.minutes < 59:
            self.minutes += 1
        else:
            if self.hours < 23:
                self.minutes = 0
                self.hours += 1
            else:
                self.minutes = 0
                self.hours = 0
        self.current_time = "%02d:%02d:%02d" % (self.hours, self.minutes, self.seconds)

    def time_plus_hour(self):
        if self.hours < 23:
            self.hours += 1
        else:
            self.hours = 0
        self.current_time = "%02d:%02d:%02d" % (self.hours, self.minutes, self.seconds)

    def __add__(self, other):
        self.seconds = (self.seconds + other.seconds) % 60
        if self.seconds + other.seconds > 60:
            self.minutes = (self.seconds + other.seconds) // 60
        self.minutes = (self.minutes + other.minutes) % 60
        if self.minutes + other.minutes > 60:
            self.hours = ((self.minutes + other.minutes) // 60) % 24
        self.hours = (self.hours + other.hours) % 24
        return "%02d:%02d:%02d" % (self.hours, self.minutes, self.seconds)


t1 = Clock(23, 58, 52)
print(t1.current_time)
t1.time_plus_min()
print(t1.current_time)
t1.time_plus_min()
print(t1.current_time)
t1.time_plus_hour()
print(t1.current_time)
t2 = Clock(23, 34, 35)
t3 = t1 + t2
print(f"{t1.current_time} + {t2.current_time} = {t3}")

""" трава и травоядные """


class Grass:
    def __init__(self, grass_variety, nutritional_value):
        self.grass_variety = grass_variety
        self.nutritional_value = nutritional_value  # self.amount_of_grass = amount_of_grass


class Herbivore:
    def __init__(self, animal_breed, grass_capacity, bellyful):
        self.animal_breed = animal_breed
        self.grass_capacity = grass_capacity
        self.bellyful = bellyful

    def feeding(self, grass: Grass):
        if self.grass_capacity <= self.bellyful:
            print(f"{self.animal_breed} есть не хочет")
        else:
            if self.bellyful + grass.nutritional_value <= self.grass_capacity:
                self.bellyful += grass.nutritional_value
                print(f"{self.animal_breed} съел {grass.grass_variety} питательностью "
                      f"{grass.nutritional_value}. текущий уровень сытости: {self.bellyful}")
            else:
                self.bellyful = self.grass_capacity
                print(f"{self.animal_breed} наелся досыта")

    def activity(self, activity_points: int):
        if self.bellyful - activity_points <= 0:
            self.bellyful = 0
            print(f"{self.animal_breed} устал и ничего больше делать не будет")
        else:
            self.bellyful = self.bellyful - activity_points
            print(f"{self.animal_breed} бегал {activity_points} часа и теперь хочет есть. "
                  f"текущий уровень сытости: {self.bellyful}")


corn = Grass("кукуруза", 14)
spinach = Grass("шпинат", 8)
mint = Grass("мята", 4)
dill = Grass("укроп", 3)
cabbage = Grass("капуста", 6)
burenka = Herbivore("корова", 60, 54)
dambo = Herbivore("слон", 100, 38)
pufik = Herbivore("кролик", 10, 8)

burenka.feeding(spinach)
burenka.activity(50)
burenka.feeding(mint)

""" перемешиваем элементы """


class Water:
    element = "Вода"

    def __add__(self, other):
        if isinstance(other, Air):
            return Shtorm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()


class Air:
    element = "Воздух"

    def __add__(self, other):
        if isinstance(other, Water):
            return Shtorm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()


class Fire:
    element = "Огонь"

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()


class Earth:
    element = "Земля"

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()


class Shtorm:
    element = "Шторм"


class Steam:
    element = "Пар"


class Dirt:
    element = "Грязь"


class Lightning:
    element = "Молния"


class Dust:
    element = "Пыль"


class Lava:
    element = "Лава"


element1 = Water()
element2 = Air()
element3 = element1 + element2

print(f"{element1.element} + {element2.element} = {element3.element}")

""" исключения """


class NoMoneyToWithdrawError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PaymentError(Exception):
    def __init__(self, message):
        super().__init__(message)


class NoAccountError(Exception):
    def __init__(self, message):
        super().__init__(message)


def print_accounts(accounts):
    """Печать аккаунтов."""
    print("Список клиентов ({}): ".format(len(accounts)))
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print("{}. {} {}".format(i, name, value))


def transfer_money(accounts, account_from, account_to, value):
    """Выполнить перевод 'value' денег со счета 'account_from' на 'account_to'.

    При переводе денежных средств необходимо учитывать:
        - хватает ли денег на счету, с которого осуществляется перевод;
        - перевод состоит из уменьшения баланса первого счета и увеличения
          баланса второго; если хотя бы на одном этапе происходит ошибка,
          аккаунты должны быть приведены в первоначальное состояние
          (механизм транзакции)
          см. https://ru.wikipedia.org/wiki/Транзакция_(информатика).

    Исключения (raise):
        - NoMoneyToWithdrawError: на счету 'account_from'
                                  не хватает денег для перевода;
        - PaymentError: ошибка при переводе;
        - NoAccountError: отсутствует аккаунт.
    """
    account_from_value = accounts.get(account_from)
    if account_from_value is None:
        raise NoAccountError("Отсутствует акканут: ", account_from)

    account_to_value = accounts.get(account_to)
    if account_to_value is None:
        raise NoAccountError("Отсутствует акканут: ", account_to)

    if account_from_value < value:
        raise NoMoneyToWithdrawError(f"На аккаунте {account_from} недостаточно средств для "
                                     f"перевода")

    try:
        accounts[account_from] = account_from_value - value
        accounts[account_to] = account_to_value + value
    except Exception:
        accounts[account_from] = account_from_value
        accounts[account_to] = account_to_value
        raise PaymentError(f'Ошибка при переводе. Перевод с аккаунта {account_from} на '
                           f'аккаунт {account_to} в размере {value} отменен.')


if __name__ == "__main__":
    accounts = {"Василий Иванов": 100, "Екатерина Белых": 1500, "Михаил Лермонтов": 400}
    print_accounts(accounts)

    payment_info = {"account_from": "Екатерина Белых", "account_to": "Василий Иванов"}

    print("Перевод от {account_from} для {account_to}...".format(**payment_info))

    try:
        payment_info["value"] = int(input("Сумма = "))
        transfer_money(accounts, **payment_info)
        print("OK!")
        print_accounts(accounts)
    except ValueError:
        print("Сумма перевода введена неверно")

# """ исключние для нечисловых значений """
# def sum_of_nums(number_of_inputs: int) -> float:
#     total = float(0.0)
#     for _ in range(number_of_inputs):
#         try:
#             num = float(input("введите число: "))
#             total += num
#             print(f"текущая сумма: {total}")
#         except ValueError:
#             print("введено неподходящее значение")
#     return total
#
#
# # sum_of_nums(4)


# """ переводы оценок """
# def marks_converter():
#     marks_amount = int(input("Сколько оценок введете? "))
#     print("Вводите: ")
#     marks = [input() for _ in range(marks_amount)]
#     marks_converted = []
#
#     def numeric_to_letter(numeric):
#         numeric = int(numeric)
#         if 1 < numeric < 6:
#             if numeric == 2: return "F"
#             elif numeric == 3: return "D or E"
#             elif numeric == 4: return "B or C"
#             else: return "A"
#         else:
#             if numeric < 60: return "F"
#             elif numeric < 68: return "E"
#             elif numeric < 74: return "D"
#             elif numeric < 84: return "C"
#             elif numeric < 91: return "B"
#             else: return "A"
#
#     def letter_to_numeric(letter: str):
#         if letter == "A": return 5
#         elif letter == "B": return 4
#         elif letter == "C": return 4
#         elif letter == "D": return 3
#         elif letter == "E": return 3
#         elif letter == "F": return 3
#         else: return f"Значение {mark} не является допустимым"
#
#     for mark in marks:
#         try:
#             marks_converted.append(numeric_to_letter(mark))
#         except Exception:
#             try: marks_converted.append(letter_to_numeric(mark))
#             except Exception:
#                 print(f"Значение {mark} не является допустимым")
#     for i in range(len(marks)):
#         print(f"{marks[i]} -> {marks_converted[i]}")
#
#
# marks_converter()
