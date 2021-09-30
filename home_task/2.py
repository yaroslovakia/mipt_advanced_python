def write_array(array, file_name):
    """записывает строки из array в файл file_name"""
    lst1 = '/n'.join(array)
    with open("file_name", "w") as fll:
        fll.write(lst1)
    pass


