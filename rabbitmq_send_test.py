import pika

# We can connect to a broker on a different machine by
# passing in its name or IP where local host is
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create a recipient queue
channel.queue_declare(queue='hello')

# send message to the exchange
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()

