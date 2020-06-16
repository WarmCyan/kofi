import json
import os.path
import os
import sys
import glob

from collections import OrderedDict

from kofi import util
from kofi.note import Note
from kofi.map import Map


class Inbox(Note):
    def __init__(self):
        super().__init__()

        # recent notes (filenames)
        self.low_link_count = []
        self.recent = []

        self.sections = OrderedDict()

    def parse_sections(self):
        current_section = None

        for line in self.content:
            if line[0:1] == "# ":

                # get the section title text
                section_name = line[2:]

                current_section = section_name
                self.sections[section_name] = []
            elif current_section is not None:
                self.sections[current_section].append(line)

    def grab_recent(self):
        active_dir = util.run_shell("active-dir")
        os.chdir(active_dir)
        path = "recent_list.json"
        recent = []
        if os.path.exists(path):
            with open(path, "r") as infile:
                recent = json.load(infile)

        for index, note in enumerate(recent):
            if index >= 10:
                break
            link = util.run_shell("get-link", note, "-d") + "\n\n"
            self.recent.append(link)

    def find_link_counts(self):
        active_dir = util.run_shell("active-dir")
        os.chdir(active_dir)
        
        notemap = Map()
        notemap.construct_map()

        ordered = sorted(notemap.links_from, key=lambda k: len(notemap.links_from[k]))
        
        for key in ordered:
            print(key, notemap.links_from[key])

