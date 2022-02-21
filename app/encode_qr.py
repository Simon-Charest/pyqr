from app import function, io
import base64
import json
import pyqrcode
import zlib


def run(file, verbose=False):
    json_data = io.load_json(file)
    json_string = json.dumps(json_data)
    binary_data = json_string.encode()
    compressed_data = compress(binary_data)
    base64_data = encode_to_base64(compressed_data)

    if verbose:
        function.print_function()
        function.debug(file, 'file')
        function.debug(json_data, 'json_data')
        function.debug(json_string, 'json_string')
        function.debug(binary_data, 'binary_data')
        function.debug(compressed_data, 'compressed_data')
        function.debug(base64_data, 'base64_data')

    # shc_data = decode_to_shc(file)
    # jws_data = decode_to_jws(shc_data)
    # jws_data_list = jws_data.split('.')
    # base64_data = list(map(decode_to_base64, jws_data_list))
    # binary_data = decompress(base64_data[1])
    # json_data = json.loads(binary_data)


def compress(data, level=6, method=zlib.DEFLATED, wbits=15, memLevel=8, strategy=zlib.Z_DEFAULT_STRATEGY):
    compression_object = zlib.compressobj(level=level, method=method, wbits=wbits, memLevel=memLevel, strategy=strategy)
    data = compression_object.compress(data)
    compression_object.flush()

    return data


def encode(content, file, error='L', version=34, mode='binary', scale=6):
    qr_code = pyqrcode.create(content, error=error, version=version, mode=mode)
    qr_code.png(file, scale=scale)


def encode_to_base64(jws_data):
    base64_data = base64.urlsafe_b64encode(jws_data)

    return base64_data
