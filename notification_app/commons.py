from notification_app.models import Recipient


def get_recipient_list() -> list[str]:
    return [recipient.email for recipient in Recipient.objects.all()]
