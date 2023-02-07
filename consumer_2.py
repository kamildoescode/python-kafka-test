from kafka import KafkaConsumer

TOPIC_NAME = 'item'
AUTO_OFFSET_RESET = 'earliest' #read all messages on the topic
KAFKA_SERVER = 'localhost:9092'

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers = KAFKA_SERVER, auto_offset_reset = AUTO_OFFSET_RESET)

for message in consumer:
    print(message)