import os
from django.core import mail

from backend import settings

EMAIL_HOST_USER = "CollabConnect <" + os.getenv("EMAIL") + ">"
WHITELISTED_ADDRESSES = ["aditya20016@iiitd.ac.in",
                         "heemank20064@iiitd.ac.in",
                         "shikhar20121@iiitd.ac.in"]


def send_mail(to, subject: str = "", body: list = None, html=None):
    if type(to) == str:
        to = [to]
    print("Sending mail to " + ", ".join(to), flush=True)
    if not settings.DEBUG or set(WHITELISTED_ADDRESSES) >= set(to):
        mail.send_mail(subject=subject, message=body,
                       from_email=EMAIL_HOST_USER, recipient_list=to,
                       html_message=html)
    else:
        print("Attempt to send email to"
              "non-whitelisted address in DEBUG mode", flush=True)
        raise ConnectionRefusedError("Attempt to send email to"
                                     "non-whitelisted address in DEBUG mode")
