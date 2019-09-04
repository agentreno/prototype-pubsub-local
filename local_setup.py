import os

from google.cloud import pubsub_v1


project_id = os.environ.get('PROJECT_ID', None)
topic_name = os.environ.get('TOPIC_NAME', None)
sub_name = os.environ.get('SUB_NAME', None)

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)
publisher.create_topic(topic_path)

subscriber = pubsub_v1.SubscriberClient()
sub_path = subscriber.subscription_path(project_id, sub_name)
subscriber.create_subscription(name=sub_path, topic=topic_path)
