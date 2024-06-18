import datetime
import pprint

import pymongo as pyM

password = input("Digite a senha: ")

# Conectando
client = pyM.MongoClient(f"mongodb+srv://ar-vinicius:{password}@cluster0.cx1y4t0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.test
collection = db.test_collection
print(db.test_collection)

# Definindo o arquivo para compor o documento
post = {
    "author": "Mike",
    "text": "My first MongoDB application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.now()
}

# Preparando para submeter as infos
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

# print(db.posts.find_one())
# Mostra a estrutura de forma indentada
pprint.pprint(db.posts.find_one())

# Criando outro documento
# bulk inserts
new_posts = [{
    "author": "Mike",
    "text": "Another post",
    "tags": ["bulk", "post", "insert"],
    "date": datetime.datetime.now()
    },
    {
    "author": "Joao",
    "text": "Post from Joao. New post available",
    "title": "Mongo is fun",
    "date": datetime.datetime(2009,11,10,10,45)
    }]

result = posts.insert_many(new_posts)
print(result.inserted_ids)

print("\nRecuperação Final")
pprint.pprint(db.posts.find_one({"author": "Joao"}))

print("\nDocumentos presentes na coleção posts")
for post in posts.find():
    pprint.pprint(post)
