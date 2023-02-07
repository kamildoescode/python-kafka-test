from kafka import KafkaProducer
import time

TOPIC_NAME = 'item'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)


while True:
    producer.send(TOPIC_NAME, b'HELLO')
    producer.flush()

    time.sleep(1)