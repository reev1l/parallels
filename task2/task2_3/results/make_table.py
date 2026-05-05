import csv

# Имя твоего файла
filename = "lab2_var2_threads.csv"

try:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        # Читаем заголовки
        headers = next(reader)
        
        # Печатаем заголовки в формате Markdown
        print(f"| {' | '.join(headers)} |")
        
        # Печатаем разделитель Markdown (например: |---|---|---|)
        separator = ['---'] * len(headers)
        print(f"| {' | '.join(separator)} |")
        
        # Печатаем строки данных
        for row in reader:
            print(f"| {' | '.join(row)} |")

except FileNotFoundError:
    print(f"Файл {filename} не найден.")