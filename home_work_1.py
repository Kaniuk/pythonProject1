# Створіть клас, який описує відгук до книги. Додайте до класу книги поле список відгуків. Зробіть так, щоб при виведенні
# книги на екран за допомогою функції print також виводилися відгуки до неї
class Genre:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Genre({self.name}, {self.description})"

    def __str__(self):
        return self.name


class Review:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"Review({self.text})"

    def __str__(self):
        return self.text


class Author:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def __eq__(self, other):
        if not isinstance(other, Author):
            raise TypeError(f"Cannot compare Author with {type(other)}")
        return self.last_name == other.last_name and self.first_name == other.first_name

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return f"Author({self.first_name}, {self.last_name}, {self.birth_date})"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
        return f"{self.first_name} {self.last_name}"


class Book:
    def __init__(self, authors: list[Author], title: str, year, genre: Genre, reviews: list[Review] = []):
        self.authors = authors
        self.title = title
        self.year = year
        self.genre = genre
        self.reviews = reviews

    def __repr__(self):
        return f"Book({self.authors}, {self.title}, {self.year}, {self.genre})"

    def __str__(self):
        reviews_str = "\n".join([str(review) for review in self.reviews])
        return (f"{self.title} by {', '.join([str(author) for author in self.authors])} ({self.year}) \n"
                f"Reviews: \n{reviews_str if reviews_str else 'No reviews yet.'}")

    # def __eq__(self, other):
    #     if not isinstance(other, Book):
    #         raise TypeError(f"Cannot compare Book with {type(other)}")
    #     return self.authors == other.authors and self.title == other.title
    #     return self.title == other.title and set(self.authors) == set(other.authors)
    #
    # def __ne__(self, other):
    #     return not self == other
    #     # return not self.__eq__(other)
    #
    # def __repr__(self):
    #     return f"Book({self.authors}, {self.title}, {self.year}, {self.genre},{self.reviews})"
    #
    # def __str__(self):
    #     return f"({self.title} by {self.authors} {self.year})"


if __name__ == "__main__":
    fantasy = Genre("Fantasy",
                    "A genre of speculative fiction set in a fictional universe, often inspired by real world myth and folklore.")
    author = Author("J. R. R.", "Tolkien", "1892-01-03")
    author2 = Author("George R. R.", "Martin", "1948-09-20")
    review1 = Review('An epic tale of adventure and friendship.')
    review2 = Review("A must-read for fantasy lovers.")

    book = Book([author], "The Lord of the Rings", 1954, fantasy, [review1])
    book2 = Book([author2], "A Game of Thrones", 1996, fantasy, )
    book3 = Book([author, author2], "The Hobbit", 1937, fantasy, )
    book4 = Book([author2, author], "The Hobbit", 1937, fantasy, )

    # print(book3 == book4)  # book3.__eq__(book4)
    # print(book3 == book2)
    # print(book3 != book4)  # book3.__nq__(book4)
    # print(book3 != book2)
    print(book)
    print(book2)


# Створіть клас, який описує автомобіль. Створіть клас автосалону, що містить в собі список автомобілів,
# доступних для продажу, і функцію продажу заданого автомобіля.

class Car:
    def __init__(self, id: int, model: str, year: int, max_speed: int, color: str):
        self.id = id
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.color = color

    def __repr__(self):
        return f"Car({self.id}, {self.model}, {self.year}, {self.max_speed}, {self.color})"

    def __str__(self):
        return f"Car ID: {self.id}, Model: {self.model}, Year: {self.year}, Max Speed: {self.max_speed} km/h, Color: {self.color}"


class CarDealership:
    def __init__(self, cars: list[Car]):
        self.cars = cars

    def sale_car(self, car_id):
        for car in self.cars:
            if car.id == car_id:
                self.cars.remove(car)
                return car
        return None

    def add_car(self, new_car):
        if new_car.id < 0:
            raise ValueError('Id field must be greater 0')
        for car in self.cars:
            if car.id == new_car.id:
                raise ValueError('Id already exist!')
        self.cars.append(new_car)

    def __repr__(self):
        return f"CarDealership({self.cars})"

    def __str__(self):
        return "\n".join(
            str(car) for car in self.cars)


car1 = Car(1, 'BMW', 2006, 150, 'black')
car2 = Car(2, 'Lanos', 2000, 120, 'white')
car3 = Car(3, 'Zaporoszes', 1956, 100, 'green')
car4 = Car(4, 'Ford', 2005, 150, 'blue')
car5 = Car(5, 'Mercedes', 2020, 200, 'red')

car_list = CarDealership([car1, car2, car3, car4, car5])

new_car = Car(6, 'DDD', 1996, 120, 'blue')
car_list.add_car(new_car)

print(car_list)

sold_car = car_list.sale_car(2)
print(sold_car)

print(car_list)
