# predictive-maintenance
predictive maintenance using ML, hosted by FastAPI and Kafka

# settings
Try to clone the repo.

```
git clone https://github.com/bm777/predictive-maintenance.git
```

#### 0. Set up the kafka env

```
cd kafka
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
```

#### 1. Create the transactions, anomalies and normals topics in Kafka Consumer

```
cd kafka
bin/kafka-topics.sh --create --topic transactions --bootstrap-server localhost:9092
bin/kafka-topics.sh --create --topic anomalies --bootstrap-server localhost:9092
bin/kafka-topics.sh --create --topic normals --bootstrap-server localhost:9092
```

We can check our created topics by this command `kafka-topics.sh --bootstrap-server localhost:9092 --list`, they should be three.


#### 2. Start the producer (from our distributed users)

```
python streaming_kafka/producer.py
```
#### 3. Start the predictive maintenance

```
python predictive_maintenance.py
```

#### 4. Alterts bot to slack (building...)
