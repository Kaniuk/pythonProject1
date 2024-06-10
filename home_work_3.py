from PIL import Image, ImageDraw


# Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані? Доступ до таких
# атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).
class Car:
    def __init__(self, make, model, year, max_speed, color):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__max_speed = max_speed
        self.__color = color

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if year > 1885:
            self.__year = year
        else:
            raise ValueError("Year must be greater than 1885")

    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, max_speed):
        if max_speed > 0:
            self.__max_speed = max_speed
        else:
            raise ValueError("Max speed must be a positive number")

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def display_info(self):
        return (f"Car make: {self.__make}, Model: {self.__model}, Year: {self.__year}, "
                f"Max Speed: {self.__max_speed} km/h, Color: {self.__color}")


car = Car("Toyota", "Camry", 2020, 240, "Red")
print(car.display_info())

car.set_year(2021)
print(car.get_year())

car.set_max_speed(250)
print(car.get_max_speed())


# Створіть 2 класи мови, наприклад, англійська та іспанська. В обох класів має бути метод greeting(). Обидва створюють
# різні привітання. Створіть два відповідні об'єкти з двох класів вище та викличте дії цих двох об'єктів в одній функції
# (функція hello_friend).

class English:
    def greeting(self):
        return "Hello!"


class Spanish:
    def greeting(self):
        return "¡Hola!"


def hello_friend():
    eng = English()
    esp = Spanish()
    print(eng.greeting())
    print(esp.greeting())


hello_friend()


# Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції, як властивості. Ознайомтеся
# з декоратором property у Python. Створіть клас, що описує температуру і дозволяє задавати та отримувати температуру за
# шкалою Цельсія та Фаренгейта, причому дані можуть бути задані в одній шкалі, а отримані в іншій.

class Temperature:
    def __init__(self, celsius=None, fahrenheit=None):
        if celsius is not None:
            self._celsius = celsius
            self._fahrenheit = self.celsius_to_fahrenheit(celsius)
        elif fahrenheit is not None:
            self._fahrenheit = fahrenheit
            self._celsius = self.fahrenheit_to_celsius(fahrenheit)
        else:
            self._celsius = 0
            self._fahrenheit = self.celsius_to_fahrenheit(0)

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value
        self._fahrenheit = self.celsius_to_fahrenheit(value)

    @property
    def fahrenheit(self):
        return self._fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._fahrenheit = value
        self._celsius = self.fahrenheit_to_celsius(value)


temp = Temperature(celsius=25)
print(f"Температура: {temp.celsius}°C / {temp.fahrenheit}°F")

temp.fahrenheit = 77
print(f"Температура: {temp.celsius}°C / {temp.fahrenheit}°F")

temp.celsius = 0
print(f"Температура: {temp.celsius}°C / {temp.fahrenheit}°F")


# Опишіть два класи Base та його спадкоємця Child з методами method(), який виводить на консоль фрази відповідно ("Hello "
# "from Base") та "Hello from Child", using classmethod (@classmethod) decorator.

class Base:
    @classmethod
    def method(cls):
        print("Hello from Base")


class Child(Base):
    @classmethod
    def method(cls):
        print("Hello from Child")


Base.method()
Child.method()


# example_7.py


class Shape:
    def __init__(self):
        # Колір тла
        self.back_color = (155, 213, 117, 100)
        # Створюємо зображення 500 * 500
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def draw(self):
        pass

    def erase(self):
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Background was created")
        return self.im.save('picture.png', quality=95)


class Circle(Shape):
    def draw(self):
        self.draw1.ellipse((75, 100, 175, 200), fill='yellow', outline=(255, 255, 255))

    def erase(self):
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)

    def save(self):
        print("Image with circle was created")
        return self.im.save('draw-circle.png', quality=95)


class Square(Shape):
    def draw(self):
        self.draw1.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))

    def erase(self):
        self.draw1.rectangle((200, 200, 300, 200), fill=self.back_color)

    def save(self):
        print("Image with square was created")
        return self.im.save('draw-square.png', quality=95)


class Triangle(Shape):
    def draw(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=(255, 255, 255))

    def erase(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)

    def save(self):
        print("Image with triangle was created")
        return self.im.save('draw-triangle.png', quality=95)


class Paraboloid(Shape):
    def draw(self):
        self.draw1.polygon([(250, 50), (200, 200), (300, 200)], fill='green', outline=(255, 255, 255))
        self.draw1.ellipse((200, 180, 300, 220), fill='green', outline=(255, 255, 255))

    def erase(self):
        self.draw1.polygon([(250, 50), (200, 200), (300, 200)], fill=self.back_color)
        self.draw1.ellipse((200, 180, 300, 220), fill=self.back_color)

    def save(self):
        print("Image with paraboloid was created")
        return self.im.save('draw-paraboloid.png', quality=95)


def work_with_obj(obj):
    obj.draw()
    obj.save()


def update_obj(obj):
    obj.erase()
    obj.save()


def menu():
    while True:
        value = int(
            input('\nМЕНЮ:\n\t1. Cтворити тло\n\t2. Cтворити коло\n\t3. Cтворити квадрат\n\t4. Cтворити трикутник'
                  '\n\t5. Зафарбувати коло\n\t6. Зафарбувати квадрат\n\t7. Зафарбувати трикутник'
                  '\n\t8. Cтворити параболоїд\n\t9. Зафарбувати параболоїд\n\t10. Вихід з програми\nОберіть необхідний пункт меню: '))
        match value:
            case 1:
                s = Shape()
                s.save()
            case 2:
                c = Circle()
                work_with_obj(c)
            case 3:
                sq = Square()
                work_with_obj(sq)
            case 4:
                t = Triangle()
                work_with_obj(t)
            case 5:
                c = Circle()
                update_obj(c)
            case 6:
                sq = Square()
                update_obj(sq)
            case 7:
                t = Triangle()
                update_obj(t)
            case 8:
                para = Paraboloid()
                work_with_obj(para)
            case 9:
                para = Paraboloid()
                update_obj(para)
            case 10:
                break
            case _:
                print('Оберіть пункт меню корректно!!!')


if __name__ == '__main__':
    menu()

paraboloid = Paraboloid()
work_with_obj(paraboloid)
update_obj(paraboloid)
