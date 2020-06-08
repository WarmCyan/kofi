""" Note class to handle note things """

import yaml

from kofi import util


class Note:
    def __init__(self):
        self.filename = ""
        self.content = []
        self.data = {}

    def load(self, filename):
        """ Load all info from a note from its file """
        with open(self.filename, "r") as infile:
            file_lines = infile.readlines()

        # get all yaml lines
        yaml_start = -1
        yaml_end = -1
        for index, line in enumerate(file_lines):
            if line == "---\n" and yaml_start == -1:
                yaml_start = index
            elif line == "---\n" and yaml_end == -1:
                yaml_end = index

        yaml_lines = file_lines[yaml_start + 1 : yaml_end]
        data = util.read_yaml_metadata(yaml_lines)

        # load content
        for line in file_lines[yaml_end + 1 :]:
            self.content += line

    # NOTE: assume filename already populated
    def write(self):
        output = ""
        output += "<!-- KOFI -->\n\n---\n"

        output += str(yaml.dump(self.data, default_flow_style=False))
        output += "---\n"
        output += "".join(self.content)

        with open(self.filename, "w") as outfile:
            outfile.write(output)
