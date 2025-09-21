from confluent_kafka import Producer
import time

conf = {
    'bootstrap.servers': 'localhost:9092',  # change to your broker(s)
}

producer = Producer(conf)

topic = "test"

def delivery_report(err, msg):
    """Delivery callback confirming success or failure"""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

# Send 10 text messages
for i in range(2):
    message = f"Hello Kafka! Message {i}"
    producer.produce(topic, value=message.encode("utf-8"), callback=delivery_report)
    producer.poll(0)  # Trigger delivery callbacks
    time.sleep(1)

# Wait for all messages to be delivered
producer.flush()
