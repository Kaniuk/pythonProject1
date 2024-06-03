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

    print(book3 == book4)  # book3.__eq__(book4)
    print(book3 == book2)
    print(book3 != book4)  # book3.__nq__(book4)
    print(book3 != book2)
    print(book)
    print(book2)
