from dataclasses import dataclass
import statistics


def calculate_pixel_brightness(red:int, green:int, blue:int) -> float:
    """Calculates the brightness of a pixel from its r,g,b values."""
    return statistics.mean([red, green, blue])


@dataclass
class Pixel:
    red: int
    green: int
    blue: int


pixels = [
    Pixel(red=100, green=0, blue=0),
    Pixel(red=100, green=0, blue=0),
]

pixel_brightnesses = [calculate_pixel_brightness(pixel['red'], pixel['green'], pixel['blue']) for pixel in pixels]
mean_brightness = calculate_pixel_brightness(pixel_brightnesses)
print(mean_brightness)
