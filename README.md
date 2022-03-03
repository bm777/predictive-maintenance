# predictive-maintenance
predictive maintenance using ML, hosted by FastAPI and Kafka

# settings

#### 0. Set up the kafka env

```
$ bash server-cron-start.sh
```

#### 1. Create the transactions, anomalies and normals topics in Kafka Consumer

```
$ cd kafka
$ bin/kafka-topics.sh --create --topic transactions --bootstrap-server localhost:9092
$ bin/kafka-topics.sh --create --topic anomalies --bootstrap-server localhost:9092
$ bin/kafka-topics.sh --create --topic normals --bootstrap-server localhost:9092
```

We can check our topics created by this command `kafka-topics.sh --zookeeper localhost:9092 --list`, they should be three.


#### 2. Start the producer (from our distributed users)

```
streaming/producer.py
```
