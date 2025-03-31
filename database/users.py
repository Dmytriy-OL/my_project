from pprint import pprint
from database.connection import db
import hashlib

# Підключення до колекції
collection_users = db['users']


def view_users():
    documments = collection_users.find()
    for doc in documments:
        print(doc)


def searching_user(login: str):
    user = collection_users.find_one({"login": login})
    return user


def update_user(login: str, new_data: dict):
    collection_users.update_one({"login": login}, {"$set": new_data})


# перевірка чи є даний користувач у базі даних
def register_user(email: str, login: str):
    user_document = collection_users.find_one({"$or": [{"email": email}, {"login": login}]})
    return bool(user_document)


def create_user(name: str, surname: str, email: str, login: str, password: str):
    # Хешуємо пароль перед збереженням у базі даних
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    user = {
        "surname": surname,
        "name": name,
        "email": email,
        "login": login,
        "password_hash": password_hash  # Зберігаємо хеш паролю
    }
    collection_users.insert_one(user)


def password_verification(login: str, password: str):
    # Отримати користувача з бази даних за логіном
    user = collection_users.find_one({"login": login})

    # Перевірка, чи є користувач з таким логіном
    if user:
        # Отримати хеш пароля користувача з бази даних
        stored_password_hash = user.get("password_hash", "")

        # Хешування введеного пароля
        input_password_hash = hashlib.sha256(password.encode()).hexdigest()

        # Порівняти хеші паролів
        if stored_password_hash == input_password_hash:
            return True  # Пароль вірний
    return False


if __name__ == '__main__':
    pass
    # print(password_verification('vasiliq', '1111'))
    # register_user("hn@example.com", 'Simasik')
    # user_document = db.collection_users.find_one({"email":"john@example.com"})
    # pprint(user_document)
    # view_users()
    #  create_user("Василь", "Пупкін", "vasa@vt.com", "vasiliq", "1111")
    # print('______________________________________')
    # view_users()
