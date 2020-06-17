""" Utility functions """

import yaml

import subprocess


def get_meta_data(path):
    """ Get all yaml config data in the top '---' pandoc block at the top of the markdown file. """
    # open the markdown file
    with open(path, "r") as infile:
        lines = infile.readlines()

    # collect all lines between '---'
    yaml_lines = []
    started = False

    for line in lines:
        if line[:3] == "---" and not started:
            started = True
            continue
        elif line[:3] == "---" and started:
            break
        else:
            yaml_lines.append(line)

    # parse it out and return it!
    return read_yaml_metadata(yaml_lines)


def read_yaml_metadata(yaml_lines):
    """ Take an array of lines that contain yaml data and parse it """
    yaml_string = "".join(yaml_lines)
    data = yaml.full_load(yaml_string)
    return data


def from_tag_string(string):
    """ Returns a tag list. """
    if string is None:
        return []
    
    tags = string.split("#")
    
    # strip empty spaces and any blank tags from split
    tags = [tag.strip() for tag in tags if tag]
    return tags


def to_tag_string(tags):
    """ Returns a #string #like #this """
    line = ""
    for tag in tags:
        line += "#" + tag

    return line.strip()


def run_shell(*args):
    output = subprocess.run(args, stdout=subprocess.PIPE).stdout.decode('ascii').rstrip()
    return output

def run_raw_shell(*args):
    output = subprocess.run(args, stdout=subprocess.PIPE, shell=True).stdout.decode('ascii').rstrip()
    return output

def log(msg, src, level="info"):
    run_shell("kofi-log", src, level, msg)
