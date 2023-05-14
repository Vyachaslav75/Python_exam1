import json


def export_file(data, file_name='notes.json'):
    with open(file_name, 'w') as file:

        json.dump(data, file)


def import_file(file_name='notes.json'):
    with open(file_name) as file:
        data = json.load(file)
        return data
