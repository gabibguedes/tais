import json
from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'kafka-python-topic',
     bootstrap_servers=['localhost:29095'],
     value_deserializer=lambda m: json.loads(m.decode('utf-8')),
     sasl_plain_username='admin',
     sasl_plain_password='admin-secret',
     sasl_mechanism='PLAIN',
     security_protocol='SASL_PLAINTEXT')

for message in consumer:
    print("ENTROU aki")
    print("\n\n")
    print(message.value)
    print("\n\n")
