Этот пакет предоставляет функции для обработки и визуализации данных в наборах изображений кальциевой активности астроцитов.

## ФУНКЦИИ

• create_folders_lists(main_path): принимает путь к основной папке, и затем возвращает списки папок с изображениями интенсивностей для каждого пикселя  и изображениями, характеризующими кальциевые события внутри астроцитов, а также список имен папок.

• read_dataframe(folder, name_dataset): принимает путь к папке с изображениями  и читает изображения из этой папки и создает DataFrame с информацией о каждом изображении.

• calculate_white_area_stats(path): принимает путь к изображению и вычисляет количество белых областей и среднюю площадь белых областей на изображении.

• add_white_area_info_to_df(df): принимает DataFrame с информацией о изображениях и добавляет информацию о количестве белых областей и средней площади белых областей к DataFrame.

• graph_average_area(df): принимает DataFrame с информацией о изображениях и строит график зависимости средней площади области от времени.

• save_graph(gragh, name_graph_png, name_graph_svg): сохраняет график в форматах PNG и SVG.

• save_data_average_area(df, name_table): сохраняет таблицу с данными о средней площади области в формате Excel.

• calculate_mean_luminosity(images_folders, events_folders, folder_names): вычисляет средний уровень светимости для каждой папки с изображениями активности

• save_luminosity_to_excel(mean_luminosity, folder_names, file_name='luminosity.xlsx'): сохраняет среднюю светимость в формате Excel.

• create_luminosity_dataframe(folder_names, mean_luminosity): создает DataFrame с информацией о средней яркости.

• run_all_functions(main_path): принимает путь к основной папке, и затем вызывает остальные функции в правильном порядке и сохраняет результаты в соответствующие файлы.
## РЕЗУЛЬТАТЫ
В результате работы кода будут созданы следующие файлы:
• График средней площади области в зависимости от времени (graph_{имя_папки}.png, graph_{имя_папки}.svg).
• Таблица с данными о средней площади области (data_{имя_папки}.xlsx).
• Таблица с данными о среднем уровне светимости (luminosity_{имя_папки}.xlsx).
Файлы будут сохранены в папке results/{имя_папки}, которая будет создана автоматически, если ее нет.


## УСТАНОВКА
Для запуска кода необходимо выполнить следующие шаги:
1) Для корректной работы данного кода существует необходимость установки определенных пакетов. 
Данные пакеты представлены в файле requirements.txt. 
Для установки всех пакетов из requirements.txt необходимо выполнить команду "pip install -r requirements.txt" в командной строке или терминале.

2) установить данный пакет, воспользовавшись командой:
pip install my_package

3) импортировать необходимые функции из пакета:
from my_package import create_folders_lists, read_dataframe, calculate_white_area_stats, add_white_area_info_to_df, graph_average_area, save_graph, save_data_average_area, calculate_mean_luminosity, save_luminosity_to_excel, create_luminosity_dataframe, run_all_functions

4) Указать путь к папке с изображениями активности. Для этого необходимо изменить значение переменной main_path на нужный путь.

5) Запустить функцию run_all_functions(main_path), передав в нее путь к папке с изображениями активности. 
#Пример вызова функции:
main_path = 'путь_к_папке_с_изображениями'
run_all_functions(main_path)

## ИСПОЛЬЗОВАНИЕ(Пример использования функции run_all_functions)

from my_package import create_folders_lists, read_dataframe, calculate_white_area_stats, add_white_area_info_to_df, graph_average_area, save_graph, save_data_average_area, calculate_mean_luminosity, save_luminosity_to_excel, create_luminosity_dataframe, run_all_functions

main_path = 'C:/Astro/Task Astrocytes'
result = run_all_functions(main_path)
# ЛИЦЕНЗИЯ
Этот проект лицензирован по лицензии MIT - подробности см. в файле LICENSE.


*Для получения более подробной информации вы можете обратится к автору за дополнительной помощью:
Автор: Белоусова Елена
Email: elbel0603@gmail.com
