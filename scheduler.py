import os
from twilio.rest import Client

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")  # "whatsapp:+14155238886"
MY_WHATSAPP_NUMBER = os.getenv("MY_WHATSAPP_NUMBER")          # "whatsapp:+3519xxxxxxx"

client = Client(TWILIO_SID, TWILIO_AUTH)

def send_whatsapp(message):
    msg = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body=message,
        to=MY_WHATSAPP_NUMBER,
    )
    return msg.sid
