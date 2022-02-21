import json


def dump_json(json_data, file, mode='w', indent=2):
    stream = open(file, mode)
    json.dump(json_data, stream, indent=indent)
    stream.close()
