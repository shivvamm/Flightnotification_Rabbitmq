import pika
import json
from config import RABBITMQ_HOST, RABBITMQ_QUEUE

def connect_to_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE)
    return channel, connection

def send_notification(message):
    channel, connection = connect_to_rabbitmq()
    channel.basic_publish(
        exchange='',
        routing_key=RABBITMQ_QUEUE,
        body=json.dumps(message),
        properties=pika.BasicProperties(delivery_mode=2) 
    )
    print(f" [x] Sent {message}")
    connection.close()
