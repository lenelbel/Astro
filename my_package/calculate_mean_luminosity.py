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
    for i, events_folder in enumerate(events_folders): # Начинается цикл по всем папкам с событиями, при этом i - индекс текущего элемента, events_folder - сама папка
        event_files = natsorted(os.listdir(events_folder)) #Получаем список изображений в папке events_folder и сортируем их естественным образом
        images_folder = images_folders[i] # Получаем соответствующую папку с изображениями активности из images_folders по индексу i
        image_files = natsorted(os.listdir(images_folder)) # Получаем список изображений в images_folder и сортируем их естественным образом
        total_luminosity = 0 #Инициализируем переменную total_luminosity для хранения общего уровня светимости.
        
        for j, event_image in enumerate(event_files): #Начинается вложенный цикл по изображениям в event_files, где j - индекс текущего изображения, event_image - само изображение.
            event_image_path = os.path.join(events_folder, event_image) #Создаем путь к текущему изображению в events_folder.
            event_image_data = cv2.imread(event_image_path, cv2.IMREAD_GRAYSCALE) #Считываем изображение с использованием OpenCV в оттенках серого и сохраняем в event_image_data
            white_pixels = np.where(event_image_data > 0) #Находим позиции белых пикселей на изображении.
            
            image_image = image_files[j] #Получаем имя соответствующего изображения из image_files.
            image_image_path = os.path.join(images_folder, image_image) #Создаем путь к соответствующему изображению в images_folder
            image_image_data = cv2.imread(image_image_path, cv2.IMREAD_GRAYSCALE)#Считываем изображение с использованием OpenCV в оттенках серого и сохраняем в image_data
            luminosity = np.mean(image_image_data[white_pixels])#Вычисляем средний уровень светимости для белых пикселей на изображении c активностью
            total_luminosity += luminosity#Добавляем текущий уровень светимости к общему уровню светимости
        mean_luminosity.append(total_luminosity / len(event_files)) #обавляем средний уровень светимости для текущего события в список mean_luminosity
    
    return mean_luminosity