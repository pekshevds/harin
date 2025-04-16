from const_app.models import SEODefaults


def fetch_current_consts() -> SEODefaults | None:
    return SEODefaults.objects.all()[0]


def fetch_seo_title_category() -> str:
    first_record = fetch_current_consts()
    if first_record:
        return first_record.seo_title_category
    return ""


def fetch_seo_description_category() -> str:
    first_record = fetch_current_consts()
    if first_record:
        return first_record.seo_description_category
    return ""


def fetch_seo_keywords_category() -> str:
    first_record = fetch_current_consts()
    if first_record:
        return first_record.seo_keywords_category
    return ""


def fetch_seo_title_good() -> str:
    first_record = fetch_current_consts()
    if first_record:
        return first_record.seo_title_category
    return ""


def fetch_seo_description_good() -> str:
    first_record = fetch_current_consts()
    if first_record:
        return first_record.seo_description_category
    return ""


def fetch_seo_keywords_good() -> str:
    first_record = fetch_current_consts()
    if first_record:
        return first_record.seo_keywords_category
    return ""
