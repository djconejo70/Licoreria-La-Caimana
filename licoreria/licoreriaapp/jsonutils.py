import decimal
import json


def dumps(item: dict) -> str:
    return json.dumps(item, default=default_type_error_handler)


def default_type_error_handler(obj):
    if isinstance(obj, decimal.Decimal):
        return int(obj)
    raise TypeError