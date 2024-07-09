# main.py

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['cat_database']
collection = db['cats']

def create_cat(name, age, features):
    """Створення запису про кота."""
    cat = {"name": name, "age": age, "features": features}
    collection.insert_one(cat)
    print(f"Cat {name} added.")

def read_all_cats():
    """Виведення всіх записів із колекції."""
    cats = collection.find()
    for cat in cats:
        print(cat)

def read_cat_by_name(name):
    """Виведення інформації про кота за ім'ям."""
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"No cat found with name {name}")

def update_cat_age(name, new_age):
    """Оновлення віку кота за ім'ям."""
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.matched_count:
        print(f"Updated age for {name} to {new_age}.")
    else:
        print(f"No cat found with name {name}")

def add_cat_feature(name, feature):
    """Додавання нової характеристики до списку features кота за ім'ям."""
    result = collection.update_one({"name": name}, {"$push": {"features": feature}})
    if result.matched_count:
        print(f"Added feature '{feature}' to {name}.")
    else:
        print(f"No cat found with name {name}")

def delete_cat_by_name(name):
    """Видалення запису про кота за ім'ям."""
    result = collection.delete_one({"name": name})
    if result.deleted_count:
        print(f"Deleted cat with name {name}.")
    else:
        print(f"No cat found with name {name}")

def delete_all_cats():
    """Видалення всіх записів із колекції."""
    result = collection.delete_many({})
    print(f"Deleted {result.deleted_count} cats.")
