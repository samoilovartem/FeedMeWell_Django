import pymongo
import certifi
import local_settings


client = pymongo.MongoClient(local_settings.MONGO_URI, tlsCAFile=certifi.where())
db = client[local_settings.MONGO_DB]
collection = local_settings.MONGO_DB_COLLECTION
