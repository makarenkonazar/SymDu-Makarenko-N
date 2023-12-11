import json

class Student:
    def __init__(self, last_name, first_name, address, school_number, attendance_day):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.school_number = school_number
        self.attendance_day = attendance_day

students_data = [
    {"last_name": "Ivanenko", "first_name": "Ivan", "address": "Main St, 1", "school_number": 1, "attendance_day": "Saturday"},
    {"last_name": "Petrenko", "first_name": "Mariya", "address": "Oak St, 22", "school_number": 2, "attendance_day": "Sunday"},
    {"last_name": "Kovalenko", "first_name": "Oleksandr", "address": "Sunny St, 45", "school_number": 3, "attendance_day": "Saturday"},
    {"last_name": "Sydorenko", "first_name": "Anna", "address": "River St, 10", "school_number": 2, "attendance_day": "Sunday"},
    {"last_name": "Hryhorenko", "first_name": "Vasyl", "address": "Polar St, 7", "school_number": 1, "attendance_day": "Saturday"},
    {"last_name": "Melnychenko", "first_name": "Yevheniya", "address": "Meadow St, 30", "school_number": 2, "attendance_day": "Sunday"},
    {"last_name": "Kuzmenko", "first_name": "Dmytro", "address": "Star St, 12", "school_number": 2, "attendance_day": "Saturday"},
    {"last_name": "Oliynyk", "first_name": "Olena", "address": "Garden St, 18", "school_number": 3, "attendance_day": "Sunday"},
    {"last_name": "Tkachenko", "first_name": "Maxym", "address": "Spring St, 25", "school_number": 3, "attendance_day": "Saturday"},
    {"last_name": "Shevchenko", "first_name": "Sofiya", "address": "Summer St, 14", "school_number": 1, "attendance_day": "Sunday"},
]
def search(students, criterion, value):
    result = []
    for student in students:
        if criterion in student.__dict__ and student.__dict__[criterion] == value:
            result.append(student)
    return result

x = json.dumps(students_data, ensure_ascii=False, indent=2)
with open("Lab.json", "wt") as file:
    file.write(x)
file.close()

with open("Lab.json", 'r') as file:
    data = json.load(file)
    students = [Student(**student) for student in data]

while True:
    print("\nОберіть опцію:")
    print("1. Вивести вміст JSON файлу")
    print("2. Додати нового учня")
    print("3. Видалити учня за прізвищем")
    print("4. Пошук учнів за критерієм")
    print("5. Вийти")

    choice = input("Ваш вибір: ")
    if choice == '1':
        with open("Lab.json", 'r') as file:
            json_content = file.read()
            print(json_content)
        file.close()

    elif choice == '2':
        last_name = input("Прізвище: ")
        first_name = input("Ім'я: ")
        address = input("Адреса: ")
        school_number = int(input("Номер школи: "))
        attendance_day = input("День відвідування (Saturday/Sunday): ")
        students.append(Student(last_name, first_name, address, school_number, attendance_day))
        with open("Lab.json", 'w') as file:
            json.dump([student.__dict__ for student in students], file, ensure_ascii=False, indent=2)

    elif choice == '3':
        last_name = input("Прізвище учня для видалення: ")
        students = [student for student in students if student.last_name != last_name]
        with open("Lab.json", 'w') as file:
            json.dump([student.__dict__ for student in students], file, ensure_ascii=False, indent=2)

    elif choice == '4':
        criterion = input("Оберіть критерій пошуку (last_name, first_name, address, school_number, attendance_day): ")
        value = input(f"Введіть значення {criterion}: ")
        result = search(students, criterion, value)
        for student in result:
            print(f"Прізвище: {student.last_name}, Ім'я: {student.first_name}, Адреса: {student.address}")

    elif choice == '5':
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")