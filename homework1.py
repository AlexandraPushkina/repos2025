#--------------------------------------TASK 1----------------------------------------
import datetime
import math

class Book:
    def __init__(self, title: str, author: str, year: int):
        self._title = title
        self._author = author
        self.year = year

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int):
        current_year = datetime.datetime.now().year
        if not (1 <= value <= current_year):  #проверка: дата больше 1 и не больше текущего года
            print(f"Год издания должен быть в диапазоне от 1 до {current_year}.")
        self._year = value

    def display_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год издания: {self.year}")
        print("-" * 20)

# Создаем книгу с корректным годом
book1 = Book("Мастер и Маргарита", "М. Булгаков", 1967)
book1.display_info()

print("Изменяем год книги на 2023")
book1.year = 2023
book1.display_info()
# book1.year = 20813103 #(проверка на ошибку)

book2 = Book("Путешествие к центру Земли", "Ж. Верн", 1)
book2.display_info()
# book2.author = "Александр Пушкин" #(проверка на ошибку (@property))

#--------------------------------------TASK 2----------------------------------------
class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.__balance = initial_balance

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.__balance += amount
        print(f"Внесено: {amount:.2f}. Баланс: {self.__balance:.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self.__balance:
            raise ValueError(f"Недостаточно средств. На счету: {self.__balance:.2f}. Не хватает {amount - self.__balance:.2f}.")
        self.__balance -= amount
        print(f"Снято: {amount:.2f}. Баланс: {self.__balance:.2f}")

    def __del__(self):
        print(f"Счёт закрыт. Остаток: {self.__balance:.2f}!")

print("--- Задача 2: BankAccount ---")
try:
    account1 = BankAccount(1000.50)
    account1.deposit(500.25)
    account1.withdraw(200.00)
    account1.withdraw(2000.00)
except ValueError as e:
    print(f"Ошибка операции: {e}")

try:    
    account1.deposit(-100.00)
except ValueError as e:
    print(f"Ошибка операции: {e}")

#--------------------------------------TASK 3----------------------------------------
class Car:
    def __init__(self, brand: str, model: str, max_speed: int):
        self.__brand = brand
        self.__model = model
        self.__max_speed = max_speed
        self.__speed = 0

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, value: int):
        if not (0 <= value <= self.__max_speed):
            raise ValueError(f"Скорость должна быть от 0 до {self.__max_speed}")
        self.__speed = value

    def accelerate(self, delta: int):
        new_speed = self.__speed + delta
        self.speed = min(new_speed, self.__max_speed) # Не превышаем max_speed
        print(f"Ускорение. Текущая скорость: {self.speed}")

    def brake(self):
        self.speed = 0
        print("Торможение. Скорость: 0")

print("--- Задача 3: Car ---")
my_car = Car("Toyota", "Camry3.5", 180)
print(f"Марка: {my_car._Car__brand}, Модель: {my_car._Car__model}, Макс. скорость: {my_car._Car__max_speed}")
my_car.accelerate(50)
my_car.accelerate(150)
my_car.brake()
try:
    my_car.speed = -10 # Попытка установить отрицательную скорость
except ValueError as e:
    print(f"Ошибка: {e}")

#--------------------------------------TASK 4----------------------------------------
class Student:
    def __init__(self, name: str):
        self.__name = name
        self.__grades = []

    def add_grade(self, grade: int):
        if not (1 <= grade <= 5):
            raise ValueError("Оценка должна быть от 1 до 5.")
        self.__grades.append(grade)
        print(f"Добавлена оценка: {grade}")

    @property   #определяем propety, так как он позволяет получить его значение, просто обратившись к нему как к атрибуту
    def average_grade(self) -> float:
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)

    def __str__(self) -> str:
        return f"Студент: {self.__name}, Средний балл: {self.average_grade:.2f}"


print("--- Задача 4: Student ---")
student1 = Student("John")
student1.add_grade(4)
student1.add_grade(5)
student1.add_grade(3)
print(student1)

student2 = Student("Anna")
print(student2) # Средний балл 0.0
try:
    student2.add_grade(6)
except ValueError as e:
    print(f"Ошибка: {e}")

#--------------------------------------TASK 5----------------------------------------
class Shape:
    def __init__(self, color: str):
        self.__color = color

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, value: str):
        if not value:
            raise ValueError("Цвет не может быть пустым.")
        self.__color = value

    def area(self) -> float:
        raise NotImplementedError("NotImplementedError")

    def info(self):
        print(f"Фигура цвета {self.color}, площадь: {self.area()}")

class Rectangle(Shape):
    def __init__(self, color: str, width: float, height: float):
        super().__init__(color)
        self.__width = width
        self.__height = height

    def area(self) -> float:
        return self.__width * self.__height

# --- Пример использования ---
print("--- Задача 5: Shape ---")
try:
    # Прямоугольник
    rect = Rectangle("Пурпурный", 10, 5)
    rect.info() # Выведет информацию с площадью
    
    shape1 = Shape("")
except ValueError as e:
    print(f"Ошибка: {e}")
except NotImplementedError as e:
    print(f"Ошибка: {e}")

try:
    generic_shape = Shape("Циан")
    generic_shape.info() # Вызовет NotImplementedError
except NotImplementedError as e:
    print(f"Ошибка: {e}")

