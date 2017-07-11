import util.util as util


class _Instruction(object):
    def __init__(self, args: str):
        self._args = args

    def process(self, computer):
        pass

    def get_basename(self) -> str:
        return ''


class _NOPInstruction(_Instruction):
    def process(self, computer):
        computer._pc += 1

    def get_basename(self) -> str:
        return 'NOP'


class _LDAInstruction(_Instruction):
    def process(self, computer):
        computer._a = computer._ram.get_content(int(self._args, 2))
        computer._pc += 1

    def get_basename(self) -> str:
        return 'LDA'


class _ADDInstruction(_Instruction):
    def process(self, computer):
        computer._b = computer._ram.get_content(int(self._args, 2))

        x = int(computer._a, 2) + int(computer._b, 2)
        x = util._fix_bin(bin(x))

        if len(x) > 8:
            x = x[len(x) - 8:]

        computer._a = x
        computer._pc += 1

    def get_basename(self) -> str:
        return 'ADD'


class _SUBInstruction(_Instruction):
    def process(self, computer):
        computer._b = computer._ram.get_content(int(self._args, 2))

        x = int(computer._a, 2) - int(computer._b, 2)
        x = util._fix_bin(bin(x))

        if len(x) > 8:
            x = x[len(x) - 8:]

        computer._a = x
        computer._pc += 1

    def get_basename(self) -> str:
        return 'SUB'


class _STAInstruction(_Instruction):
    def process(self, computer):
        computer._ram.write(int(self._args, 2), computer._a)
        computer._pc += 1

    def get_basename(self) -> str:
        return 'STA'

class _LDIInstruction(_Instruction):
    def process(self, computer):
        computer._a = self._args
        computer._pc += 1

    def get_basename(self) -> str:
        return 'LDI'

class _JMPInstruction(_Instruction):
    def process(self, computer):
        computer._pc = int(self._args, 2)

    def get_basename(self) -> str:
        return 'NOP'

class _OUTInstruction(_Instruction):
    def process(self, computer):
        print('[OUT] ' + computer._a)
        computer._pc += 1

    def get_basename(self) -> str:
        return 'OUT'


class _HLTInstruction(_Instruction):
    def process(self, computer):
        computer.get_clock().stop()
        computer._pc += 1

    def get_basename(self) -> str:
        return 'HLT'


_INSTRUCTION_SET = {
    '0000': _NOPInstruction,
    '0001': _LDAInstruction,
    '0010': _ADDInstruction,
    '0011': _SUBInstruction,
    '0100': _STAInstruction,
    '0101': _LDIInstruction,
    '0110': _JMPInstruction,
    '1110': _OUTInstruction,
    '1111': _HLTInstruction
}


def get_instruction(basename: str) -> callable:
    return _INSTRUCTION_SET.get(basename)