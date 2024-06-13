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
