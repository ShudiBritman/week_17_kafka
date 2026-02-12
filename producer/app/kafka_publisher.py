from confluent_kafka import Producer
import logging
import json


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

producer_config = {
    'bootstrap.servers':'kafka:9092',
    'acks':'all'}


producer = Producer(producer_config)
logger = logging.getLogger(__name__)

def delivery_report(err, msg):
    if err:
        logger.error("Delivery failed: %s", err)
    else:
        logger.info(
            "Delivered message: %s",
            msg.value().decode("utf-8")
        )
        logger.info(
            "Delivered to %s | partition %s | offset %s",
            msg.topic(),
            msg.partition(),
            msg.offset()
        )



def send_event_to_kafka(event):
        value = json.dumps(event)
        producer.produce(
            topic='users_posts.registered',
            value=value,
            callback=delivery_report
        )
        logger.info("seeding from file in batches of 10 every 5 seconds")
        producer.poll(0)


        producer.flush()
        return 



