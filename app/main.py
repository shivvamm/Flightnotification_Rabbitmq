from fastapi import FastAPI
from typing import Dict
from app.flight_service import notify_flight_delay
from consumer.consumer import start_consumer
import threading
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI()



class DelayDetails(BaseModel):
    reason: str
    duration: int

class UserDetails(BaseModel):
    email: str
    name: str
    subject: str
    body:str
    phone_number: str

class FlightDelayNotification(BaseModel):
    flight_id: str
    delay_details: DelayDetails
    user_details: UserDetails

@app.on_event("startup")
async def startup_event():
    # Start consumer in a background thread
    def run_consumer():
        start_consumer()
    thread = threading.Thread(target=run_consumer)
    thread.daemon = True
    thread.start()

@app.post("/notify_flight_delay/")
async def notify_flight_delay_endpoint(notification: FlightDelayNotification):
    message = notification.dict()
    from publisher.producer import send_notification
    send_notification(message)
    return {"message": "Notification sent"}
