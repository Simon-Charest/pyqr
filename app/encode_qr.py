import base64
import pyqrcode
import zlib


def compress(data, level=6, method=zlib.DEFLATED, wbits=15, memLevel=8, strategy=zlib.Z_DEFAULT_STRATEGY):
    compression_object = zlib.compressobj(level=level, method=method, wbits=wbits, memLevel=memLevel, strategy=strategy)
    data = compression_object.compress(data)
    compression_object.flush()

    return data


def encode(string, filepath, scale=6):
    qr = pyqrcode.create(string)
    qr.png(filepath, scale=scale)


def encode_to_base64(jws_data):
    base64_data = base64.urlsafe_b64encode(jws_data)

    return base64_data
