from urllib.parse import urlparse


def valid_input(request_body: dict, needed_keys: list):
    for key in needed_keys:
        if key not in request_body:
            return False
    return True


def to_gcs_uri(url):
    return "gs:/" + urlparse(url).path
