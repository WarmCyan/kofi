import glob
import os
import re

from kofi import util

LINK_PATTERN = re.compile("\[.*\]\((.*)\)")

class Map:
    def __init__(self):
        # [key:A] -> B
        self.links_to = (
            {}
        )  # key is a file, value is array of files that key file links to

        # A -> [key:B]
        self.links_from = (
            {}
        )  # key is a file, value is array of files that link _to_ this file

        self.filetitles = {}
        

    def construct_map(self, root=None, ignore_recent=True, ignore_inbox=True, grab_titles=True):
        # NOTE: use root = None to construct the map of _all_ notes
        active_dir = util.run_shell("active-dir")
        os.chdir(active_dir)


        if root is None:
            for filepath in glob.iglob("*.md"):
                if filepath == "recent.md" and ignore_recent:
                    continue
                if filepath == "inbox.md" and ignore_inbox:
                    continue

                if grab_titles:
                    title = util.run_shell("get-title", filepath)
                    self.filetitles[filepath] = title

                # make sure the respective dictionary keys exist
                if filepath not in self.links_to:
                    self.links_to[filepath] = []
                    
                if filepath not in self.links_from:
                    self.links_from[filepath] = []
                
                # scan the file for links
                self.parse_file_links(filepath)
        else:
            if grab_titles:
                title = util.run_shell("get-title", root)
                self.filetitles[root] = title
                
            with open(root, "r") as infile:
                contents = infile.read()

                matches = re.findall(LINK_PATTERN, contents)
                for match in matches:
                    link = match
                    self.create_link(root, link)
                    
                    if grab_titles:
                        title = util.run_shell("get-title", link)
                        self.filetitles[link] = title
                    
                    # go one level deep
                    self.parse_file_links(link)
                
    def parse_file_links(self, filepath, grab_titles=True):
        with open(filepath, "r") as infile:
            contents = infile.read()

            matches = re.findall(LINK_PATTERN, contents)
            for match in matches:
                link = match
                self.create_link(filepath, link)
                
                if grab_titles:
                    title = util.run_shell("get-title", link)
                    self.filetitles[link] = title
        

    # file_from is a
    # file_to is b
    # A -> B
    def create_link(self, a, b):
        # file_from (a) is key in links_to, file_to (b) is added to values
        if a not in self.links_to:
            self.links_to[a] = []

        self.links_to[a].append(b)

        # (b) is key in links_from, file_from (a) is added to values
        if b not in self.links_from:
            self.links_from[b] = []

        self.links_from[b].append(a)


    def to_graphviz(self):
        lines = ["strict digraph G", "{", "bgcolor=\"transparent\""]
        
        for item in self.filetitles:
            link = item[:item.rfind(".")] + ".html"
            lines.append(f"\"{item}\" [ label=\"{self.filetitles[item]}\" URL=\"{link}\" ];")

        already_handled = []

        for item in self.links_to:
            for end in self.links_to[item]:
                if (item, end) in already_handled:
                    continue

                if item in self.links_to[end]:
                    lines.append(f"\"{item}\" -> \"{end}\"[dir=both]")
                    already_handled.append((end, item))
                else:
                    lines.append(f"\"{item}\" -> \"{end}\"")

        lines.append("}")

        graph = "\n".join(lines)

        return graph
