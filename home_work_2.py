# Створіть клас Editor, який містить методи view_document та edit_document. Нехай метод edit_document виводить на екран
# інформацію про те, що редагування документів недоступне для безкоштовної версії. Створіть підклас ProEditor, у якому цей
# метод буде перевизначено. Введіть ліцензійний ключ із клавіатури і, якщо він коректний, створіть екземпляр класу ProEditor
# , інакше Editor. Викликайте методи перегляду та редагування документів.

class Editor:
    def view_document(self):
        print('Перегляд документу')

    def edit_document(self):
        print('редагування документів недоступне для безкоштовної версії')


class ProEditor(Editor):
    def edit_document(self):
        print('редагування документів недоступне для безкоштовної версії')


def editor_type():
    valid_key = '523'

    enter_key = input('Enter valid key\n')

    if enter_key == valid_key:
        editor = ProEditor()
    else:
        editor = Editor()

    editor.view_document()
    editor.edit_document()


if __name__ == "__main__":
    editor_type()


# Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші. Опишіть клас кнопки.
# Створіть об'єкт кнопки та звичайного прямокутника. Викличте метод натискання на кнопку.

class GrapObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"GraphicalObject at ({self.x}, {self.y})"


class Rectangle(GrapObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}"


class ClickObject:
    def clickObject(self):
        print('The object was clicked!')


class Button(Rectangle, ClickObject):
    def __init__(self, x, y, width, height, label):
        Rectangle.__init__(self, x, y, width, height)
        self.label = label

    def __str__(self):
        return f"Button '{self.label}' at ({self.x}, {self.y}) with width {self.width} and height {self.height}"

    def clickObject(self):
        print(f"Button '{self.label}' was clicked")


button = Button(10, 10, 10, 10, 'open')
rectangle = Rectangle(20, 20, 30, 30, )

print(button)
print(rectangle)

button.clickObject()


# Створіть ієрархію класів із використанням множинного успадкування. Виведіть на екран порядок вирішення методів для
# кожного класу. Поясніть, чому лінеаризація даних класів виглядає саме так.



class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")

class C(A):
    def method(self):
        print("C.method")

class D(B, C):
    def method(self):
        print("D.method")

print("MRO for class D:", D.mro())

a = A()
b = B()
c = C()
d = D()

print("Calling method for each class:")
a.method()
b.method()
c.method()
d.method()
