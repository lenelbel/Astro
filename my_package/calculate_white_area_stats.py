import cv2
import numpy as np
import pandas as pd
def calculate_white_area_stats(path):
    """
    Данная функция calculate_white_area_stats вычисляет число белых областей на изображении и их площадь.

    Аргументы:
    path (str): Путь к изображению в градациях серого.

    Возвращает:
    tuple: Количество белых областей и средняя площадь в микрометрах квадратных.

    Пример использования:
    >>> white_areas_count, avg_area_in_mkm = calculate_white_area_stats('/path/to/image.png')
    >>> print(white_areas_count)
    >>> print(avg_area_in_mkm)
    """
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    contours = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    white_areas_count = 0
    total_area = 0

    for contour in contours:
        area = cv2.contourArea(contour)
        white_areas_count += 1
        total_area += area
    
    spatial_scale = 5.1
    avg_area_in_pixels = total_area / white_areas_count if white_areas_count > 0 else 0
    avg_area_in_mkm = avg_area_in_pixels / (spatial_scale ** 2) if avg_area_in_pixels > 0 else 0 
   
    return white_areas_count, avg_area_in_mkm
