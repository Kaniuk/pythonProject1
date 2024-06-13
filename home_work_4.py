class InvalidInputError(Exception):
    pass


class ZeroDivisionError(Exception):
    pass


class NegativeExponentError(Exception):
    pass


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Помилка: ділення на нуль!")
    return x / y


def power(x, y):
    if x == 0 and y < 0:
        raise NegativeExponentError("Помилка: піднесення нуля до негативного степеня!")
    return x ** y


def calculator():
    while True:
        print("\nОберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Піднесення до степеня")
        print("6. Вихід")

        choice = input("Введіть номер операції (1/2/3/4/5/6): \n")

        if choice == '6':
            print("Програма завершена.")
            break

        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Введіть перше число: "))
                num2 = float(input("Введіть друге число: "))
            except ValueError:
                print("Помилка: введено некоректні дані!")
                continue

            try:
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"{num1} ** {num2} = {power(num1, num2)}")
            except (ZeroDivisionError, NegativeExponentError) as e:
                print(e)
        else:
            print("Помилка: некоректний вибір операції!")


if __name__ == "__main__":
    calculator()


#
# Опишіть клас співробітника, який вміщує такі поля: ім('я, прізвище, відділ і рік початку роботи. Конструктор має'
# ' генерувати виняток, якщо вказано неправильні дані. Введіть список працівників із клавіатури. Виведіть усіх'
#                                                       ' співробітників, які були прийняті після цього року.)


class InvalidEmployeeDataError(Exception):
    pass


class Employee:
    def __init__(self, first_name, last_name, department, start_year):
        if not first_name or not last_name or not department or not isinstance(start_year, int) or start_year < 1900:
            raise InvalidEmployeeDataError("Invalid data provided for employee.")
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.start_year = start_year

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Department: {self.department}, Start Year: {self.start_year}"


def input_employees():
    employees = []
    while True:
        try:
            first_name = input("Enter first name (or 'q' to quit): ")
            if first_name.lower() == 'q':
                break
            last_name = input("Enter last name: ")
            department = input("Enter department: ")
            start_year = int(input("Enter start year: "))
            employee = Employee(first_name, last_name, department, start_year)
            employees.append(employee)
        except InvalidEmployeeDataError as e:
            print(e)
        except ValueError:
            print("Start year must be an integer.")
    return employees


def display_employees_hired_after(employees, year):
    for employee in employees:
        if employee.start_year > year:
            print(employee)


if __name__ == "__main__":
    employees = input_employees()
    year = int(input("Enter the year to filter employees hired after: "))
    display_employees_hired_after(employees, year)


#
# Створіть програму спортивного комплексу, у якій передбачене меню: 1 - перелік видів спорту, 2 - команда тренерів, 3 -
# розклад тренувань, 4 - вартість тренування. Дані зберігати у словниках. Також передбачити пошук по прізвищу тренера,
# яке вводиться з клавіатури у відповідному пункті меню. Якщо ключ не буде знайдений, створити відповідний клас-Exception,
# який буде викликатися в обробнику виключень.

class CoachNotFoundError(Exception):
    pass


sports = {
    1: "Basketball",
    2: "Swimming",
    3: "Tennis",
    4: "Soccer"
}

coaches = {
    "Smith": {"sport": "Basketball", "experience": "10 years"},
    "Johnson": {"sport": "Swimming", "experience": "8 years"},
    "Williams": {"sport": "Tennis", "experience": "6 years"},
    "Brown": {"sport": "Soccer", "experience": "12 years"}
}

schedules = {
    "Basketball": "Mon, Wed, Fri - 6:00 PM to 8:00 PM",
    "Swimming": "Tue, Thu - 7:00 AM to 9:00 AM",
    "Tennis": "Mon, Wed, Fri - 5:00 PM to 7:00 PM",
    "Soccer": "Tue, Thu - 4:00 PM to 6:00 PM"
}

costs = {
    "Basketball": "$50 per session",
    "Swimming": "$40 per session",
    "Tennis": "$45 per session",
    "Soccer": "$35 per session"
}


def display_sports():
    print("List of sports:")
    for key, value in sports.items():
        print(f"{key}. {value}")


def display_coaches():
    print("Coaching staff:")
    for name, details in coaches.items():
        print(f"Name: {name}, Sport: {details['sport']}, Experience: {details['experience']}")


def display_schedule():
    print("Training schedule:")
    for sport, schedule in schedules.items():
        print(f"{sport}: {schedule}")


def display_cost():
    print("Training cost:")
    for sport, cost in costs.items():
        print(f"{sport}: {cost}")


def search_coach(last_name):
    if last_name in coaches:
        coach = coaches[last_name]
        print(f"Coach {last_name} - Sport: {coach['sport']}, Experience: {coach['experience']}")
    else:
        raise CoachNotFoundError(f"Coach with last name '{last_name}' not found.")


def menu():
    while True:
        print(
            "\nMENU:\n1. List of sports\n2. Coaching staff\n3. Training schedule\n4. Training cost\n5. Search coach by last name\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            display_sports()
        elif choice == '2':
            display_coaches()
        elif choice == '3':
            display_schedule()
        elif choice == '4':
            display_cost()
        elif choice == '5':
            last_name = input("Enter coach's last name: ")
            try:
                search_coach(last_name)
            except CoachNotFoundError as e:
                print(e)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    menu()
