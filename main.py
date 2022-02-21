#!/usr/bin/python
# coding: utf-8

from app import decode_qr, io


def main():
    json_data = decode_qr.run('data/ac.png', True)
    io.dump_json(json_data, 'data/ac.json')


if __name__ == '__main__':
    main()
