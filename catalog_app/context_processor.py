from django.conf import settings


def yml_catalog_url_def(request):
    """
    Returns the URL of the YML catalog file.
    """
    return {"yml_catalog_url": f"{settings.MEDIA_URL}yml_catalog.xml"}
