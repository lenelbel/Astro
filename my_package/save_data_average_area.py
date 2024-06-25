import pandas as pd
def save_data_average_area(df, name_table):
    """
    Данная функция  save_data_average_area сохраняет данные о средней площади белых областей в Excel файл.

    Аргументы:
    df (DataFrame): DataFrame с данными для сохранения.
    name_table (str): Имя Excel файла для сохранения данных.

    Пример использования:
    >>> save_data_average_area(df_with_info, 'data.xlsx')
    """
    time_average_area_df = df[['time_seconds', 'average_area']].copy()
    print(time_average_area_df)
    time_average_area_df.to_excel(name_table)