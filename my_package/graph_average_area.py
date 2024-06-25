import pandas as pd
import matplotlib.pyplot as plt
def graph_average_area(df):
    """
    Данная функция graph_average_area создает график средней площади белых областей в зависимости от времени.

    Аргументы:
    df (DataFrame): DataFrame с информацией для построения графика.

    Возвращает:
    Объект графика matplotlib.

    Пример использования:
    >>> graph = graph_average_area(df_with_info)
    >>> graph.show()
    """

    df['time_seconds'] = df.index / 2

    gragh = plt.figure(figsize=(6.49, 3.37), dpi=300)   
    plt.plot(df['time_seconds'], df['average_area'], color='#7B68EE', linewidth=3)
    plt.xlabel('Время, c')
    plt.ylabel('Средняя площадь области, мкм²')
    plt.title('Средняя площадь области в зависимости от времени')
    plt.xlim(df['time_seconds'].min(), df['time_seconds'].max())
    plt.ylim(df['average_area'].min(), df['average_area'].max())
    plt.legend(['Средняя площадь'], loc='upper right')
    plt.tight_layout()
    plt.show()
    return gragh