from kafka import KafkaProducer
import json

TOPIC_NAME = 'message'
KAFKA_SERVER = 'localhost:9092'


class MessageProducer:
    def __init__(self):
        self._producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER,
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    def produce_message(self, _message: dict):
        print(f'Produced message = {_message}')
        self._producer.send(TOPIC_NAME, _message)
        self._producer.flush()

        return '', 202
