from twilio.rest import Client

TWILIO_SID = "AC0a7db17255fa1985cd91bff2388be981"
TWILIO_AUTH_TOKEN = "55c2b2b96cb931b11e727eedc3794aef"
TWILIO_VIRTUAL_NUMBER = "+18146820299"
TWILIO_VERIFIED_NUMBER = "+243995657258"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
