from abc import ABC, abstractmethod
import sys # Для получения информации об исключении
import traceback # Для форматирования traceback в лог
import datetime # Для добавления метки времени к логам

#--------------------------------------TASK 1----------------------------------------
class NotificationService(ABC):  # Для создания абстр. класса, необходимо создать класс, наследуя его от ABC
    @abstractmethod
    def send(self, message: str) -> None:
        pass  # Необходимо расписать метод внутри других классов


class EmailService(NotificationService):
    def send(self, message: str) -> None:
        print(f"[Email] Отправлено: {message}")

class SMSService(NotificationService):
    def send(self, message: str) -> None:
        print(f"[SMS] Отправлено: {message}")

class PushService(NotificationService):
    def send(self, message: str) -> None:
        print(f"[Push] Отправлено: {message}")

print("--- Задача 1: NotificationService ---")
# Создаем экземпляры каждого сервиса
email_notifier = EmailService()
sms_notifier = SMSService()
push_notifier = PushService()

# Определяем сообщение для отправки
test_message = "Проверка работы..."

# Отправляем сообщение через каждый сервис
email_notifier.send(test_message + "пришло на почту")
sms_notifier.send(test_message + "пришло смс")
push_notifier.send(test_message + "баннер сверху")


#--------------------------------------TASK 2----------------------------------------
class PaymentProcessor(ABC):
    @abstractmethod
    def validate_payment(self, data: dict) -> bool:  #Метод для выявления корректности номера. 
                                                    #Параметр - словарь, например {'card_number': '...', 'cvv': '...'}
        pass

    @abstractmethod
    def process_payment(self, amount: float) -> None: #Метод для выполнения платежа на указанную сумму.
        pass


class CreditCardProcessor(PaymentProcessor):
    def validate_payment(self, data: dict) -> bool: # Валидация: номер карты (16 цифр), CVV (3 или 4 цифры).
        # Проверяем наличие всех необходимых полей в данных
        if 'card_number' not in data or 'cvv' not in data:
            raise ValueError("Для кредитной карты требуются 'card_number' и 'cvv'.")

        card_number = str(data['card_number'])
        cvv = str(data['cvv'])

        if not (card_number.isdigit() and len(card_number) == 16):
            raise ValueError("Номер карты должен состоять из 16 цифр.")

        if not (cvv.isdigit() and (len(cvv) == 3 or len(cvv) == 4)):
            raise ValueError("CVV должен состоять из 3 или 4 цифр.")

        print(f"CreditCardProcessor: Данные карты валидны. (Номер: {card_number[:4]}********{card_number[-4:]})")
        return True

    def process_payment(self, amount: float) -> None:
        print(f"[Credit Card] Платеж на сумму {amount:.2f} выполнен успешно.")


class PayPalProcessor(PaymentProcessor):
    def validate_payment(self, data: dict) -> bool:
        if 'email' not in data:  # Валидация: нужен email
            raise ValueError("Для PayPal требуется 'email'.")

        email = data['email']

        if '@' not in email or '.' not in email:
            raise ValueError("Некорректный формат email для PayPal (отсутствует '@' или '.')")

        print(f"PayPalProcessor: Email валиден. ({email})")
        return True

    def process_payment(self, amount: float) -> None:
        print(f"[PayPal] Платеж на сумму {amount:.2f} выполнен успешно.")


class CryptoProcessor(PaymentProcessor):
    def validate_payment(self, data: dict) -> bool:
        if 'wallet_address' not in data:
            raise ValueError("Для криптовалютного платежа требуется 'wallet_address'.")

        wallet_address = data['wallet_address']

        # Валидация адреса кошелька: должен начинаться с 'bc1'
        if not wallet_address.startswith('bc1'):
            raise ValueError("Некорректный адрес кошелька (должен начинаться с 'bc1').")

        print(f"CryptoProcessor: Адрес кошелька валиден. ({wallet_address})")
        return True

    def process_payment(self, amount: float) -> None:
        print(f"[Crypto] Платеж на сумму {amount:.8f} выполнен успешно.")

print("--- Задача 2: PaymentProcessor ---")

credit_card_processor = CreditCardProcessor()
paypal_processor = PayPalProcessor()
crypto_processor = CryptoProcessor()

# Вспомогательная функция для удобства тестирования (внесение платжеа)
def make_payment_attempt(processor: PaymentProcessor, payment_data: dict, amount: float):
    processor_name = processor.__class__.__name__
    print(f"\n--- Попытка платежа через {processor_name} на {amount:.2f} ---")
    try:
        if processor.validate_payment(payment_data):
            processor.process_payment(amount)
    except ValueError as e:  #ошибка, связанная с неккоректными данными (например 12 цифр в номере карты)
        print(f"Ошибка валидации для {processor_name}: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка при платеже через {processor_name}: {e}")  #если с данными всё в порядке, но есть другая ошибка

# Успешный платеж
make_payment_attempt(credit_card_processor, {'card_number': '1234567890123456', 'cvv': '123'}, 100.50)
# Ошибка
make_payment_attempt(credit_card_processor, {'card_number': '214436568', 'cvv': '456'}, 50.00)
# Ошибка
make_payment_attempt(credit_card_processor, {'card_number': '1234567890123456', 'cvv': 'dsdsa'}, 10.00)

# Успешный платеж
make_payment_attempt(paypal_processor, {'email': 'user@example.com'}, 200.00)
# Ошибка
make_payment_attempt(paypal_processor, {'email': 'userexample.com'}, 75.20)


# Успешный платеж
make_payment_attempt(crypto_processor, {'wallet_address': 'bc1qxyzabc123def456ghi789jkl01234567890'}, 0.01)
# Ошибка
make_payment_attempt(crypto_processor, {'wallet_address': 'i7r7rnegilrjokfq9u4mifhlijr;gnvm;'}, 0.005)


#--------------------------------------TASK 3----------------------------------------
def process_data(data):
    # Если data — не список
    if not isinstance(data, list):
        raise TypeError("Входные данные должны быть списком.")

    # Если список пуст
    if not data:
        raise ValueError("Список не должен быть пустым.")

    # Если в списке есть нечисловые элементы
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Все элементы списка должны быть числами, найден нечисловой элемент: '{item}' (тип: {type(item).__name__}).")

    return "process_data: Обработка завершена успешно."

def run_square_program():
    result = None

    try:
        user_input = input("Введите число для возведения в квадрат: ")
        number = float(user_input)
        result = number ** 2

    except ValueError:
        print("❌ Ошибка ввода: Пожалуйста, введите число.")
    except Exception as e:
        print(f"❌ Произошла непредвиденная ошибка: {e}")
    else:
        print(f"✅ Квадрат числа {number} равен: {result}")
    finally:
        print("Операция завершена.")

print("--- Задание 3: Process_data ---")

# Успех
try:
    process_data([10, 20.5, 30])
except (TypeError, ValueError) as e:
    print(f"Ошибка при вызове process_data: {e}")

# Некорректный тип данных
try:
    process_data("привет")
except (TypeError, ValueError) as e:
    print(f"Ошибка при вызове process_data: {e}")

# Пустой список
try:
    process_data([])
except (TypeError, ValueError) as e:
    print(f"Ошибка при вызове process_data: {e}")

# Список с нечисловыми элементами
try:
    process_data([1, 2, 'три'])
except (TypeError, ValueError) as e:
    print(f"Ошибка при вызове process_data: {e}")

run_square_program()
run_square_program()
run_square_program()

#--------------------------------------TASK 4----------------------------------------
class SafeFile:
    def __init__(self, filename, mode='r', encoding=None):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self._file = None  #Внутренний объект файла

    def _log_error(self, message):  #Внутренний метод для логирования ошибок
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] ОШИБКА SafeFile ({self.filename}, {self.mode}): {message}")
        print(traceback.format_exc())  #Более подробный лог

    def __enter__(self):  #Пытается открыть файл. При ошибке логирует её и возвращает None
        try:
            self._file = open(self.filename, self.mode, encoding=self.encoding)
            print(f"Успешно открыт файл: '{self.filename}' в режиме '{self.mode}'")
            return self._file
        except IOError as e:  #IOError is an exception that signals a failure during an input/output (I/O)
            self._log_error(f"Не удалось открыть файл. {e}")
            self._file = None
            return None
        except Exception as e:   # Ловим любые другие неожиданные ошибки при открытии
            self._log_error(f"Произошла непредвиденная ошибка при открытии файла. {e}")
            self._file = None
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):  #Метод вызывается при выходе из блока 'with'. Закрывает файл, если он был успешно открыт.
        if self._file:
            self._file.close()
            print(f"Файл '{self.filename}' закрыт.")

        if exc_type:  # Если внутри блока 'with' произошло исключение
            error_details = f"Исключение типа: {exc_type.__name__}, Значение: {exc_val}"
            self._log_error(f"Ошибка произошла внутри блока 'with'. {error_details}")
            return True # Возвращаем True, чтобы подавить исключение и не прерывать программу

        return False


print("\n--- Задание 4: SafeFile ---")

test_output = 'test_output.txt'
non_existent_file = 'non_existent_file.txt'
read_only = 'read_only.txt'
another_file = 'another_file.txt'

with SafeFile(test_output, 'w') as f:
    if f: # Проверяем, что файл был успешно открыт (f не None)
        f.write("Hello, Python!.\n")
        f.write("Hello, sptcol!.\n")
        print(f"Данные успешно записаны в {test_output}.")
    else:
        print("Файл не был открыт, запись невозможна.")
print("-" * 30)


with SafeFile(non_existent_file, 'r') as f:  #Файл не существует
    if f:
        content = f.read()
        print(f"Содержимое: \n{content}")
    else:
        print(f"Файл {non_existent_file} не был открыт, чтение невозможно.")
print("-" * 30)


with open(read_only, 'w') as temp_f:  #попытка записи в файл, открытый для чтения
    temp_f.write("Привет!")
with SafeFile(read_only, 'r') as f:
    if f:
        try:
            print("Пытаемся записать в файл, открытый для чтения...")
            f.write("Попытка записи.") # Это вызовет исключение io.UnsupportedOperation
        except Exception as e:
            print(f"Попытка записи вызвала ошибку: {e}")
    else:
        print(f"Файл {read_only} не был открыт.")
print("-" * 30)


with SafeFile(another_file, 'invalid_mode') as f:  #Ошибка при передаче некорректного режима
    if f:
        f.write("The thing...")
    else:
        print(f"Файл {another_file} не был открыт из-за некорректного режима.")
