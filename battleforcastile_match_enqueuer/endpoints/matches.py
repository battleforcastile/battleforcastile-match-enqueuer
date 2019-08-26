import json
import os

import pika

from flask import request, abort
from flask_restful import Resource


class MatchPendingResource(Resource):
    def post(self):
        data = json.loads(request.data) if request.data else {}

        # Validate request
        if (
                not data.get('first_user') or
                not data.get('first_user').get('username') or
                not data.get('first_user').get('character')
        ):
            abort(400)

        credentials = pika.PlainCredentials(
            os.getenv('RABBITMQ_USER').rstrip(), os.getenv('RABBITMQ_PASSWORD').rstrip())
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

        print("%r sent to exchange %r with data: %r" % (routing_key, exchange_name, data))
        connection.close()

        return '', 201
