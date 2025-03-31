from pprint import pprint
from typing import Optional
from pprint import pprint
from database.connection import db

# Підключення до колекції
collection_users = db['product']


def viewing_clothes(category: str, gender: Optional[str] = None):
    # Підготовка фільтра на основі категорії
    filter_query = {'category': category}

    # Додати умову для gender, якщо воно передано
    if gender is not None:
        filter_query['gender'] = gender

    # Пошук документів у колекції з використанням фільтра
    documents = collection_users.find(filter_query)

    # Виведення знайдених документів
    return list(documents)
    # for d in documents:
    #     print(d)

if __name__ == '__main__':
    # Приклад виклику функції з параметрами
    # pass
    pprint(viewing_clothes('Жіноча сукня'))
    # register_user("hn@example.com", 'Simasik')
    # user_document = db.collection_users.find_one({"email":"john@example.com"})
    # pprint(user_document)
    # view_users()
    # create_user("КАКА", "Пупкін", "ssa@sda.com", "sasa", "1111")
    # print('______________________________________')
    # view_users()
