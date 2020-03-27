import json
import uuid
from datetime import datetime


def get_uuid():
    return str(uuid.uuid4())


def get_object(obj_id):
    # TODO: will eventually need to change to "store" or "cache"
    with open(f"./cache/{obj_id}", "r") as infile:
        contents = infile.read()
    return contents[:-1]  # ignore the last new line?


def write_object_metadata(obj_id):
    # metadata =
    pass


def date_to_string(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def string_to_date(string):
    return datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
