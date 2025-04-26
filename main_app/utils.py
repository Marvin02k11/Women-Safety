from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AppTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return text_type(user.is_active) + text_type(user.pk) + text_type(timestamp)


account_activation_token = AppTokenGenerator()



from django.conf import settings
from twilio.rest import Client


def send_sms(to_number, message_body):
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message_body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to_number
        )
        print(f"Message sent to {to_number}. SID: {message.sid}")
        return message.sid
    except Exception as e:
        print(f"SMS sending failed: {e}")
        return None


# def send_sms(to_numbers, name, link):
#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#     message_body = f"""🚨🛑 Emergency Alert 🛑🚨
# {name} is in an emergency and needs your help immediately!
# Click the link below for location:
# {link}"""

#     for number in to_numbers:
#         try:
#             message = client.messages.create(
#                 body=message_body,
#                 from_=settings.TWILIO_PHONE_NUMBER,
#                 to=number
#             )
#             print(f"Message sent to {number}. SID: {message.sid}")
#         except Exception as e:
#             print(f"SMS sending failed to {number}: {e}")