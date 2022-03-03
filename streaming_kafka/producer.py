import json
import time
import random
import numpy as np
from datetime import datetime
from streaming_kafka.confluent_utils import create_producer
from settings import TRANSACTIONS_TOPIC, DELAY, OUTLIERS_GENERATION_PROBABILITY

_id = 0
producer = create_producer()

if producer is not None:

    fake_data = ["Noor", "Victor", "Yusuf", "Bayang", 123, 152, 555]
    while True:
        # Generate some wrong good case to simulate normal and abnormal behavior
        for_pred = random.choice(fake_data)

        X_test = for_pred

        current_time = datetime.utcnow().isoformat()

        record = {"id": _id, "data": X_test, "current_time": current_time}
        record = json.dumps(record).encode("utf-8")

        producer.produce(topic=TRANSACTIONS_TOPIC,
                         value=record)
        producer.flush()
        _id += 1
        time.sleep(DELAY)
