def task_01():
    print("Задание 1.")
    a = [1, 5, 3]
    b = [1, 5, 1, 5]
    c = [1, 3, 1, 5, 3, 3]
    a.extend(b)
    print(a.count(5))
    # a = list(filter(lambda x: x != 5, a))
    a = list(x for x in a if x != 5)
    a.extend(c)
    print(a.count(3))
    print(a)


def task_02():
    print(f"\nЗадание 2.")
    class1 = list(x for x in range(160, 177, 2))
    class2 = list(x for x in range(162, 181, 3))
    print(list(set(class1 + class2)))


def task_03():
    print(f"\nЗадание 3.")
    shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500],
            ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
    shop_dict = dict()
    for i in shop:
        if i[0] not in shop_dict:
            shop_dict[i[0]] = [i[1]]
        else:
            shop_dict[i[0]].append(i[1])
    i = input("Введите название детали: ")
    print(
        f'Название детали: {i}\nК-во деталей: {len(shop_dict[i])}\nОбщая стоимость: {sum(shop_dict[i])}\n')


def task_04():
    print(f"\nЗадание 4.")
    guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    # name = str()
    while True:
        new = input("Гость пришеш или ушел? ")
        if new == "пришел":
            name = input("Имя гостя: ")
            if len(guests) < 6:
                guests.append(name)
                print(f"Привет, {name}!")
                print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
            else:
                print(f"Прости, {name}, мест нет.")
        elif new == "ушел":
            name = input("Имя гостя: ")
            if name in guests:
                guests.remove(name)
                print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
            else:
                print("такого гостя нет")
        elif new == "пора спать":
            print("Вечеринка закончилась, все легли спать.")
            break
        else:
            print("посмотри в задании, что можно вводить")
            break


def task_05():
    print(f"\nЗадание 5.")
    violator_songs = [['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43],
                      ['Personal Jesus', 4.56], ['Halo', 4.9], ['Waiting for the Night', 6.07],
                      ['Enjoy the Silence', 4.20], ['Policy of Truth', 4.76], ['Blue Dress', 4.29],
                      ['Clean', 5.83]]
    violator_songs_dict = dict((s[0], s[1]) for s in violator_songs)
    n = int(input("Сколько песен выбрать? "))
    m = 0
    for i in range(n):
        m += violator_songs_dict[input(f"Название {i + 1}-й песни: ")]
    print(f"Общее время звучания песен: {round(m, 2)} минуты")


def task_06():
    a1 = list()
    a2 = list()
    for _ in range(3):
        a1.append(int(input(f"Введите {_ + 1}-е число для первого списка: ")))
    for _ in range(7):
        a2.append(int(input(f"Введите {_ + 1}-е число для второго списка: ")))
    print("Первый список: ", a1)
    print("Второй список: ", a2)
    a3 = set(a1 + a2)
    print("Новый список с уникальными элементами: ", a3)


def task_07():
    n_skates = int(input("Кол-во коньков: "))
    skates = list()
    people = list()
    match = 0
    for i in range(n_skates):
        skates.append(int(input(f"Размер {i + 1}-й пары: ")))
    n_people = int(input("\nКол-во людей: "))
    for i in range(n_people):
        people.append(int(input(f"Размер ноги {i + 1}-го человека: ")))
    for i in range(min(n_skates, n_people)):
        if max(people) > max(skates):
            people.remove(max(people))
        else:
            match += 1
            people.remove(max(people))
            skates.remove(max(skates))
    print("Наибольшее кол-во людей, которые могут взять ролики: ", match)


def task_08():
    n8 = int(input("Кол-во человек: "))
    k8 = int(input("Какое число в считалке? "))
    people = list(i + 1 for i in range(n8))
    # it_people = people.__iter__()
    print(people)
    i = 0
    while len(people) > 1:
        print("\nТекущий круг людей: ", people)
        print("Начало счёта с номера: ", people[i])
        rm_id = (i + k8 - 1) % len(people)
        print("Выбывает человек под номером: ", people[rm_id])
        people.remove(people[rm_id])
        i = rm_id % len(people)
    print('Остался человек под номером:', people[0])


def task_09():
    a = 1


# task_01()
# task_02()
# task_03()
# task_04()
# task_05()
# task_06()
# task_07()
# task_08()
task_09()  # task_10()
