import uuid


def get_uuid():
    return str(uuid.uuid4())

def get_object(obj_id):
    # TODO: will eventually need to change to "store" or "cache"
    with open(f"./cache/{obj_id}", 'r') as infile:
        contents = infile.read()
    return contents[:-1] # ignore the last new line?
