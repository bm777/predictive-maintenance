import socket
import logging
from parameters import KAFKA_BROKER
from confluent_kafka import Producer, Consumer


# the producer which create events
def create_producer():
    try:
        producer = Producer({"bootstrap.servers": KAFKA_BROKER,
                             "client.id": socket.gethostname(),
                             "enable.idempotence": True,    # EOS processing
                             "compression.type": "lz4",
                             "batch.size": 64000,           # default
                             "linger.ms": 10,               # defualt
                             "acks": "all",                 # Wait for the leader and all ISR to send response back
                             "retries": 5,                  # default
                             "delivery.timeout.ms": 1000})  # Total time to make retries
    except Exception as e:
        logging.exception("Could noot create the producer")
        producer = None
    return producer

# the consumer produced in Python
def create_consumer(topic, group_id):
    try:
        consumer = Consumer({"bootstrap.servers": KAFKA_BROKER,
                             "group.id": group_id,
                             "client.id": socket.gethostname(),
                             "isolation.level": "read_committed",
                             "default.topic.config": {"auto.offset.reset": "latest", # Only consume news messages
                                                      "enable.auto.commit": False}
                             })

        consumer.subscribe([topic])
    except Exception as e:
        logging.exception("Could not create the consumer")
        consumer = None

    return consumer
