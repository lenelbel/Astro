import pandas as pd
from my_package.create_luminosity_dataframe import create_luminosity_dataframe
def save_luminosity_to_excel(mean_luminosity, folder_names, file_name='luminosity.xlsx'):
    """
    Данная функция save_luminosity_to_excel сохраняет данные о средней светимости в Excel файл.

    Аргументы:
    mean_luminosity (list): Список со средней светимостью для каждой папки.
    folder_names (list): Список имен папок.
    file_name (str): Имя Excel файла для сохранения данных. По умолчанию 'luminosity.xlsx'.

    Пример использования:
    >>> save_luminosity_to_excel(mean_luminosity, folder_names, 'luminosity_data.xlsx')
    """
    # Создаем DataFrame с данными
    df = create_luminosity_dataframe(folder_names, mean_luminosity)
    
    # Сохраняем DataFrame в файл Excel
    df.to_excel(file_name, index=False)
    
    print(f"Data saved to {file_name}")