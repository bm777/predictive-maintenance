import os
import json
import logging
import numpy as np
from joblib import load
from multiprocessing import Process
from streaming_kafka.confluent_utils import create_producer, create_consumer
from parameters import TRANSACTIONS_TOPIC, TRANSACTIONS_CONSUMER_GROUP, ANOMALIES_TOPIC, NORMALS_TOPIC, NUM_PARTITIONS

def detect():
    consumer = create_consumer(topic=TRANSACTIONS_TOPIC, group_id=TRANSACTIONS_CONSUMER_GROUP)
    producer = create_producer()

    while True:
        message = consumer.poll(timeout=50)
        if message is None:
            continue

        if message.error():
            logging.error("Consumer error: {}".format(message.error()))
            continue

        # Message that came from producer
        record = json.loads(message.value().decode('utf-8'))
        data = record["data"]

        prediction = data # prediction operation

        # If an anomaly comes in, send it to anomalies topic
        if isinstance(prediction, str):
            score = [[0.9]]
            record["score"] = score

            _id = str(record["id"])
            record = json.dumps(record).encode("utf-8")

            producer.produce(topic=ANOMALIES_TOPIC, value=record)
            producer.flush()

        else:
            score = [[0.2]]
            record["score"] = score

            _id = str(record["id"])
            record = json.dumps(record).encode("utf-8")

            producer.produce(topic=NORMALS_TOPIC, value=record)
            producer.flush()



        # consumer.commit() # Uncomment this, to process all messages, not just new ones

    consumer.close()

# One consumer per partition (we have 3 partition, 1 suffices)
for _ in range(NUM_PARTITIONS):
    p = Process(target=detect)
    p.start()
