import pandas as pd
def create_luminosity_dataframe(folder_names, mean_luminosity):
    """
    Данная функция create_luminosity_dataframe создает DataFrame с данными о средней светимости для каждой из 6-ти папок.

    Аргументы:
    folder_names (list): Список имен папок.
    mean_luminosity (list): Список со средней светимостью для каждой папки.

    Возвращает:
    DataFrame: DataFrame с данными о средней светимости.

    Пример использования:
    >>> luminosity_df = create_luminosity_dataframe(folder_names, mean_luminosity)
    >>> luminosity_df
    """
    df = pd.DataFrame({
        'Folder Name': folder_names,
        'Mean Luminosity': mean_luminosity
    })
    return df