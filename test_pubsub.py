import pytest
import os
from google.cloud import pubsub_v1

# These ids must correspond to the project/topic ids used to run docker pubsub instance
project_id = os.environ.get('PROJECT_ID')
topic_id = os.environ.get('TOPIC_ID')
subscriber_id = os.environ.get('SUBSCRIBER_ID')

publisher = pubsub_v1.PublisherClient(credentials='')
project_path = "projects/" + project_id

def test_list_topics():
    # Pull topics from pubsub and check firist/only one
    topics = publisher.list_topics({"project": project_path})
    topic = next(iter(topics), {})
    expected_topic_name = publisher.topic_path(project_id, topic_id)
    assert topic.__getattr__('name') == expected_topic_name
