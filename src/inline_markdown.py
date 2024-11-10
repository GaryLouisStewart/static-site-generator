from textnode import (
    TextNode,
    TextType
)

from extract_markdown_elements import (
    extract_markdown_links,
    extract_markdown_images,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue
        temp_nodes = []
        split_string = node.text.split(delimiter)

        if len(split_string) % 2 == 0:
            raise ValueError("Unmatched delimiter found in text: '{}'".format(node.text))

        for i, part in enumerate(split_string):
            if part == "":
                continue
            if i % 2 == 0:
                temp_nodes.append(TextNode(part, TextType.TEXT.value))
            else:
                temp_nodes.append(TextNode(part, text_type))
        new_nodes.extend(temp_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for img in images:
            sections = original_text.split(f"![{img[0]}]({img[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT.value))
            new_nodes.append(TextNode(
                img[0],
                TextType.IMAGE.value,
                img[1],
            )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT.value))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT.value))
            new_nodes.append(TextNode(link[0], TextType.LINK.value, link[1],))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT.value))
    return new_nodes
