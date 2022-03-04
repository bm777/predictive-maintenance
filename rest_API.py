import os
import json
import uvicorn
from fastapi import FastAPI
from datetime import datetime
from multiprocessing import Process
from streaming_kafka.predictive_maintenance import detect
from streaming_kafka.confluent_utils import create_producer
from parameters import TRANSACTIONS_TOPIC, DELAY, NUM_PARTITIONS

app = FastAPI()


def increment_counter():
    tmp = json.load(open("counter.json"))
    tmp["number"] += 1
    json_object = json.dumps(tmp, indent=4)

    with open("counter.json", "w") as outfile:
        outfile.write(json_object)
    return tmp["number"]

@app.on_event("startup")
async def startup_event():
    for _ in range(NUM_PARTITIONS):
        p = Process(target=detect)
        p.start()

@app.get("/event")
def get_event(data: int):

    producer = create_producer()
    response = "Empty"
    if producer is not None:
        if data is not None:
            if os.path.exists("counter.json"):

                _id = increment_counter()

                X_test = data

                current_time = datetime.utcnow().isoformat()

                record = {"id": _id, "data": X_test, "current_time": current_time}
                response = f"event message '{X_test}' is produced into the transactions topic"
                record = json.dumps(record).encode("utf-8")

                producer.produce(topic=TRANSACTIONS_TOPIC,
                                 value=record)
                producer.flush()

            else:
                response = "Error: counter.json doesn't exists"
        else:
            response = "Error: data is None in the request parameter"
    else:
        response = "Error: Producer failed to be created"



    return {
    "type": "Predictive maintenance",
    "response": response
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5400)
