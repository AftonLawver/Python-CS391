import json
import uuid

import pika

# We can connect to a broker on a different machine by
# passing in its name or IP where local host is
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(
    exchange='user',
    exchange_type='direct'
)

user = {
    'id': str(uuid.uuid4()),
    'user_email': 'afton@gmail.com',
    'age': 27
}


# send message to the exchange
channel.basic_publish(exchange='user',
                      routing_key='user.email',
                      body=json.dumps({'user_email': user['user_email']}))
print(" [x] Sent notify message.")

channel.basic_publish(exchange='user',
                      routing_key='user.user',
                      body=json.dumps(user)
                      )

print(" [x] Sent report message.")

connection.close()
