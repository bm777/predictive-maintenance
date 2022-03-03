#!/bin/bash

echo "Zookeeper & Kafka stopping..."

cd kafka/bin
./zookeeper-server-stop.sh
./kafka-server-stop.sh
echo "Zookeeper & Kafka stoped!"
