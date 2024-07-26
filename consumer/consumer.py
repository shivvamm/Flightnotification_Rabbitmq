import pika
import json
from config import RABBITMQ_HOST, RABBITMQ_QUEUE
from app.send_notification_service import send_email

def connect_to_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE)
    return channel, connection

def process_notification(message):
    to_email=message.user.email
    subject=message.user.subject
    body=message.user.body
    send_email(to_email,subject,body)
    print(f"Processing notification to send mail: {message}")

def callback(ch, method, properties, body):
    message = json.loads(body)
    process_notification(message)

def start_consumer():
    channel, connection = connect_to_rabbitmq()
    channel.basic_consume(
        queue=RABBITMQ_QUEUE,
        on_message_callback=callback,
        auto_ack=True
    )
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
