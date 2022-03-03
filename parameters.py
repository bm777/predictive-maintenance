import os
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.token')
load_dotenv(dotenv_path)

DELAY = 0.01        # delay for event to be created in while True loop
NUM_PARTITIONS = 3
KAFKA_BROKER = "localhost:9092"
TRANSACTIONS_TOPIC = f"{os.environ.get("MAIN_TOPIC")}"
TRANSACTIONS_CONSUMER_GROUP = f"{os.environ.get("MAIN_TOPIC")}"
ANOMALIES_TOPIC = "anomalies"
ANOMALIES_CONSUMER_GROUP = "anomalies"
NORMALS_TOPIC = "normals"
NORMALS_CONSUMER_GROUP = "normals"
