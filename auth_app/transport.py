import config
from django.core.mail import send_mail as send_mail_from_django
from django.conf import settings
from auth_app.services import fetch_find_user_function


def send_sms(subject: str, message: str, recipient_list: list[str]):
    pass


def send_mail(
    subject: str,
    message: str,
    recipient_list: list[str],
    html_message: str | None = None,
    from_email: str | None = None,
):
    send_mail_from_django(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        html_message=html_message,
    )


def transport_function():
    choices = {
        settings.SEND_MESSAGE_TYPE_CHOICES.SMS: send_sms,
        settings.SEND_MESSAGE_TYPE_CHOICES.EMAIL: send_mail,
    }
    return choices.get(settings.SEND_MESSAGE_TYPE, None)


def fetch_recipient(recipient: str):
    find_user = fetch_find_user_function()
    return find_user(recipient)


def recipient_exist(recipient: str):
    user = fetch_recipient(recipient)
    return user is not None


def send_message(subject: str, message: str, recipient: str):
    """if not recipient_exist(recipient):
    raise ObjectDoesNotExist"""

    transport = transport_function()
    transport(subject=subject, message=message, recipient_list=[recipient])


def send_pin_code(pin_code: str, recipient: str):
    send_message(f"Auth pin-code for {config.CONFIRMATION_LINK}", pin_code, recipient)


def send_confirmation_link(user_id: str, recipient: str):
    link = f"https://{config.CONFIRMATION_LINK}/confirmation/?user_id={user_id}"
    send_message("Для подтверждения пройдите по ссылке", link, recipient)
