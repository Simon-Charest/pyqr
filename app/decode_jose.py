import jwt


def decode_jose(token, key, algorithms='HS256', headers=None):
    return jwt.decode(token, key, algorithms, headers)
