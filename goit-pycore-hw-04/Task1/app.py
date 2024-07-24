from os import path

def total_salary(file_path):
    total_salary = 0
    count = 0
    try:
        parent_dir = path.dirname(path.abspath(__file__))
        with open(path.join(parent_dir, '', file_path), 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  # Видаляємо зайві пробіли і нові рядки
                if line:
                    name, salary_str = line.split(',')
                    salary = float(salary_str)
                    total_salary += salary
                    count += 1
        if count == 0:
            return (0, 0)  # Якщо не було жодного рядка в файлі
        return (total_salary, (total_salary / count)) 
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)


# Приклад використання:
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")