from os import path

def get_cats_info(file_path):
    result = []
    try:
        parent_dir = path.dirname(path.abspath(__file__))
        with open(path.join(parent_dir, '', file_path), 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  # Видаляємо зайві пробіли і нові рядки
                if line:
                    id, name, age = line.split(',')
                    result.append({"id":id, "name":name, "age": age})
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    return result
    

# Приклад використання:
cats_info = get_cats_info("cats_file.txt")
print(cats_info)