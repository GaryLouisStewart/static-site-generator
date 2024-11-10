"""
author: Gary Louis Stewart, gary-stewart@outlook.com
date: 10/11/2024
"""


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    current_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        current_blocks.append(block)
    return current_blocks
