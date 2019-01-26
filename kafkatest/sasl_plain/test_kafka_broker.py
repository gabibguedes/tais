from rasa_core.broker import KafkaProducer
from rasa_platform.core.tracker_store import InMemoryTrackerStore

kafka_broker = KafkaProducer(host='localhost:29092',
                             topic='rasa_core_events')

tracker_store = InMemoryTrackerStore(db=db, event_broker=kafka_broker)

