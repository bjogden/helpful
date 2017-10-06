__author__ = 'Bryce Ogden'

from googlevoice import Voice
from googlevoice.util import input

def message_me(text, **kwargs):
    """ Send me a message """
    output = None
    try:
        voice = Voice()
        voice.login(email, password)
        phone = "phone-number-here"

        if kwargs is not None:
            for key, value in kwargs.items():
                text += " | {}: {}".format(key, value)

        voice.send_sms(phone, text)
        output = "Sucessfully sent message"

    except Exception as e:
        output = "Error sending message: {}".format(e)

    finally:
        print(output)