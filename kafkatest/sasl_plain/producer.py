from kafka import KafkaProducer
import json
import random
from time import sleep
from datetime import datetime

# Create an instance of the Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:29093',
                         value_serializer=lambda v: str(v).encode('utf-8'),
                         sasl_plain_username='admin',
                         sasl_plain_password='admin-secret',
                         sasl_mechanism='PLAIN',
                         security_protocol='SASL_PLAINTEXT')

# Call the producer.send method with a producer-record
print("Ctrl+c to Stop")
while True:
    producer.send('kafka-python-topic', random.randint(1,999))
