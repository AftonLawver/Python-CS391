#!/usr/bin/env python
import json
import os
import sys

import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    queue = channel.queue_declare(queue='user_user')
    queue_name = queue.method.queue

    channel.queue_bind(
        exchange='user',
        queue=queue_name,
        routing_key='user.user' # binding key
    )

    def callback(ch, method, properties, body):
        payload = json.loads(body)
        print(' [x] Generating report')
        print(f"""
        ID: {payload.get('id')}
        User Email: {payload.get('user_email')}
        Age: {payload.get('age')}
        """)
        print(' [x] Done')
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='user_user',
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
