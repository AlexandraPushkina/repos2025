#--------------------------------------TASK 1----------------------------------------
class Car:
    total_cars = 0

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        Car.total_cars += 1

    @staticmethod
    def is_vintage(year: int) -> bool:
        return 2025 - year > 30

    def __repr__(self) -> str:
        return f"Car(brand={self.brand}, model={self.model}, year={self.year})"

print("--- Задача 1: Car ---")

car1 = Car("Toyota", "Camry35", 2020)
car2 = Car("Ford", "Mustang", 1969)
car3 = Car("Honda", "Civic", 2010)

print(f"Total cars created: {Car.total_cars}")
print(f"Is Camry35 vintage? {Car.is_vintage(car1.year)}")
print(f"Is Mustang vintage? {Car.is_vintage(car2.year)}")
print(repr(car1))
print(repr(car2))
print(repr(car3))

#--------------------------------------TASK 2----------------------------------------

class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @staticmethod
    def from_fahrenheit(f: float) -> 'Temperature':
        celsius = (f - 32) * 5 / 9
        return Temperature(celsius)

    @staticmethod
    def from_kelvin(k: float) -> 'Temperature':
        celsius = k - 273.15
        return Temperature(celsius)

    def __add__(self, other):
        if isinstance(other, Temperature):
            return Temperature(self.celsius + other.celsius)
        elif isinstance(other, (int, float)):
            return Temperature(self.celsius + other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Temperature):
            return Temperature(self.celsius - other.celsius)
        elif isinstance(other, (int, float)):
            return Temperature(self.celsius - other)
        else:
            return NotImplemented

    def __repr__(self) -> str:
        return f"Temperature(celsius={self.celsius:.2f})"
    
print("--- Задача 2: Temperature ---")

temp_celsius = Temperature(25.0)
temp_fahrenheit = Temperature.from_fahrenheit(451)
temp_kelvin = Temperature.from_kelvin(77.0)

print(repr(temp_celsius))
print(repr(temp_fahrenheit))
print(repr(temp_kelvin))

sum_temp = temp_celsius + temp_fahrenheit
diff_temp = temp_kelvin - 10

print(f"Sum of celsius and fahrenheit: {repr(sum_temp)}")
print(f"Kelvin minus 10 degrees: {repr(diff_temp)}")

#--------------------------------------TASK 3----------------------------------------

class Student:
    next_id = 1

    def __init__(self, name: str):
        if not Student.validate_name(name):
            raise ValueError("Name must contain only letters and not be empty.")
        self.name = name
        self.student_id = Student.next_id
        Student.next_id +=1

    @staticmethod
    def validate_name(name: str) -> bool:
        return name.isalpha()

    def __eq__(self, other) -> bool:
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    def __hash__(self) -> int:
        return hash(self.student_id)

    def __repr__(self) -> str:
        return f"Student(name='{self.name}', student_id={self.student_id})"

# Task 3
print("--- Задача 3: Student ---")
try:
    student1 = Student("Alice")
    student2 = Student("Bob")
    student3 = Student("Alice") # Will have a different ID
    student4 = Student("Charlie")

    print(student1)
    print(student2)
    print(student3)
    print(student4)

    print(f"Are student1 and student3 equal? {student1 == student3}") # False, Разные ID при создании
    print(f"Are student1 and student3 equal? {student1 == student4}") # False
    student5 = Student("Alexandra")
    student6 = Student("Alexandra")
    student5.student_id = student6.student_id # Вручную присвоим ID Alexandra другой Alexandra
    print(f"Are s_test1 and s_test2 equal (by ID)? {student5 == student6}") # True

    students_set = {student1, student2, student3, student4, student5, student6}
    print(f"Set of students: {students_set}")
    print(f"Number of unique students in set: {len(students_set)}")

    invalid_student = Student.validate_name("123") # не создаст, тк есть цифры
    print(f"Is '123' a valid name? {invalid_student}")
    print(f"Is 'Alice123' a valid name? {Student.validate_name('Alice123')}") # False
    print(f"Is '' a valid name? {Student.validate_name('')}") # False

except ValueError as e:
    print(f"Error creating student: {e}")

#--------------------------------------TASK 4----------------------------------------

class Rectangle:
    count = 0

    def __init__(self, width: float, height: float):
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative.")
        self.width = width
        self.height = height
        Rectangle.count += 1

    @staticmethod
    def is_square(width: float, height: float) -> bool:
        return width == height

    @property
    def area(self) -> float:
        return self.width * self.height

    def __mul__(self, factor: float) -> 'Rectangle':
        if factor < 0:
            raise ValueError("Scaling factor cannot be negative.")
        new_width = self.width * factor
        new_height = self.height * factor
        return Rectangle(new_width, new_height)

    def __str__(self) -> str:
        return f"Rectangle with width {self.width} and height {self.height}"

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"

# Task 4
print("--- Задача 4: Rectangle ---")
try:
    rect1 = Rectangle(10, 20)
    rect2 = Rectangle(5, 5)
    rect3 = Rectangle(10, 20)

    print(f"Total rectangles created: {Rectangle.count}")
    print(f"Is rect2 a square? {Rectangle.is_square(rect2.width, rect2.height)}")
    print(f"Is rect1 a square? {Rectangle.is_square(rect1.width, rect1.height)}")

    print(f"Area of rect1: {rect1.area}")
    print(f"Area of rect2: {rect2.area}")

    scaled_rect = rect1 * 2
    print(f"Scaled rect1: {repr(scaled_rect)}")
    print(repr(rect1))
    print(str(rect1))
    print(repr(rect2))

    print(f"Are rect1 and rect3 equal (by value)? {rect1.width == rect3.width and rect1.height == rect3.height}") # True
except ValueError as e:
    print(f"Error creating rectangle: {e}")

# Task 5
class Library:
    books = []

    def __init__(self):
        pass

    def add_book(self, title: str, author: str):
        book_info = {"title": title, "author": author}
        self.books.append(book_info)

    @staticmethod
    def format_book_info(title: str, author: str) -> str:
        return f"«{title}» by {author}"

    def __len__(self) -> int:
        return len(self.books)

    def __getitem__(self, index: int) -> dict:
        if 0 <= index < len(self.books):
            return self.books[index]
        else:
            raise IndexError("Index out of range.")

    def __contains__(self, title: str) -> bool:
        for book in self.books:
            if book["title"] == title:
                return True
        return False

    def __repr__(self) -> str:
        return f"Library with {len(self.books)} books."

print("--- Задача 5: Library ---")
library = Library()
library.add_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
library.add_book("1984", "George Orwell")
library.add_book("Pride and Prejudice", "Jane Austen")
library.add_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams") # Adding a duplicate to show it's just added again

print(Library.format_book_info("Dune", "Frank Herbert"))

print(f"Number of books in library: {len(library)}")
print(f"Book at index 1: {library[1]}")
print(f"Book at index 0: {library[0]}")
print(f"Is '1984' in library? {'1984' in library}")
print(f"Is 'Brave New World' in library? {'Brave New World' in library}")

print(library)