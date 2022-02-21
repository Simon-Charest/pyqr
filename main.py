#!/usr/bin/python
# coding: utf-8

from app import decode_qr, encode_jose, encode_qr, function, io


def main():
    input_image_file = 'data/ac.png'
    output_image_file = 'data/ac2.png'
    json_file = 'data/ac.json'

    # Decode QR code image to JSON data
    # json_data = decode_qr.run(input_image_file, True)

    # Write JSON data to file
    # io.dump_json(json_data, json_file)

    # Read JSON data from file
    json_data = io.load_json(json_file)
    # function.debug(json_data, 'json_data')

    # Encode JSON data to QR code image
    # shc_data = decode_qr.decode_to_shc(input_image_file)
    # encode_qr.encode(shc_data, output_image_file)

    # TODO
    encode_qr.run(json_file, True)

    # TODO
    token = encode_jose.run(json_data, 'qFdl0tDZK9JAWP6g9_cAv57c3KWxMKwvxCrRVSzcxvM')
    function.debug(token, 'token')


if __name__ == '__main__':
    main()
