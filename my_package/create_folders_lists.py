import os
def create_folders_lists(main_path):
    """
    Данная функция create_folders_lists создает списки папок для изображений и событий, а также список названий папок.

    Аргументы:
    main_path (str): путь к основной папке.

    Возвращает:
    images_folders (list): список папок с изображениями.
    events_folders (list): список папок с событиями.
    folder_names (list): список названий папок.

    Пример использования:
    >>> main_path ='C:/Astro/Task Astrocytes'
    >>> images_folders, events_folders, folder_names = create_folders_lists(main_path)
    >>> print(images_folders, events_folders)
    >>> print(folder_names)
    """
    images_folders = []
    events_folders = []
    folder_names = []
    for folder_name in os.listdir(main_path):
        folder_names.append(folder_name)
        folder_path = os.path.join(main_path, folder_name)
        subfolders = os.listdir(folder_path)
        events_folder_path = os.path.join(folder_path, subfolders[0])
        images_folder_path = os.path.join(folder_path, subfolders[1])

        images_folders.append(images_folder_path)
        events_folders.append(events_folder_path)

    return images_folders, events_folders, folder_names
