import logging
import sqlite3

from display_types import DisplayType


class ObjectManager:
    def __init__(self):
        logging.info("Connecting to database...")
        self.conn = sqlite3.connect("./store/objects.db")
        logging.info("Connected successfully")

        self.c = self.conn.cursor()

        self.loaded_objects = {}

    def __del__(self):
        self.conn.close()

    def init_tables(self):
        self.c.execute(  # or should this be self.conn
            """ select count(name) from sqlite_master where type='table' and name='objects' """
        )

        logging.debug("Checking object tables...")
        if self.c.fetchone()[0] == 1:
            logging.debug("Tables existing and happy!")
            return
        else:
            logging.warning("Object tables not found")

        logging.info("Creating object tables...")
        self.conn.execute(
            """
            CREATE TABLE Objects
            (
                id INT primary key not null,
                date_created DATETIME not null,
                date_updated DATETIME not null,
                name VARCHAR(100) not null,
                edits INT not null,
                display_type INT not null,
            );
            """
        )

        self.conn.execute(
            """
            CREATE TABLE Connections
            (
                id INT primary key not null,
                id1 INT not null,
                id2 INT not null,
                type VARCHAR(100) not null
            );
            """
        )

        self.conn.execute(
            """
            CREATE TABLE Properties
            (
                id INT primary key not null,
                object_id INT not null,
                key VARCHAR(50) not null,
                value TEXT not null
            );
            """
        )

        self.conn.commit()
        logging.info("Objects created!")

    def load_connections(self, obj_id):
        cursor = self.conn.execute(
            """
            SELECT
                Connections.id1,
                Connections.id2,
                Connections.edge_type
            FROM Objects JOIN Connections
            WHERE
                Objects.id == Connections.id1 OR
                Objects.id == Connections.id2;
            """
        )
        connection_objects = []
        for row in cursor:
            #connection_object.append(Connection())
            pass


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
        connections=None,  # []
        default_display=DisplayType.NORMAL,
        properties=None,  # {}
        content=None,
        manager=None,
    ):
        self.manager = manager

        self.id = obj_id
        self.date_created = date_created
        self.date_updated = date_updated
        self.name = name
        self.edits = edits
        self.default_display = default_display

        self._connections = connections
        self.connections_loaded = True

        self.properties = properties
        self.properties_loaded = True

        self.content = content
        self.content_loaded = True

        if self.content is None:
            self.content_loaded = False

        if self._connections is None:
            self.connections_loaded = False

        if self.properties is None:
            self.properties_loaded = False

    @property
    def connections(self):
        pass
