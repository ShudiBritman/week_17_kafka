from mongo_connection import MongoConnection


def get_mongo_client():
    return MongoConnection().get_client()


