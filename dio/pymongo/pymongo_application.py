import datetime
import pymongo as pyM

# Conectando
client = pyM.MongoClient("mongodb+srv://ar-vinicius:<password>@cluster0.cx1y4t0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

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
