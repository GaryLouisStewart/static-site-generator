import os

from copystatic import copy_src_dest
from generate_page import generate_pages_recursive


def main():
    # set path so that no matter where we run this script from it always finds the right directories in our project.
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # set file paths below
    static_path = os.path.join(project_root, "static")
    public_path = os.path.join(project_root, "public")
    template_file = os.path.join(project_root, "template.html")
    content_path = os.path.join(project_root, "content")

    # debug paths print(f"Public Path: {public_path}\nStatic Path: {static_path}\nTemplate file Path: {
    # template_file}\nContent path: {content_path}\nFinal output file: {final_output_file}")

    copy_src_dest(static_path, public_path)
    generate_pages_recursive(content_path, template_file, public_path)


if __name__ == '__main__':
    main()
