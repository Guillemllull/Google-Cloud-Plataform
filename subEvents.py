# -*- coding: utf-8 -*-
"""
Created on Wed May 25 11:37:47 2022

@author: Usuario
"""

from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1

# TODO(developer)

# Number of seconds the subscriber should listen for messages
timeout = 5.0

subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_id}`
subscription_path_book = "projects/cloud-madm/subscriptions/sub-book"
subscription_path_buy = "projects/cloud-madm/subscriptions/sub-buy"
subscription_path_search = "projects/cloud-madm/subscriptions/sub-search"

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    print(f"Received {message}.")
    print(f"data {message.data}")
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path_book, callback=callback)
print(f"Listening for messages on {subscription_path_book}..\n")
streaming_pull_future = subscriber.subscribe(subscription_path_buy, callback=callback)
print(f"Listening for messages on {subscription_path_buy}..\n")
streaming_pull_future = subscriber.subscribe(subscription_path_search, callback=callback)
print(f"Listening for messages on {subscription_path_search}..\n")

# Wrap subscriber in a 'with' block to automatically call close() when done.
with subscriber:
    try:
        # When `timeout` is not set, result() will block indefinitely,
        # unless an exception is encountered first.
        streaming_pull_future.result(timeout=timeout)
    except TimeoutError:
        streaming_pull_future.cancel()  # Trigger the shutdown.
        streaming_pull_future.result()  # Block until the shutdown is complete.
        
        
        
```     
from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1

# TODO(developer)
project_id = "cloud-madm"
subscription_id_book = "sub-book"
subscription_id_buy = "sub-buy"
subscription_id_search = "sub-search"
# Number of seconds the subscriber should listen for messages
timeout = 40.0

subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_id}`
subscription_path_book = subscriber.subscription_path(project_id, subscription_id_book)
subscription_path_buy = subscriber.subscription_path(project_id, subscription_id_buy)
subscription_path_search = subscriber.subscription_path(project_id, subscription_id_search)

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    print(f"Received {message}.")
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path_book, callback=callback)
print(f"Listening for messages on {subscription_path_book}..\n")

streaming_pull_future = subscriber.subscribe(subscription_path_buy, callback=callback)
print(f"Listening for messages on {subscription_path_buy}..\n")

streaming_pull_future = subscriber.subscribe(subscription_path_search, callback=callback)
print(f"Listening for messages on {subscription_path_search}..\n")

# Wrap subscriber in a 'with' block to automatically call close() when done.
with subscriber:
    try:
        # When `timeout` is not set, result() will block indefinitely,
        # unless an exception is encountered first.
        streaming_pull_future.result(timeout=timeout)
    except TimeoutError:
        streaming_pull_future.cancel()  # Trigger the shutdown.
        streaming_pull_future.result()  # Block until the shutdown is complete.
```