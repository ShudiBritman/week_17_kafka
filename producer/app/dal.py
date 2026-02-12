from mongo_connection import MongoConnection


def get_mongo_client():
    return MongoConnection().get_client()


def pull_batches(skip: int, limit: int):
    coll = get_mongo_client()
    projection = {'_id':0}
    cursor = (
        coll.find({}, projection)
        .sort("time_insertion", 1)
        .skip(skip)
        .limit(limit)
    )
    return list(cursor)
