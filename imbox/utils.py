def str_encode(value='', encoding=None, errors='strict'):
    return str(value, encoding, errors)


def str_decode(value, encoding=None, errors='strict'):
    try:
        return bytes(value, encoding, errors).decode('utf-8')
    except:
        try:
            return value.decode(encoding)
        except:
            return str(value)
