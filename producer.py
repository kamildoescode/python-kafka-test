import time, json, random
from datetime import datetime
from generator import generate_message
from kafka import KafkaProducer


TOPIC = 'messages'

# def serialiser(message):
#     return json.dumps(message).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers = ['localhost:9092'],
    # value_serializer = serialiser
    value_serializer = lambda x: json.dumps(x).encode('utf-8')
)

if __name__ == '__main__':
    while True:
        message = generate_message()

        print(f'{datetime.now()} | Producing message {message}')
        producer.send(TOPIC, message)
        # producer.flush()

        time.sleep(1)