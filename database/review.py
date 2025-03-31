from database.connection import db
from bson import ObjectId

collection_reviews = db['reviews']  # Переконайтеся, що назва колекції правильна

def get_all_reviews():
    return list(collection_reviews.find())

def add_review(name, surname, text):
    review = {
        'name': name,
        'surname': surname,
        'text': text,
        'likes': 0
    }
    collection_reviews.insert_one(review)

def like_review(review_id):
    collection_reviews.update_one({'_id': ObjectId(review_id)}, {'$inc': {'likes': 1}})
    review = collection_reviews.find_one({'_id': ObjectId(review_id)})
    return review['likes']
