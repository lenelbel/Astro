import cv2
import os
import pandas as pd
from natsort import natsorted
def read_dataframe(folder, name_dataset):
    """
    Данная функция read_dataframe читает данные изображений из папки и создает DataFrame с информацией об изображениях.

    Аргументы:
    folder (str): Путь к папке с изображениями.
    name_dataset (str): Название набора данных для метки в DataFrame.

    Возвращает:
    DataFrame: DataFrame с информацией об изображениях.

    Пример использования:
    >>> df = read_dataframe('C:\\Astro\\Task Astrocytes\\31_08_2020_tser1\\events', 'dataset1')
    >>> df
    """
    data = []
    image_names = natsorted(os.listdir(folder))  
    for image_name in image_names:
        image_path = os.path.join(folder, image_name)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        image_data = {
            'dataset': name_dataset,
            'image_name': image_name,
            'image_path': image_path,
            'image_size': image.shape}
        data.append(image_data)
    df = pd.DataFrame(data)
    return df