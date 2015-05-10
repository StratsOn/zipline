#!/usr/bin/env python
from zipline.utils import run_pipeline
from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
import os
import csv


if __name__ == "__main__":
    # if not os.environ.has_key('DOCKER_HOST'):
    # os.environ['DOCKER_HOST'] = "172.17.42.1"
    sessionid = os.environ['SESSION_ID'].strip('\n')
    print "%s:9092" % os.environ['DOCKER_HOST'].strip('\n')
    client = KafkaClient("%s:9092" % os.environ['DOCKER_HOST'].strip('\n'))
    producer = SimpleProducer(client, async=True)

    #producer.send_messages("plot", "some message")

    #uid, sid, start, end, capital, code = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]
    #args = {'start': start, 'end': end, 'symbols': 'AAPL', 'source': 'yahoo', 'capital_base': float("1.0e5"), 'algo_text': code}
    #run_pipeline(print_algo=True, **args)

    with open('/data/engine/sample.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print 'plot', '{"date": %s, "close": %s, "sessionid": %s}' % (row[0], row[4], sessionid)
            producer.send_messages('plot', '{"date": "%s", "close": "%s", "sessionid": "%s"}' % (row[0], row[4], sessionid))
