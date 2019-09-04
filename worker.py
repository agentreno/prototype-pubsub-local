import time
import os

from google.cloud import pubsub_v1


project_id = os.environ.get('PROJECT_ID', None)
topic_name = os.environ.get('TOPIC_NAME', None)
sub_name = os.environ.get('SUB_NAME', None)

# Subscribe and define a callback for messages
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, sub_name)

def callback(message):
    print(f'Received message: {message}')
    message.ack()
    exit(1)

subscriber.subscribe(subscription_path, callback=callback)
print('Listening')

# Publish a message
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

publisher.publish(topic_path, b'Hello')

while True:
    time.sleep(1)
