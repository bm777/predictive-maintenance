#!/bin/bash

echo "Zookeeper & Kafka starting..."
cd kafka/
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
echo "Zookeeper & Kafka started..."
