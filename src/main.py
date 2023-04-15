from .file_manipulation import get_files, get_file_name, move_file
from .file_manipulation.type_detection import detect_types
from .image_manupulation import convert_normal
from .archiver import zip_directory
import shutil


def get_new_normal_name(name: str, normal_map_opengl_suffix: str, normal_map_directx_suffix: str) -> str:
    extension = name.split('.')[-1]
    name = ''.join(name.split('.')[:-1])
    if name.endswith(normal_map_opengl_suffix):
        return f"{name[:-len(normal_map_opengl_suffix)]}{normal_map_directx_suffix}.{extension}"
    if name.endswith(normal_map_directx_suffix):
        return f"{name[:-len(normal_map_directx_suffix)]}{normal_map_opengl_suffix}.{extension}"
    return f"{name}.{extension}"


def sort_3d_models(working_path, project_name: str, file_dict: dict[str, list[str]],
                   model_folder_prefix: str) -> dict[str, list[str] | str]:
    textures_folder_name = f"{working_path}\\Textures_{project_name}"
    renders_folder_name = f"{working_path}\\Renders_{project_name}"
    folders = {'model_folders': set(), 'render': renders_folder_name, 'texture': textures_folder_name}
    for name, files in file_dict.items():
        for file in files:
            file_path = f"{working_path}\\{file}"
            if name == 'render':
                move_file(file_path, f"{renders_folder_name}\\{file}")
            elif name == 'texture':
                move_file(file_path, f"{textures_folder_name}\\{file}")
            elif name != 'unknown':
                model_folder = f"{working_path}\\{model_folder_prefix}{project_name}_{name}"
                move_file(file_path, f"{model_folder}\\{file}")
                folders['model_folders'].add(model_folder)
    return folders


def pack_3d_models(working_path, project_name: str, formats_info: dict[str, list[str]], render_prefix: str,
                   render_suffix: str, texture_prefix: str, normal_map_opengl_suffix: str,
                   normal_map_directx_suffix: str, model_folder_prefix: str):
    file_paths = get_files(working_path)
    file_names = [get_file_name(file_path) for file_path in file_paths]
    file_dict = detect_types(file_names, formats_info, render_prefix, render_suffix, texture_prefix)
    folders = sort_3d_models(working_path, project_name, file_dict, model_folder_prefix)
    normal_maps = [texture for texture in get_files(folders['texture'])
                   if (name := ''.join(texture.split('.')[:-1])).endswith(normal_map_opengl_suffix)
                   or name.endswith(normal_map_directx_suffix)]
    for normal_map in normal_maps:
        convert_normal(normal_map).save(get_new_normal_name(normal_map,
                                                            normal_map_opengl_suffix, normal_map_directx_suffix))
    textures = get_files(folders['texture'])
    for model_folder in folders['model_folders']:
        for texture in textures:
            move_file(texture, f"{model_folder}\\{get_file_name(texture)}", remove_old=False)
        zip_directory(model_folder)
        shutil.rmtree(model_folder)
    zip_directory(folders['texture'])
    shutil.rmtree(folders['texture'])
    zip_directory(folders['render'])
    shutil.rmtree(folders['render'])
