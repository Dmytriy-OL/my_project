from pymongo import MongoClient


# Підключення до локального сервера MongoDB
client = MongoClient('localhost', 27017)

# Перевірка підключення
# client.admin.command('ping')
# print("Підключення до MongoDB встановлено успішно.")

# Підключення до бази даних
db = client['shop']