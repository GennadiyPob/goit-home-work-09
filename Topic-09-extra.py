
#функція обробки помилок

def input_error(func):
    # Декоратор для обробки помилок введення користувача.
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a correct name"  # Обробляє помилку відсутності ключа.
        except ValueError:
            return "Invalid input. Enter please correct name and phone"  # Обробляє неправильний формат вводу.
        except IndexError:
            return "Invalid input format. Use 'add', 'change', or 'phone' before entered data"  # Обробляє неправильний формат команди.
    return wrapper


@input_error
def add_contact(contacts, name, phone):
    # Додаємо контакт у словник
    contacts[name] = phone

@input_error
def change_phone(contacts, name, new_phone):
    # Змінюємо номер телефону для існуючого контакту
    if name in contacts:
        contacts[name] = new_phone
    else:
        raise ValueError(f"Contact '{name}' not found")

@input_error
def get_phone(contacts, name):
    # Отримуємо номер телефону за ім'ям контакту
    if name in contacts:
        return contacts[name]
    else:
        raise ValueError(f"Contact '{name}' not found")

def show_all_contacts(contacts):
    # Виводимо всі збережені контакти у консоль
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    # Ініціалізуємо словник для зберігання контактів (ім'я - номер телефону).
    contacts = {}
    print("Hello!")
    print("How can I help you?")
    while True:
        command = input().strip().lower()
        if command == "good bye" or command == "close" or command == "exit":
            # Завершуємо роботу бота, якщо користувач ввів одну з команд виходу.
            print("Good bye!")
            break
        elif command == "hello":
            # Виводимо привітання і запитуємо, як можемо допомогти.
            print("How can I help you?")
        elif command.startswith("add "):
            try:
                # Розбиваємо команду "add" на окремі слова.
                _, name, phone = command.split(" ", 2)
                add_contact(contacts, name, phone)
                print(f"Added contact: {name}")
            except ValueError:
                print("Enter name and phone, e.g., 'add Ivan 12345'")
        elif command.startswith("change "):        #зміна контактних даних
            try:
                # Розбиваємо команду "change" на окремі слова
                _, name, new_phone = command.split(" ", 2)
                change_phone(contacts, name, new_phone)
                print(f"Changed phone for {name}")
            except ValueError:
                print("Enter name and new phone, e.g., 'change Ivan 112233'")
        elif command.startswith("phone "):
            try:
                # Розбиваємо команду "phone" на окремі слова
                _, name = command.split(" ", 1)
                phone = get_phone(contacts, name)
                print(f"Phone for {name}: {phone}")
            except ValueError:
                print("Enter a valid name, e.g., 'phone John'")
        elif command == "show all":
            # Виводимо всі контакти
            show_all_contacts(contacts)
        else:
            # Якщо введена невідома команда, виводимо повідомлення про невідповідність
            print("Unknown command. Type 'hello' for assistance.")

if __name__ == "__main__":
    # Запускаємо бота
    main()