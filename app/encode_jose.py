from app import function
import jwt


def run(json_data):
    key = 'qFdl0tDZK9JAWP6g9_cAv57c3KWxMKwvxCrRVSzcxvM'
    algorithms = 'HS256'
    headers = {"kid": "qFdl0tDZK9JAWP6g9_cAv57c3KWxMKwvxCrRVSzcxvM"}
    token = encode_jose(json_data, key, algorithms, headers)
    print('encode_jose')
    function.debug(token, 'token')


def encode_jose(json_data, key, algorithms='HS256', headers=None):
    return jwt.encode(json_data, key, algorithms, headers)
