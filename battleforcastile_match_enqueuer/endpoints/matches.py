import json
import os

import pika

from flask import request, abort
from flask_restful import Resource

from battleforcastile_match_enqueuer.custom_logging import logging


class MatchPendingResource(Resource):
    def post(self):
        data = json.loads(request.data) if request.data else {}

        # Validate request
        if (
                not data.get('first_user') or
                not data.get('first_user').get('username') or
                not data.get('first_user').get('character')
        ):
            logging.info(
                f'[ENQUEUE MATCH] Match could not be enqueued for creation due to missing information',
                {
                    'request_id': None,
                    'service': 'battleforcastile-match-enqueuer',
                    'username': None,
                    'action': 'enqueue_match',
                    'payload': data
                }
            )
            abort(400)

        credentials = pika.PlainCredentials(
            os.getenv('RABBITMQ_USER', 'user').rstrip(), os.getenv('RABBITMQ_PASSWORD', '').rstrip())
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue='matches_pending')

        # We use the default exchange ''
        exchange_name = ''
        routing_key = 'matches_pending'

        channel.basic_publish(exchange=exchange_name,
                              routing_key=routing_key,
                              body=json.dumps(data),
                              # Delivery mode 2 makes the broker save the message to disk.
                              # This will ensure that the message be restored on reboot even
                              # if RabbitMQ crashes before having forwarded the message.
                              properties=pika.BasicProperties(
                                  delivery_mode=2,
                              ))

        logging.info(
            f'[ENQUEUE MATCH] Match was enqueued for creation',
            {
                'request_id': None,
                'service': 'battleforcastile-match-enqueuer',
                'username': None,
                'action': 'enqueue_match',
                'payload': data
            }
        )
        connection.close()

        return '', 201
