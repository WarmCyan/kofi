""" All classes pertaining to kofi objects """

import json
import logging
import os
from datetime import datetime

import util
from display_types import DisplayType


class ObjectManager:
    def __init__(self):
        self.loaded_objects = {}
        self.recent_objects = []

        # self.name_index = {}

    def get(self, obj_id):
        if obj_id not in self.loaded_objects:
            self.loaded_objects[obj_id] = Object.load(obj_id)

        return self.loaded_objects[obj_id]

    def create_connection(self, obj1, obj2, edge_type):
        obj1.connect(obj2, edge_type)
        obj2.connect(obj1, edge_type)

    def break_connection(self, obj1, obj2, edge_type):
        obj1.disconnect(obj2, edge_type)
        obj2.disconnect(obj1, edge_type)

    def save_cache(self):
        logging.info("Object manager saving cache...")
        cache_data = {"recent_objects": self.recent_objects}

        with open("./cache/manager-cache.json", "w") as outfile:
            json.dump(cache_data, outfile)
        logging.info("Cache dumped!")

    def load_cache(self):
        logging.info("Object manager loading cache...")

        if os.path.exists("./cache/manager-cache.json"):
            with open("./cache/manager-cache.json", "r") as infile:
                cache_data = json.load(infile)
            self.recent_objects = cache_data["recent_objects"]
            logging.info("Cache loaded!")
        else:
            logging.warning("No cache found")

    def create_object(self):
        new_id = util.get_uuid()
        logging.info("Creating new object %s...", new_id)
        self.loaded_objects[new_id] = Object(
            new_id, date_created=datetime.now(), manager=self
        )
        return new_id


class Connection:
    def __init__(self, obj1, obj2, edge_type):
        self.edge_type = edge_type
        self.obj1 = obj1
        self.obj2 = obj2


class Object:
    def __init__(
        self,
        obj_id,
        date_created=None,
        date_updated=None,
        name="",
        edits=0,
        connections=[],
        default_display=DisplayType.NORMAL,
        properties={},
        content="",
        manager=None,
    ):
        self.id = obj_id
        self.date_created = date_created
        self.date_updated = date_updated
        self.name = name
        self.edits = edits
        self.connections = connections
        self.default_display = default_display
        self.properties = properties

        self.content = content
        self.content_loaded = True

        if self.content is None:
            self.content_loaded = False

        self.manager = manager

    def connect(self, obj2, edge_type):
        """ Create a new connection between this object and the passed object with specified type. """
        logging.debug(
            "Creating connection %s --%s--> %s...", self.id, obj2.id, edge_type
        )
        new_conn = Connection(self, obj2, edge_type)
        self.connections.append(new_conn)

    def disconnect(self, obj2, edge_type):
        """ Remove the specified typed connection between this object and obj2 (only removes on this end) """
        logging.debug(
            "Removing connection %s --%s--> %s...", self.id, obj2.id, edge_type
        )
        for conn in self.connections:
            if conn.obj2 == obj2 and conn.edge_type == edge_type:
                self.connections.remove(conn)
                logging.debug("Connection removed!")
                break

    def load_content(self):
        with open(f"./cache/{self.id}", "r") as infile:
            contents = infile.read()

        self.content = contents
        self.content_loaded = True

    def save(self):
        """ Write out any existing metadata and content changes. """
        if self.content_loaded:
            with open(f"./cache/{self.id}", "w") as outfile:
                contents = outfile.write(self.content)

        self.date_updated = datetime.now()
        self.edits += 1

        metadata = {
            "date_created": util.date_to_string(self.date_created),
            "date_updated": util.date_to_string(self.date_updated),
            "name": self.name,
            "edits": self.edits,
            "connections": self.serialize_connections(),
            "default_display": self.default_display.value,
            "properties": self.properties,
        }
        with open(f"./cache/{self.id}.json", "w") as outfile:
            json.dump(metadata, outfile)

    def serialize_connections(self):
        serialized_connections = []
        for connection in self.connections:
            serialized_connections.append([connection.obj2, connection.edge_type])

        return serialized_connections

    # NOTE: this is probably dangerous to just call all the time, or will have to load the entire database each time.
    def populate_connections(self, connection_array):
        for connection_pair in connection_array:
            self.connect(self.manager.get(connection_pair[0]), connection_pair[1])

    @staticmethod
    def load(obj_id, load_content=True):
        contents = None

        if load_content:
            with open(f"./cache/{obj_id}", "r") as infile:
                contents = infile.read()

        with open(f"./cache/{obj_id}.json", "r") as infile:
            metadata = json.load(infile)

        return Object(
            obj_id,
            date_created=util.string_to_date(metadata["date_created"]),
            date_updated=util.string_to_date(metadata["date_updated"]),
            name=metadata["name"],
            edits=metadata["edits"],
            connections=metadata["connections"],
            default_display=DisplayType(metadata["default_display"]),
            properties=metadata["properties"],
        )
