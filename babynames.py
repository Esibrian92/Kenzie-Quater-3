#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""

import sys
import re
import argparse
import re


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """

    # read the file.
    # print all text from file
    # grab the tags from the html file
    # grab just the names or ranking
    names = []
    pattern = r"<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>"
    with open(filename, "r") as f:
        content = f.read()
        year_patern = r"\d\d\d+"
        year = re.findall(year_patern, filename)
    matches = re.findall(pattern, content)
    for name in matches:
        names = name[1:]
        value = name[0]
        for key in names:
            key = key
        node = (key, value)
        #got key and value 
        # if the key is already there then take it of and replace it with the new one
    new_node = node
    if new_node == node:
        node.remove(node)
        
    # new_dict = dict(matches)
    # print(new_dict)
    # for rank,names in enumerate(matches):
    #     for i,name in enumerate(names):
    #         name_pattern = r"\w+"
    #         name_macthes = re.findall(name_pattern,name)
    #         name_macthes
    #         break
    # return a list
    #   turn the dict to a list.
    # sort the list in alphabetical order
    #   ranking first


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more
    # filenames. It will also expand wildcards just like the shell.
    # e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    # Create a command line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files

    # option flag
    create_summary = ns.summaryfile

    # For each filename, call `extract_names()` with that single file.
    # Format the resulting list as a vertical list (separated by newline \n).
    # Use the create_summary flag to decide whether to print the list
    # or to write the list to a summary file (e.g. `baby1990.html.summary`).

# loop through the list and call extract_names for every item in the list.
# if create_summary is True then write a new line for every outcome
    for file in file_list:
        outcome = extract_names(file)
        if create_summary:
            with open(f"{file}.summary", "w") as f:
                f.write('\n'.join(outcome))
        else:
            pass
            # print('\n'.join(outcome))


if __name__ == '__main__':
    main(sys.argv[1:])
