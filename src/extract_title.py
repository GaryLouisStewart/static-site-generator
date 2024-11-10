"""
author: Gary Louis Stewart, gary-stewart@outlook.com
date: 10/11/2024
"""


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    else:
        raise Exception("No h1 header found.")
