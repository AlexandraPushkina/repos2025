#--------------------------------------TASK 1----------------------------------------
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Внесено: {amount:.2f}. Баланс: {self.__balance:.2f}")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Снято: {amount}. Баланс: {self.__balance}")
        else:
            print(f"Недостаточно средств. На счету: {self.__balance:.2f}. Не хватает {amount - self.__balance:.2f}.")

    def display_info(self):
        print(f"Баланс: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, initial_balance, interest_rate):
        super().__init__(initial_balance)  # Вызов конструктора родительского класса (добавлен __interest_rate)
        self.__interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self.__interest_rate

    def display_info(self):
        super().display_info()  # Вызов метода родителя для вывода базовой информации
        print(f"Interest Rate: {self.interest_rate}%")

print("--- Savings Account ---")
savings = SavingsAccount(1000, 5)
savings.display_info()
savings.deposit(500)
savings.withdraw(200)

#--------------------------------------TASK 2----------------------------------------

class Course:
    def __init__(self, title, duration):
        self.__title = title
        self.__duration = duration

    @property
    def title(self):
        return self.__title

    @property
    def duration(self):
        return self.__duration

    def get_info(self):
        return f"Курс: {self.title}, Длительность: {self.duration} час(ов)"

class PremiumCourse(Course):
    def __init__(self, title, duration, mentor):
        super().__init__(title, duration)
        self.__mentor = mentor

    @property
    def mentor(self):
        return self.__mentor
    
    def get_info(self):
        # Получаем строку от родительского метода и добавляем к ней новую информацию
        base_info = super().get_info()
        return f"{base_info}\nПреподаватель: {self.mentor}"  # Заменила на русский "Преподаватель"

print("\n--- Course ---")
# Обычный курс
basic_course = Course("ООП в Питоне", 10)
print(basic_course.get_info())

# Премиум-курс
premium_course = PremiumCourse("Чистый код. Питон", 25, "Ильнур А.")
print(premium_course.get_info())

#--------------------------------------TASK 3----------------------------------------
class Animal:
    def __init__(self, name):
        self.__name = name
        
    @property
    def name(self):
        return self.__name

    def make_sound(self):
        return "Некий звук"

    def display_info(self):
        print(f"Имя: {self.name}")


class Pet(Animal):
    def __init__(self, name, owner):
        super().__init__(name)
        self.__owner = owner

    @property
    def owner(self):
        return self.__owner

    def make_sound(self):
        return f"{self.name} издает милый звук :3."  # Заменила на русский язык

    def display_info(self):
        super().display_info()
        print(f"Владелец: {self.owner}")

print("--- Animal ---")
animal = Animal("Лев")
animal.display_info()
print(f"Звук: {animal.make_sound()}")


pet = Pet("Пушок-пирожок", "Александра")
pet.display_info()
print(f"Звук: {pet.make_sound()}")


#--------------------------------------TASK 4----------------------------------------
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def area(self): # Площадь
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def side(self):
        return self.width

print("\n--- Rectangle ---")
rect = Rectangle(10, 5)
print(f"Прямоугольник: Ширина={rect.width}, Высота={rect.height}, Площадь={rect.area}")

square = Square(7)
print(f"Квадрат: Сторона={square.side}, Ширина={square.width}, Площадь={square.area}")

#--------------------------------------TASK 5----------------------------------------
class User:
    def __init__(self, username, email):
        self.__username = username
        self.__email = email

    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email

    def display_info(self):
        print(f"Пользователь: {self.username}, Email: {self.email}")


class Admin(User):
    def __init__(self, username, email, admin_level):
        super().__init__(username, email)
        if not 1 <= admin_level <= 3:
            raise ValueError("Уровень администратора должен быть в диапазоне от 1 до 3.")
        self.__admin_level = admin_level

    @property
    def admin_level(self):
        return self.__admin_level

    def display_info(self):
        super().display_info()
        print(f"Уровень доступа: {self.admin_level}")

print("\n--- User ---")
user = User("alexandra_p", "alexandrap@gmail.com")
user.display_info()
admin = Admin("admin_user", "admin@corp.com", 2)
admin.display_info()

# Пример с неверным уровнем доступа
try:
    invalid_admin = Admin("admin", "admin@corp.com", 5)
except ValueError as e:
    print(f"\nОшибка создания администратора: {e}")
