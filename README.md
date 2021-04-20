# Event-Handler

Standalone WIP handling gcp's pubsub service locally with tests.

## Docker

Spin up local dockerized container for pubsub https://github.com/marcelcorso/gcloud-pubsub-emulator.

This command starts pubsub on port 8618 with test project, topic and subscriber args.

TODO: Make args env vars and pass to docker + pytest

```bash
docker run --rm -ti -p 8681:8681 -e PUBSUB_PROJECT1=test-pubsub-project,test-pubsub-topic:test-pubsub-subscriber messagebird/gcloud-pubsub-emulator:latest
```

## Pytest

Be sure to run local docker pubsub using the comand above or tests won't be able to communicate with service.

```bash

# Activate virtualenv
$ python3 -m virtualenv venv
$ source venv/bin/activate

# Install API dependencies
$ pip install -r requirements.txt

# Export env vars
$ export PUBSUB_EMULATOR_HOST=localhost:8681 
$ export PROJECT_ID=test-pubsub-project
$ export TOPIC_ID=test-pubsub-topic
$ export SUBSCRIBER_ID=test-pubsub-subscriber

# Run tests with env
$ pytest

```
