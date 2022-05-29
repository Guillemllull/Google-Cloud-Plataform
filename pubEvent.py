# -*- coding: utf-8 -*-
"""
Created on Tue May 24 09:39:01 2022

@author: Usuario
"""

import time
from google.cloud import pubsub_v1

project_id = "cloud-madm"
topic_id_search = "search"
topic_id_buy = "buy"
topic_id_book = "book"

publisher = pubsub_v1.PublisherClient()
topic_path_book = publisher.topic_path(project_id, topic_id_book)
topic_path_buy = publisher.topic_path(project_id, topic_id_buy)
topic_path_search = publisher.topic_path(project_id, topic_id_search)

count = 0

f = open("events.csv","r")
while True:
	line = f.readline()
	if not line:
	 	break

	
	sleepingTime,topic,message = line.split(",")

	sleepingTime = int(sleepingTime)
	message = message.replace("\n","")

print("Publishing a topic: '%s' with message: %s"%(topic,message))
	
    # TODO PUB
	count += 1
	data_str = f"Message number {count}"
    data = data_str.encode("utf-8")
    if topic == "book":
        future = publisher.publish(topic_path_book, data)
        print(future.result())
    if topic == "buy":
        future = publisher.publish(topic_path_buy, data)
        print(future.result())
    if topic == "search":
        future = publisher.publish(topic_path_search, data)
        print(future.result())

    print("Waiting %i seconds"%sleepingTime)
	time.sleep(sleepingTime)

print("Done")

