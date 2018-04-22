def _fix_bin(b: str, binlen: int = 4) -> str:
    b = b.replace('0b', '')

    while len(b) < binlen:
        b = '0' + b

    return b