decode_dict = {
    'a': 'z',
    'b': 'y',
    'c': 'x',
    'd': 'w',
    'e': 'v',
    'f': 'u',
    'g': 't',
    'h': 's',
    'i': 'r',
    'j': 'q',
    'k': 'p',
    'l': 'o',
    'm': 'n',
    'n': 'm',
    'o': 'l',
    'p': 'k',
    'q': 'j',
    'r': 'i',
    's': 'h',
    't': 'g',
    'u': 'f',
    'v': 'e',
    'w': 'd',
    'x': 'c',
    'y': 'b',
    'z': 'a',
}

encode_dict = {
    'z': 'a',
    'y': 'b',
    'x': 'c',
    'w': 'd',
    'v': 'e',
    'u': 'f',
    't': 'g',
    's': 'h',
    'r': 'i',
    'q': 'j',
    'p': 'k',
    'o': 'l',
    'n': 'm',
    'm': 'n',
    'l': 'o',
    'k': 'p',
    'j': 'q',
    'i': 'r',
    'h': 's',
    'g': 't',
    'f': 'u',
    'e': 'v',
    'd': 'w',
    'c': 'x',
    'b': 'y',
    'a': 'z',
}


def decode(w):
    decoded = ''

    for l in w.lower():
        decoded += decode_dict.get(l, '')

    return decoded


def encode(w):
    encoded = ''
    count = 0

    for l in w.lower().replace(' ', ''):
        if l.isdigit():
            encoded += l
            if count % 5 == 0:
                encoded += ' '
        elif count % 5 == 0 and count != 0 and l != '.':
            encoded += ' '
            encoded += decode_dict.get(l, '')
        else:
            encoded += decode_dict.get(l, '')

        count += 1

    return encoded