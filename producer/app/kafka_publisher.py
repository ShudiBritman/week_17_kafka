from confluent_kafka import Producer
from mongo_connection import MongoConnection
import json

def get_collection():
    return MongoConnection().get_collection()


producer_config = {
    "bootstrap.servers": "kafak:9092"
}
 
producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Delivered {msg.value().decode("utf-8")}")
        print(f"Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")



def send_to_kafka(data):
    producer.produce(
    topic="orders",
    value=data,
    callback=delivery_report
    )

producer.flush()
