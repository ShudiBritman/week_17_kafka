from kafka_consumer import ensure_topic_exists, create_consumer, consume_loop
from db import init_db



def main():
    init_db()
    ensure_topic_exists()
    consumer = create_consumer()
    consume_loop(consumer)


if __name__ == "__main__":
    main()
