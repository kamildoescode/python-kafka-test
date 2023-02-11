# Python-kafka-test
Just a small api that you can use to produce messages in python

# Reading messages on the topic
if you want to read messages from kafka in console consumer:
cd into /opt/kafka_2.13-2.8.1/bin on the docker image
'kafka-console-consumer.sh -bootstrap-server <bootstrap-server> -topic <topic> --from-beginning
in this example:

    - <bootstrap-server> = localhost:9092
    - <topic> = message
    
    - --from-beginning will read all messages, not only updates