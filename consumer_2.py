from kafka import KafkaConsumer

TOPIC_NAME = 'item'
consumer = KafkaConsumer(TOPIC_NAME)

for message in consumer:
    print(message)