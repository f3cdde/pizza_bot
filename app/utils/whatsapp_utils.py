from twilio.rest import Client
from app.config import Config

class WhatsAppUtils:
    def __init__(self):
        self.client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)

    def send_message(self, to, body):
        message = self.client.messages.create(
            body=body,
            from_=f'whatsapp:{Config.TWILIO_PHONE_NUMBER}',
            to=f'whatsapp:{to}'
        )
        return message.sid

    def send_media(self, to, media_url):
        message = self.client.messages.create(
            media_url=media_url,
            from_=f'whatsapp:{Config.TWILIO_PHONE_NUMBER}',
            to=f'whatsapp:{to}'
        )
        return message.sid
