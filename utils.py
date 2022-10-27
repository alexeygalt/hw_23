# payload={
#   'file_name': 'apache_logs.txt',
#   'cmd1': 'filter',
#   'value1': 'GET',
#   'cmd2': 'map',
#   'value2': '0'
# }
from typing import Iterator


def do_command(command: str, value: str, file: Iterator) -> Iterator:
    if command == 'filter':
        file = filter(lambda x: value in x, file)

    elif command == 'map':
        file = map(lambda x: x.split()[int(value)], file)

    elif command == 'unique':
        file = set(file)

    elif command == 'sort':
        if value == 'desc':
            file = sorted(file, reverse=True)
        else:
            file = sorted(file)

    elif command == 'limit':
        file = [item for item in list(file)[:int(value)]]

    return file


def get_result(data: dict, file: Iterator) -> list:
    count = 1
    command = 'cmd' + str(count)
    value = 'value' + str(count)

    while command in data.keys() and value in data.keys():
        if command in data.keys():
            file = do_command(data[command], data[value], file)
        count += 1
        command = 'cmd' + str(count)
        value = 'value' + str(count)

    return list(file)
