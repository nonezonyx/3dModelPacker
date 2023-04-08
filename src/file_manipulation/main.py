import glob
import ntpath
import os
import shutil


def get_files(path_to_files):
    files = glob.glob(path_to_files+"/*")
    return files


def get_file_name(path_to_file):
    return ntpath.basename(path_to_file)


def move_file(old_path: str, new_path: str, remove_old: bool = True):
    new_directory = os.path.dirname(new_path)
    if not os.path.exists(new_directory):
        os.mkdir(new_directory)
    if remove_old:
        os.replace(old_path, new_path)
    else:
        shutil.copy(old_path, new_directory)
