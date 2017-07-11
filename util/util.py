def _fix_bin(b: str) -> str:
    b = b.replace('0b', '')

    while len(b) < 4:
        b = '0' + b

    return b