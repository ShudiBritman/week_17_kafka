from mongo_connection import MongoConnection


def get_mongo_client():
    return MongoConnection().get_client()


def pull_batches(skip):
    coll = get_mongo_client()
    projection = {'_id':0}
    cursor = list(coll.find({},projection).skip(skip).limit(30))
    return cursor
