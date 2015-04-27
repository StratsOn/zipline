#!/usr/bin/env python
from zipline.utils import run_pipeline
from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
import sys


if __name__ == "__main__":
    client = KafkaClient("localhost:9092")
    producer = SimpleProducer(client)

    #producer.send_message("plot", "some message")

    uid, sid, start, end, capital, code = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]
    args = {'start': start, 'end': end, 'symbols': 'AAPL', 'source': 'yahoo', 'capital_base': float("1.0e5"), 'algo_text': code}
    run_pipeline(print_algo=True, **args)