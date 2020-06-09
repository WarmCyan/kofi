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

        self.filename = filename
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
        self.data = util.read_yaml_metadata(yaml_lines)
        self.data["tags"] = util.from_tag_string(self.data["tags"])

        # load content
        for line in file_lines[yaml_end + 1 :]:
            self.content.append(line)

    def _yamlline(self, key):
        value = self.data[key]
        if key == "tags":
            value = util.to_tag_string(value)
            
        if value is None:
            value = ""
            
        return f"{key}: {value}\n"

    # NOTE: assume filename already populated
    # NOTE: I am not using yaml.dump() because it breaks ordering and adds quotes to strings
    def write(self):
        output = ""
        output += "<!-- KOFI -->\n\n---\n"

        output += self._yamlline("name")
        output += self._yamlline("date-created")
        output += self._yamlline("date-updated")
        output += self._yamlline("description")
        output += self._yamlline("tags")

        used = ["name", "date-created", "date-updated", "description", "tags"]
        unused = [x for x in self.data if x not in used]
        
        for key in unused:
            output += self._yamlline(key)
        #output += str(yaml.dump(self.data, default_style=None, default_flow_style=False))

        
        output += "---\n"
        output += "".join(self.content)

        with open(self.filename, "w") as outfile:
            outfile.write(output)
