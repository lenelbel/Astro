import cv2
import numpy as np
import pandas as pd
from my_package.calculate_white_area_stats import calculate_white_area_stats
def add_white_area_info_to_df(df):
    """
    Данная функция add_white_area_info_to_df добавляет информацию о белых областях в DataFrame.

    Аргументы:
    df (DataFrame): DataFrame, к которому нужно добавить информацию.

    Возвращает:
    DataFrame: Обновленный DataFrame с информацией о белых областях.

    Пример использования:
    >>> df_with_info = add_white_area_info_to_df(df)
    >>> print(df_with_info)
    """
 
    white_areas_count = []
    average_areas = []
    for image_path in df['image_path']:
        result_function_1 = calculate_white_area_stats(image_path)  
        white_areas_count.append(result_function_1[0])
        average_areas.append(result_function_1[1])
    
    df['white_areas_count'] = white_areas_count
    df['average_area'] = average_areas
    
    return df