from flask import Flask
from flask import request

from MessageProducer import MessageProducer

app = Flask(__name__)

producer = MessageProducer()

@app.route('/', methods = ['GET'])
def default_route():
    return 'Nothing to see here'

@app.route('/api/produce', methods=['POST'])
def produce_message():
    return producer.produce_message(request.get_json())


if __name__ == '__main__':
    app.run()