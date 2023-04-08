def validate_string(string: str, prefix: str, suffix: str) -> bool:
    return string.startswith(prefix) and string.endswith(suffix)


def identify_image(image: str, render_prefix: str, render_suffix: str, texture_prefix: str) -> str:
    name = ''.join(image.split('.')[:-1])
    if validate_string(name, render_prefix, render_suffix):
        return 'render'
    if validate_string(name, texture_prefix, ''):
        return 'texture'
    return 'unknown'


def detect_type(file_name: str, formats_info: dict[str, list[str]], render_prefix: str, render_suffix: str,
                texture_prefix: str) -> str:
    file_extension = file_name.split('.')[-1]
    for name, extensions in formats_info.items():
        if file_extension in extensions:
            if name == 'image':
                return identify_image(file_name, render_prefix, render_suffix, texture_prefix)
            return name
    return 'unknown'


def detect_types(file_names: list[str], formats_info: dict[str, list[str]], render_prefix: str, render_suffix: str,
                 texture_prefix: str) -> dict[str, list[str]]:
    dictionary = {}
    for file_name in file_names:
        file_type = detect_type(file_name, formats_info, render_prefix, render_suffix, texture_prefix)
        if file_type in dictionary:
            dictionary[file_type].append(file_name)
        else:
            dictionary[file_type] = [file_name]
    return dictionary
