from fastapi import FastAPI
from typing import Dict
from app.flight_service import notify_flight_delay
from consumer.consumer import start_consumer
import threading

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Start consumer in a background thread
    def run_consumer():
        start_consumer()
    thread = threading.Thread(target=run_consumer)
    thread.daemon = True
    thread.start()

@app.post("/notify_flight_delay/")
async def notify_flight_delay_endpoint(flight_id: str, delay_details: Dict,user_details:Dict):
    message = {
        'flight_id': flight_id,
        'delay_details': delay_details,
        'user_details':user_details
    }
    from publisher.producer import send_notification
    send_notification(message)
    return {"message": "Notification sent"}
