"""
author: Gary Louis Stewart, gary-stewart@outlook.com
date: 10/11/2024
"""

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def block_to_block_type(markdown):
    """
    Headings start with 1-6 # characters, followed by a space and then the heading text.
    Code blocks must start with 3 backticks and end with 3 backticks.
    Every line in a quote block must start with a > character.
    Every line in an unordered list block must start with a * or - character, followed by a space.
    Every line in an ordered list block must start with a number followed by a . character and a space.
    The number must start at 1 and increment by 1 for each line.

    If none of the above conditions are met, the block is a normal paragraph.

    :param markdown:
    :return a string representing the markdown block type:
    """

    lines = markdown.split("\n")
    if markdown.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if markdown.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if markdown.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if markdown.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if markdown.startswith("1."):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph
