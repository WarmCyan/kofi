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
            if line[0:2] == "# ":

                # get the section title text
                section_name = line[2:]

                current_section = section_name
                self.sections[section_name] = [line]
            elif current_section is not None:
                self.sections[current_section].append(line)

    def grab_recent(self):
        active_dir = util.run_shell("kofi-active-dir")
        os.chdir(active_dir)
        path = "recent_list.json"
        recent = []
        if os.path.exists(path):
            with open(path, "r") as infile:
                recent = json.load(infile)

        for index, note in enumerate(recent):
            if index >= 10:
                break
            link = util.run_shell("kofi-get-link", note, "-d") + "\n\n"
            self.recent.append(link)

    def find_link_counts(self):
        active_dir = util.run_shell("kofi-active-dir")
        os.chdir(active_dir)
        
        notemap = Map()
        notemap.construct_map()

        ordered = sorted(notemap.links_from, key=lambda k: len(notemap.links_from[k]))

        for key in ordered:
            if len(notemap.links_from[key]) <= 2:
                link = util.run_shell("kofi-get-link", key, "-d") + " :: (" + str(len(notemap.links_from[key])) + ")\n\n"
                self.low_link_count.append(link)

    # NOTE: assumes parse already called
    def compile_content(self):

        self.grab_recent()
        self.find_link_counts()

        if "Recent\n" not in self.sections:
            self.sections["Recent\n"] = []
            
        if "Disconnected\n" not in self.sections:
            self.sections["Disconnected\n"] = []

        self.sections["Recent\n"] = ["# Recent\n\n"]
        self.sections["Recent\n"].extend("".join(self.recent))
        self.sections["Disconnected\n"] = ["# Disconnected\n\n"]
        self.sections["Disconnected\n"].extend("".join(self.low_link_count))
        
        self.content = []
        for section in self.sections:
            for line in self.sections[section]:
                self.content.append(line)
