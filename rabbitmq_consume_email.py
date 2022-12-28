#!/usr/bin/env python
import json
import os
import sys

import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    queue = channel.queue_declare(queue='user_email')
    queue_name = queue.method.queue

    channel.queue_bind(
        exchange='user',
        queue=queue_name,
        routing_key='user.email' # binding key
    )

    def callback(ch, method, properties, body):
        payload = json.loads(body)
        print(' [x] Notifying {}'.format(payload['user_email']))
        print(' [x] Done')
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='user_email',
                          on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os.exit(0)
