students = {
    "Petrenko": ["Ivan", "Shevchenko 12", 1, 10] ,
    "Sydorenko": ["Maria", "Heroes of Ukraine 7", 2, 11],
    "Kovalchuk": ["Petro", "Heroes of Ukraine 25", 1, 11],
    "Melnik": ["Olena", "Tarasivska 9", 3, 11],
    "Kovalenko": ["Andriy", "Soborna 14", 2, 10],
    "Shevchenko": ["Oleksandr", "Hrushevskoho 30", 3, 11],
    "Prokopenko": ["Tetiana", "Hrushevskoho 5", 1, 10],
    "Bondarenko": ["Oleg", "Stepana Bandery 17", 2, 11],
    "Kravchenko": ["Iryna", "Shevchenko 3", 1, 10],
    "Pavlenko": ["Victor", "Kirova 11", 3, 10],
}

def Print(students):
    for prizv, dani in students.items():
        print(f"Прізвище: {prizv}, ім'я: {dani[0]}, адреса: {dani[1]}, номер школи: {dani[2]}, номер класу: {dani[3]}")


def add(students):
    new_prizv = str(input("Введіть прізвище: "))
    new_name = str(input("Введіть ім'я: "))
    new_adress = str(input("Введіть адресу: "))
    new_school = int(input("Введіть номер школи: "))
    new_class = int(input("Введіть номер класу: "))

    students[new_prizv] = [new_name, new_adress, new_school, new_class]

def Del(students, key):
    try:
        del students[key]
        print("Видалено", key, ".")
    except KeyError:
        print("Помилка: Неможливо знайти запис з прізвищем", key)

def print_sort(students):
    students = {k: students[k] for k in sorted(students)}
    print("Відсортований словник: ")
    Print(students)


def find(students, result):
    wanted_school = int(input("Введіть номер школи: "))
    for prizv, dani in students.items():
        if dani[2] == wanted_school and dani[3] >= 10:
            result[prizv] = [dani[0], dani[1]]

    if not result:
        print("Немає учнів старших класів в даній школі.")
    else:
        for prizv, dani in result.items():
            print(f"Прізвище: {prizv}, ім'я: {dani[0]}, адреса: {dani[1]}")





while True:
    print("\nЯкщо ви бажаєте виведення усіх значень словника, тоді натисніть [1]")
    print("Якщо ви бажаєте добавити новий запис до словника, тоді натисніть [2]")
    print("Якщо ви бажаєте видалення запису із словника, тоді натисніть [3]")
    print("Якщо ви бажаєте перегляду вмісту словника за відсортованими ключами, тоді натисніть [4]")
    print("Якщо ви бажаєте побачити інформацію про учнів старших класів, які навчаються в конкретній школі , тоді натисніть [5]")
    print("Вихід з програми, натисніть [0]\n")

    n = int(input("Введіть опцію: "))

    if n == 1:
        Print(students)
    elif n == 2:
        add(students)
    elif n == 3:
        delete_k = input("Введіть прізвище для видалення: ")
        Del(students, delete_k)
    elif n == 4:
        print_sort(students)
    elif n == 5:
        result = {}
        find(students, result)
    elif n == 0:
        print("Вихід з програми")
        break
    else:
        print("Невірно вказана операція")
