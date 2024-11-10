"""
author: Gary Louis Stewart, gary-stewart@outlook.com
date: 10/11/2024
"""

from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page using template {template_path} from {from_path} to {dest_path}")

    with open(from_path, 'r') as f:
        file = f.read()

    with open(template_path, 'r') as t:
        template = t.read()

    html_string = markdown_to_html_node(file).to_html()
    page_title = extract_title(file)

    completed_template = template.replace("{{ Title }}", page_title).replace("{{ Content }}", html_string)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as d:
        d.write(completed_template)


def generate_pages_recursive(dir_path_content, template_path, dest_path):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # now iterate through the folders using os.walk to find each file corresponding with 'index.md' and generate a
    # page based on this file.

    # we will need to walk this content_path directory.
    content_path = os.path.join(project_root, dir_path_content)
    dest_path = os.path.join(project_root, dest_path)

    for dirpath, dirname, filenames in os.walk(content_path):
        for filename in filenames:
            if filename.endswith(".md"):
                file_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(file_path, content_path)
                base_name = os.path.splitext(relative_path)[0]
                dest_file_path = os.path.join(dest_path, base_name + ".html")
                # generate page recursively.
                generate_page(file_path, template_path, dest_file_path)
