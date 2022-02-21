import json


def dump_json(json_data, file, mode='w', indent=2):
    stream = open(file, mode)
    json.dump(json_data, stream, indent=indent)
    stream.close()


def load_json(file):
    stream = open(file)
    json_data = json.load(stream)
    stream.close()

    return json_data
