import matplotlib.pyplot as plt
def save_graph(gragh, name_graph_png, name_graph_svg):
    """
    Данная функция save_graph сохраняет график в файлы PNG и SVG.

    Аргументы:
    graph: График для сохранения.
    name_graph_png (str): Имя файла для сохранения графика в формате PNG.
    name_graph_svg (str): Имя файла для сохранения графика в формате SVG.

    Пример использования:
    >>> save_graph(graph, 'graph.png', 'graph.svg')
    """
    gragh.savefig(name_graph_png)
    gragh.savefig(name_graph_svg)