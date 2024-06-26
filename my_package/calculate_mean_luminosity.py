import cv2
import os
import numpy as np
from natsort import natsorted
def calculate_mean_luminosity(images_folders, events_folders, folder_names):
    """
    Данная функция вычисляет среднюю светимость для каждой из 6-ти папок с изображениями, находящимися в папке Task Astrocytes.

    Аргументы:
    images_folders (list): Список папок с изображениями интенсивностей для каждого пикселя (характеризует концентрацию кальция).
    events_folders (list): Список папок с изображениями, характеризующими кальциевые события (белый цвет - в данном пикселе на данном кадре наблюдается кальциевая активность клетки, то есть кальциевое событие).
    folder_names (list): Список имен папок.

    Возвращает:
    list: Список со средней светимостью для каждой папки.

    Пример использования:
    >>> mean_luminosity = calculate_mean_luminosity(images_folders, events_folders, folder_names)
    >>> mean_luminosity
    """

    mean_luminosity = []
    for i, events_folder in enumerate(events_folders): 
        event_files = natsorted(os.listdir(events_folder)) 
        images_folder = images_folders[i] 
        image_files = natsorted(os.listdir(images_folder)) 
        total_luminosity = 0 
        
        for j, event_image in enumerate(event_files): 
            event_image_path = os.path.join(events_folder, event_image) 
            event_image_data = cv2.imread(event_image_path, cv2.IMREAD_GRAYSCALE)
            white_pixels = np.where(event_image_data > 0) 
            
            image_image = image_files[j] 
            image_image_path = os.path.join(images_folder, image_image) 
            image_image_data = cv2.imread(image_image_path, cv2.IMREAD_GRAYSCALE)
            luminosity = np.mean(image_image_data[white_pixels])
            total_luminosity += luminosity
        mean_luminosity.append(total_luminosity / len(event_files)) 
    
    return mean_luminosity