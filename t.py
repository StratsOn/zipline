from kafka.client import KafkaClient
from kafka.producer import SimpleProducer

client = KafkaClient("172.17.42.1:9092")
producer = SimpleProducer(client)
producer.send_messages("plot", "some message")
