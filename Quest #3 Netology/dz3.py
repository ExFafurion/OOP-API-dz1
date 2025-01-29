# Создаем список файлов с их содержимым и количеством строк
files_info = [
    ('1.txt', 'c:/Users/Zver/Desktop/Quest #3 Netology/1.txt'),
    ('2.txt', 'c:/Users/Zver/Desktop/Quest #3 Netology/2.txt'),
    ('3.txt', 'c:/Users/Zver/Desktop/Quest #3 Netology/3.txt'),
]

# Список для хранения информации о файлах
files_data = []

# Читаем содержимое файлов и сохраняем информацию
for file_name, file_path in files_info:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        line_count = content.count('\n') + 1  # Подсчет количества строк
        files_data.append((file_name, line_count, content))

# Сортируем файлы по количеству строк
files_data.sort(key=lambda x: x[1])

# Записываем в новый файл
with open('c:/Users/Zver/Desktop/Quest #3 Netology/merged.txt', 'w', encoding='utf-8') as merged_file:
    for file_name, line_count, content in files_data:
        merged_file.write(f"{file_name}\n{line_count}\n{content}\n")

print(files_data)