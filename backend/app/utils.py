from flask import jsonify
from http import HTTPStatus


def valid_input(request_body: dict, needed_keys: list):
    for key in needed_keys:
        if key not in request_body:
            return False
    return True
