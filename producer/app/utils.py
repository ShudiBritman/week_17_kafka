from kafka_publisher import send_event_to_kafka



def send_batches_to_producer(batch):
    for doc in batch:
        send_event_to_kafka(doc)
    return