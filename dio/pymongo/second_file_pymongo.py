import pprint

import pymongo
import pymongo as pyM

password = input("Digite a senha: ")

# Conectando
client = pyM.MongoClient(f"mongodb+srv://ar-vinicius:{password}@cluster0.cx1y4t0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.test
posts = db.posts

for post in posts.find():
    pprint.pprint(post)

print(posts.count_documents({}))
print(posts.count_documents({"author": "Mike"}))
print(posts.count_documents({"tags": "insert"}))

print("\nRecuperando info da coleção post de maneira ordenada")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

# Criando indices
result = db.profiles.create_index([('author', pymongo.ASCENDING)],
                                  unique=True)

print(sorted(list(db.profiles.index_information())))

# Criando profiles
user_profile_user = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Joao'}]

result = db.profile_user.insert_many(user_profile_user)

print("\nColeções armazenadas no mongodb")
collections = db.list_collection_names()
for collection in collections:
    print(collection)

# Removendo documentos
db['posts'].drop()

posts.delete_one({"author": "Mike"})
posts.drop()


# Deletando o bd
client.drop_database('test')
print(db.list_collection_names())
