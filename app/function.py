import base64
import datetime
import inspect
import zlib


def run():
    iat = 1630263124.0
    debug(convert(iat), 'iat')


def convert(iat, fmt='%Y-%m-%d %H:%M:%S'):
    timestamp = datetime.datetime.fromtimestamp(iat)

    return timestamp.strftime(fmt)


def debug(object_, name=None):
    print(f'{type(object_).__name__}[{len(object_)}] {name} = {object_}')


def decode_base64_and_inflate(b64string):
    decoded_data = base64.b64decode(b64string)

    return zlib.decompress(decoded_data, -15)


def deflate_and_base64_encode(string_val):
    zlibbed_str = zlib.compress(string_val)
    compressed_string = zlibbed_str[2:-4]

    return base64.b64encode( compressed_string )


def print_function():
    print(inspect.currentframe().f_back.f_code.co_name)
