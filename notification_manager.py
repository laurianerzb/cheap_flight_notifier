from twilio.rest import Client
import smtplib

TWILIO_SID = "AC0a7db17255fa1985cd91bff2388be981"
TWILIO_AUTH_TOKEN = "55c2b2b96cb931b11e727eedc3794aef"
TWILIO_VIRTUAL_NUMBER = "+18146820299"
TWILIO_VERIFIED_NUMBER = "+243995657258"
MY_EMAIL = "ruzubalaury@gmail.com"
MY_PASSWORD = "rguzrjibqrbqrgjm"
# 465
EMAIL_PROVIDER_SMTP_ADDRESS = 'smtp.gmail.com'


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

    def send_emails(self, emails, message):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            # connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
