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
        x = util._fix_bin(bin(x), binlen=8)

        if len(x) > 8:
            x = x[len(x) - 8:]
            computer._carry_flag = 1
        else:
            computer._carry_flag = 0

        if x == '0000000' or x == '0000':
            computer._zero_flag = 1
        else:
            computer._zero_flag = 0

        computer._a = x
        computer._pc += 1

    def get_basename(self) -> str:
        return 'ADD'


class _SUBInstruction(_Instruction):
    def process(self, computer):
        computer._b = computer._ram.get_content(int(self._args, 2))

        x = int(computer._a, 2) - int(computer._b, 2)
        x = util._fix_bin(bin(x), binlen=8)

        if '-1' in x:
            x = '11111111'  # Set to 255
            computer._carry_flag = 1  # Set carry flag

            # We are sure and we don't want to mess up the flags
            # so we continue normally and return
            computer._a = x
            computer._pc += 1

            return

        if len(x) > 8:
            x = x[len(x) - 8:]
            computer._carry_flag = 1
        else:
            computer._carry_flag = 0

        if x == '0000000':
            computer._zero_flag = 1
        else:
            computer._zero_flag = 0

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


class _JZInstruction(_Instruction):
    def process(self, computer):
        if computer._zero_flag == 1:
            computer._pc = int(self._args, 2)
        else:
            computer._pc += 1

    def get_basename(self):
        return 'JPZ'


class _JCInstruction(_Instruction):
    def process(self, computer):
        if computer._carry_flag == 1:
            computer._pc = int(self._args, 2)
        else:
            computer._pc += 1

    def get_basename(self):
        return 'JPC'


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

    '0111': _JCInstruction,
    '1000': _JZInstruction,

    '1110': _OUTInstruction,
    '1111': _HLTInstruction
}


def get_instruction(basename: str) -> callable:
    return _INSTRUCTION_SET.get(basename)
