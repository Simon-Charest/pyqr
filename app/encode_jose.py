from app import function
import jwt


def run(json_data, key):
    algorithms = 'HS256'
    headers = {"kid": key}
    token = encode_jose(json_data, key, algorithms, headers)

    return token


def encode_jose(json_data, key, algorithms='HS256', headers=None):
    return jwt.encode(json_data, key, algorithms, headers)
