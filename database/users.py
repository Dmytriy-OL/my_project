from pprint import pprint
from database.connection import db
import hashlib

# Підключення до колекції користувачів
collection_users = db['users']


def view_users():
    """
    Виводить усіх користувачів із бази даних.

    Функція отримує всі документи з колекції 'users' та друкує їх.
    """
    documents = collection_users.find()
    for doc in documents:
        print(doc)


def searching_user(login: str):
    """
    Шукає користувача в базі даних за логіном.

    :param login: Логін користувача
    :return: Документ користувача або None, якщо не знайдено
    """
    return collection_users.find_one({"login": login})


def update_user(login: str, new_data: dict):
    """
    Оновлює дані користувача у базі даних.

    :param login: Логін користувача, якого потрібно оновити
    :param new_data: Нові дані у форматі словника
    """
    collection_users.update_one({"login": login}, {"$set": new_data})


def register_user(email: str, login: str):
    """
    Перевіряє, чи є користувач у базі даних за email або логіном.

    :param email: Електронна адреса користувача
    :param login: Логін користувача
    :return: True, якщо користувач існує, інакше False
    """
    user_document = collection_users.find_one({"$or": [{"email": email}, {"login": login}]})
    return bool(user_document)


def create_user(name: str, surname: str, email: str, login: str, password: str):
    """
    Створює нового користувача та зберігає його в базі даних.

    Пароль перед збереженням хешується для безпеки.

    :param name: Ім'я користувача
    :param surname: Прізвище користувача
    :param email: Електронна адреса користувача
    :param login: Логін користувача
    :param password: Пароль користувача
    """
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    user = {
        "surname": surname,
        "name": name,
        "email": email,
        "login": login,
        "password_hash": password_hash  # Збережений хеш пароля
    }
    collection_users.insert_one(user)


def password_verification(login: str, password: str):
    """
    Перевіряє правильність пароля користувача.

    :param login: Логін користувача
    :param password: Введений пароль
    :return: True, якщо пароль правильний, інакше False
    """
    user = collection_users.find_one({"login": login})

    if user:
        stored_password_hash = user.get("password_hash", "")
        input_password_hash = hashlib.sha256(password.encode()).hexdigest()
        return stored_password_hash == input_password_hash
    return False


if __name__ == '__main__':
    pass
    # print(password_verification('vasiliq', '1111'))
    # register_user("hn@example.com", 'Simasik')
    # user_document = db.collection_users.find_one({"email": "john@example.com"})
    # pprint(user_document)
    # view_users()
    # create_user("Василь", "Пупкін", "vasa@vt.com", "vasiliq", "1111")
    # print('______________________________________')
    # view_users()
