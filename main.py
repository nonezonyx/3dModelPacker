from settings import RENDER_PREFIX, RENDER_SUFFIX, TEXTURE_PREFIX, NORMAL_MAP_OPENGL_SUFFIX, \
    NORMAL_MAP_DIRECTX_SUFFIX, MODEL_FOLDER_PREFIX
from formats_info import FORMAT_NAMES
from src import pack_3d_models


def main():
    working_path = input("Enter working path: ")
    project_name = input("Enter project name: ")
    pack_3d_models(working_path, project_name, FORMAT_NAMES, RENDER_PREFIX, RENDER_SUFFIX, TEXTURE_PREFIX,
                   NORMAL_MAP_OPENGL_SUFFIX, NORMAL_MAP_DIRECTX_SUFFIX, MODEL_FOLDER_PREFIX)


if __name__ == '__main__':
    main()
