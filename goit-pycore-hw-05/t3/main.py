import sys
import os


def parse_log_line(line: str) -> dict:
    date, time, level, message = line.split(maxsplit=3)
    return dict(
        date=date,
        time=time,
        level=level,
        message=message.strip()
    )


def load_logs(file_path: str) -> list:
    lst = []
    with open(file_path) as f:
        for line in f.readlines():
            lst.append(
                parse_log_line(line=line)
            )
    return lst


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda x: x.get('level').lower() == level, logs))


def count_logs_by_level(logs: list) -> dict:
    levels = [log.get('level') for log in logs]

    return {
        lvl: levels.count(lvl) for lvl in set(levels)
    }


def display_log_counts(counts: dict):
    print('Рівень логування | Кількість')
    print('-----------------|----------')
    for k, v in sorted(counts.items(), key=lambda x: -x[1]):
        print(f'{k:^17}|{v:^10}')


def display_log_filtered(filtered_logs: list, level: str):
    print(f'Деталі логів для рівня \'{level.upper()}\':')
    for log in filtered_logs:
        date = log.get('date')
        time = log.get('time')
        message = log.get('message')
        print(date, time, message)


def main():
    current_dir = os.getcwd()
    args = sys.argv
    if len(args) < 2:
        print('не заданий шлях до лог-файлу')
    else:
        path = os.path.join(current_dir, args[1])
        if not path.endswith('log'):
            print('неправильний формат лог-файлу')
        else:
            try:
                data = load_logs(file_path=path)
            except FileNotFoundError:
                print('відсутність файлу')
            else:
                if len(args) >= 2:
                    counts = count_logs_by_level(logs=data)
                    display_log_counts(counts=counts)
                    if len(args) > 2:
                        if args[2].lower() in ('info', 'debug', 'error', 'warning'):
                            level = args[2].lower()
                            data1 = filter_logs_by_level(logs=data, level=level)
                            display_log_filtered(filtered_logs=data1, level=level)
                        else:
                            print('некоректна назва рівня')


if __name__ == '__main__':
    main()
