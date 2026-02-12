from kafka_publisher import send_event_to_kafka
import time



def send_batches_to_producer(batch):
    for doc in batch:
        send_event_to_kafka(doc)
        time.sleep(0.5)
    return