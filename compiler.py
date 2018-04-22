from argparse import ArgumentParser

from util.exception import CompilerError
from util.util import _fix_bin
import util.logger as logger

_INSTRUCTION_SET = {
    'NOP' or 'nop': '0000',
    'LDA' or 'lda': '0001',
    'ADD' or 'add': '0010',
    'SUB' or 'sub': '0011',
    'STA' or 'sta': '0100',
    'LDI' or 'ldi': '0101',
    'JMP' or 'jmp': '0110',
    'OUT' or 'out': '1110',
    'HLT' or 'hlt': '1111',
    'JPC' or 'jpc': '0111',
    'JPZ' or 'jpz': '1000'
}


def compile(code) -> str:
    lines = code.splitlines()
    compiled = ''

    logger.debug('Compiling ...')

    for line in lines:
        if _do_compile(line):
            index = lines.index(line)
            line = line.replace(' ', '')
            addr = ''

            if '#' in line:
                line = line[:line.index('#')]

            try:
                _check_instruction(line)
            except CompilerError as e:
                raise CompilerError(e.args[0], index)

            if ':' in line:
                addr = line[:line.index(':')]
                line = line[line.index(':') + 1:]

            if line[:3] in _INSTRUCTION_SET:
                line = _INSTRUCTION_SET[line[:3]] + _fix_bin(bin(int(line[3:])))
            else:
                line = _fix_bin(bin(int(line)))

                while len(line) < 8:
                    line = '0' + line

            if addr is not '':
                line = _fix_bin(bin(int(addr))) + ': ' + line

            compiled += line + '\n'

    logger.debug('Done.')
    return compiled


def _do_compile(line):
    if len(line.replace(' ', '')) == 0 or line.replace(' ', '').startswith('#'):
        return False

    return True


def _check_instruction(line):
    if ':' in line:
        addr = line[:line.index(':')]
        line = line[line.index(':') + 1:]

        _check_size(addr, 15)
        _check_size(line, 255)
    else:
        _check_size(line[3:], 15)


def _check_size(addr, max):
    if int(addr) > max:
        raise CompilerError('Too big number: ' + str(addr), -1)


if __name__ == '__main__':
    parser = ArgumentParser(description='Assembly Compiler for the Ben Eater Computer Simulation')
    parser.add_argument('file', metavar='Path', type=str, help='The file to compile')
    parser.add_argument('-o', dest='output', default='', metavar='File', type=str, help='The output file. (Default: [file].bin)')
    args = parser.parse_args()

    with open(args.file, 'r') as f:
        c = compile(f.read())

    if args.output == '':
        args.output = args.file + '.bin'

    with open(args.output, 'w') as f:
        f.write(c)