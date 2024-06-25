from my_package.create_folders_lists import create_folders_lists
from my_package.read_dataframe import read_dataframe
from my_package.calculate_white_area_stats import calculate_white_area_stats
from my_package.add_white_area_info_to_df import add_white_area_info_to_df
from my_package.graph_average_area import graph_average_area
from my_package.save_graph import save_graph
from my_package.save_data_average_area import save_data_average_area
from my_package.calculate_mean_luminosity import calculate_mean_luminosity
from my_package.save_luminosity_to_excel import save_luminosity_to_excel
from my_package.create_luminosity_dataframe import create_luminosity_dataframe
import os
def run_all_functions(main_path):
    """
    Данная функция run_all_functions запускает все функции для обработки данных, построения графиков и сохранения результатов.

    Аргументы:
    main_path (str): Путь к главной папке с данными.

    Возвращает:

    DataFrame с общей средней светимостью для каждой папки.
    значение общей средней светимостью для конкретной папки
    DataFrame со средняя площадью области в зависимости от времени

    Пример использования:
    >>> main_folder_path ='C:/Astro/Task Astrocytes'
    >>> run_all_functions(main_folder_path)
    """
    images_folders, events_folders, folder_names = create_folders_lists(main_path)
    
    for i in range(len(events_folders)):
        df = read_dataframe(events_folders[i], folder_names[i])
        df_with_white_area = add_white_area_info_to_df(df)
        graph = graph_average_area(df_with_white_area)

        mean_luminosity = calculate_mean_luminosity([images_folders[i]], [events_folders[i]], [folder_names[i]])
        print("Mean Luminosity for folder:", f"{folder_names[i]}: = {mean_luminosity[0]}")

        folder_name = folder_names[i]
        path_to_save = rf'C:\Astro\results\{folder_name}'

        if not os.path.exists(path_to_save):
            os.makedirs(path_to_save)

        os.chdir(path_to_save)

        save_graph(graph, f"graph_{folder_names[i]}.png", f"graph_{folder_names[i]}.svg")
        save_data_average_area(df_with_white_area, f"data_{folder_names[i]}.xlsx")
        save_luminosity_to_excel([mean_luminosity], [folder_names[i]], f"luminosity_{folder_names[i]}.xlsx")
        
        common_mean_luminosity = calculate_mean_luminosity(images_folders, events_folders, folder_names)
        common_luminosity_df = create_luminosity_dataframe(folder_names, common_mean_luminosity)
        save_luminosity_to_excel(common_mean_luminosity, folder_names)
    print(common_luminosity_df)