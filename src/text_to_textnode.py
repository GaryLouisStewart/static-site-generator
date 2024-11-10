"""
author: Gary Louis Stewart, gary-stewart@outlook.com
date: 10/11/2024
"""

from textnode import (
    TextNode,
    TextType
)

from inline_markdown import (
    split_nodes_link,
    split_nodes_image,
    split_nodes_delimiter,
)


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT.value)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD.value)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC.value)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE.value)

    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)

    return nodes


