"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('001.txt') as f:
    text_lines = f.readlines()
    print(f'Количество строк в файле {f.name} = {len(text_lines)};')
    for i, line in enumerate(text_lines):
        print(f'В {i + 1} строке {len(line.split())} слов/слова.')