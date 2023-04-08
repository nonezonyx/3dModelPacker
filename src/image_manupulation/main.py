from PIL import Image
from PIL.ImageChops import invert
from enum import Enum


class Channel(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


def invert_channel(image: Image, chanel: Channel = Channel.GREEN) -> Image:
    """invert_chanel(image: Image, chanel: Channel = Channel.GREEN) -> Image
inverts one image channel"""
    red, green, blue = image.split()
    if chanel == Channel.RED:
        return Image.merge('RGB', (invert(red), green, blue))
    elif chanel == Channel.GREEN:
        return Image.merge('RGB', (red, invert(green), blue))
    elif chanel == Channel.BLUE:
        return Image.merge('RGB', (red, green, invert(blue)))
    else:
        return image


def convert_normal(normal_map: str) -> Image:
    """convert_normal(normal_map: Image) -> Image
converts OpenGl normal map into DirectX and backwards"""
    with Image.open(normal_map) as image:
        return invert_channel(image)
