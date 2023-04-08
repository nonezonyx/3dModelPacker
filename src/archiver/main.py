from shutil import make_archive


def zip_directory(directory_path) -> None:
    make_archive(directory_path, "zip", directory_path)
