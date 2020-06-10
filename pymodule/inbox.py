import sys

from kofi.note import Note

class Inbox(Note):
    def __init__(self):
        super().__init__(self)

        # recent notes (filenames)
        self.recent = []


