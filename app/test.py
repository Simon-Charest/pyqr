from app import decode_qr, encode_qr
import zlib


def test_encode_decode(string='Hello World !', filename='data/hw.png'):
    encode_qr.encode(string, filename)
    print(decode_qr.decode_to_shc(filename))


def test_encode_qr_compress(data, expected):
    for level in list(range(-1, 10)):
        for method in [zlib.DEFLATED]:
            for wbits in list(range(-15, -8)) + list(range(9, 16)) + list(range(25, 32)):
                for memLevel in list(range(1, 10)):
                    for strategy in [zlib.Z_DEFAULT_STRATEGY, zlib.Z_FILTERED, zlib.Z_HUFFMAN_ONLY, zlib.Z_RLE,
                                     zlib.Z_FIXED]:
                        value = encode_qr.compress(data, level=level, method=method, wbits=wbits, memLevel=memLevel,
                                                   strategy=strategy)

                        if value == expected:
                            return [level, method, wbits, memLevel, strategy]

    return False


def test_zlib_compress(data, expected):
    for level in list(range(-1, 10)):
        value = zlib.compress(data, level)

        if value == expected:
            return level

    return False
