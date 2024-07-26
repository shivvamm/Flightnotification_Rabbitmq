from publisher.producer import send_notification

def handle_flight_delay(flight_id, delay_details):
    message = {
        'flight_id': flight_id,
        'delay_details': delay_details
    }
    send_notification(message)
