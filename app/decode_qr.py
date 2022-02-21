from app import function
from PIL import Image
from pyzbar.pyzbar import decode
import base64
import json
import re
import zlib


def run(file, verbose=False):
    shc_data = decode_to_shc(file)
    jws_data = decode_to_jws(shc_data)
    jws_data_list = jws_data.split('.')
    base64_data = list(map(decode_to_base64, jws_data_list))
    binary_data = decompress(base64_data[1])
    json_data = json.loads(binary_data)

    if verbose:
        function.print_function()
        function.debug(file, 'file')
        function.debug(shc_data, 'shc_data')
        function.debug(jws_data, 'jws_data')
        function.debug(jws_data_list, 'jws_data_list')
        function.debug(base64_data, 'base64_data')
        function.debug(binary_data, 'binary_data')
        function.debug(json_data, 'json_data')

    return json_data


def decode_to_shc(file, verbose=False):
    # Smart Health Card (SHC)

    shc_data = decode(Image.open(file))

    if shc_data:
        return shc_data[0].data.decode()

    if verbose:
        print(f'Error decoding {file}')

    return shc_data


def decode_to_jws(shc_data):
    # JSON Web Signature (JWS)

    data = re.findall('..', shc_data[5:])
    jws_data = ''

    for datum in data:
        jws_data += chr(int(datum) + 45)

    return jws_data


def decode_to_base64(jws_data):
    padding = len(jws_data) + len(jws_data) % 4
    jws_data = jws_data.ljust(padding, '=')
    base64_data = base64.urlsafe_b64decode(jws_data)

    return base64_data


def decompress(data, wbits=-15):
    return zlib.decompress(data, wbits)
