Sure! Here's a comprehensive `README.md` file for your project. This file provides an overview of the project, setup instructions, and usage guidelines.

---

# Flight Notification System

A FastAPI-based system for handling flight delay notifications using RabbitMQ. This project includes a producer to send notifications and a consumer to process them. Notifications are sent via RabbitMQ and processed by a background consumer. The system also demonstrates how to integrate Pydantic for request validation in FastAPI.

## Project Structure

```
flight_notification_app/
├── publisher/
│   ├── __init__.py
│   ├── config.py
│   ├── producer.py
├── consumer/
│   ├── __init__.py
│   ├── config.py
│   ├── consumer.py
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── flight_service.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.8+
- RabbitMQ Server
- Mailtrap (or another SMTP service for email)

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd flight_notification_app
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up RabbitMQ**

   - Install RabbitMQ following the [official installation guide](https://www.rabbitmq.com/download.html).
   - Start the RabbitMQ server.

5. **Configure SMTP**

   - Create an account on Mailtrap (or any other SMTP service).
   - Update `publisher/config.py` with your SMTP credentials.

## Configuration

### RabbitMQ

Edit `publisher/config.py` and `consumer/config.py` to include your RabbitMQ server details:

```python
RABBITMQ_HOST = "localhost"  # RabbitMQ server address
RABBITMQ_QUEUE = "flight_notifications"  # Queue name
```

### SMTP

Edit `publisher/producer.py` to include your SMTP server details:

```python
smtp_server = "live.smtp.mailtrap.io"
port = 587
login = "api"
password = "1a2b3c4d5e6f7g"
sender_email = "mailtrap@example.com"
```

#### Set the password and the sender email in the env file

```bash
PASSWORD="email password of the google app password"
EMAIL="your email"
```

## Usage

### Running the Application

1. **Start RabbitMQ Server**: Ensure RabbitMQ is running.

2. **Run FastAPI Server**:

   ```bash
   uvicorn app.main:app --reload
   ```

3. **Start Consumer**: The consumer starts automatically with the FastAPI server.

### Sending Notifications

To send a flight delay notification, make a POST request to the endpoint `/notify_flight_delay/` with the following JSON payload:

```json
{
  "flight_id": "ABC123",
  "delay_details": {
    "reason": "Weather conditions",
    "duration": 90
  },
  "user_details": {
    "email": "user@example.com",
    "name": "John Doe",
    "subject": "Flight Delay Notification",
    "body": "Dear John Doe, your flight ABC123 has been delayed due to weather conditions. Estimated delay is 90 minutes.",
    "phone_number": "+1234567890"
  }
}
```

### Testing

You can use tools like Postman or `curl` to test the endpoint:

```bash
curl -X POST "http://127.0.0.1:8000/notify_flight_delay/" -H "Content-Type: application/json" -d '{
  "flight_id": "ABC123",
  "delay_details": {
    "reason": "Weather conditions",
    "duration": 90
  },
  "user_details": {
    "email": "user@example.com",
    "name": "John Doe",
    "phone_number": "+1234567890"
  }
}'
```

## Code Overview

- **Publisher**: Contains logic to send notifications to RabbitMQ.
  - `producer.py`: Sends notifications.
  - `config.py`: Configuration for RabbitMQ and SMTP.
- **Consumer**: Contains logic to consume messages from RabbitMQ and process them.

  - `consumer.py`: Consumes and processes notifications.
  - `config.py`: Configuration for RabbitMQ.

- **App**: Contains the FastAPI application and models.
  - `main.py`: Defines the FastAPI application and endpoints.
  - `models.py`: Pydantic models for request validation.
  - `flight_service.py`: Service for handling flight delay notifications.

## Contributing

Feel free to open issues and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This `README.md` provides an overview of your project, detailed setup and usage instructions, and code explanations. Feel free to modify it based on specific details or additional information about your project.
