def _fix_bin(b: int, binlen: int = 4) -> str:
    
    if b <= -1:
        binstr = bin(b & 0b11111111)
    else:
        binstr = bin(b)
    
    binstr = binstr.replace('0b', '')

    while len(binstr) < binlen:
        binstr = '0' + binstr

    return binstr