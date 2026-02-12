import logging
import os
import json
from confluent_kafka import Consumer
from confluent_kafka.admin import AdminClient, NewTopic
from dal import insert_doc

logger = logging.getLogger(__name__)

BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP", "kafka:9092")
TOPIC_NAME = os.getenv("TOPIC_NAME", "users-orders.registered")


def ensure_topic_exists():
    admin = AdminClient({'bootstrap.servers': BOOTSTRAP_SERVERS})
    topic = NewTopic(
        topic=TOPIC_NAME,
        num_partitions=1,
        replication_factor=1
    )
    admin.create_topics([topic])


def create_consumer():
    config = {
        'bootstrap.servers': BOOTSTRAP_SERVERS,
        'group.id': 'user-orders-tracker',
        'auto.offset.reset': 'earliest'
    }
    return Consumer(config)


def handle_message(msg):
    value = msg.value().decode('utf-8')
    try:
        user = json.loads(value)
        
    except Exception as e:
        logger.exception(e)


def consume_loop(consumer):
    consumer.subscribe([TOPIC_NAME])
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            if msg.error():
                logger.error(msg.error())
                continue

            docs = handle_message(msg)
            insert_doc(docs)

    finally:
        consumer.close()
