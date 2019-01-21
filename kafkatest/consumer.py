import json
from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'rasa_core_events',
     bootstrap_servers=['localhost:29092'],
     value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    print("ENTROU aki")
    print("\n\n")
    print(message.value)
    print("\n\n")
