import os
import shutil


def copy_src_dest(src, dst):
    # check that the source directory exists
    if not os.path.exists(src):
        raise NotADirectoryError(f"Source Directory: {src} does not exist.")

    # delete all contents of the destination directory to ensure that the copy is clean.

    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    def recursive_copy(src_path, dst_path):
        for item in os.listdir(src_path):
            s = os.path.join(src_path, item)
            d = os.path.join(dst_path, item)
            if os.path.isdir(s):
                os.mkdir(d)
                print(f"Creating Directory: {d}")
                recursive_copy(s, d)
            else:
                shutil.copy(s, d)
                print(f"Copied file: {d}")

    recursive_copy(src, dst)
