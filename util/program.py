import util.logger as logger

from computer.instr import _INSTRUCTION_SET
from util import exception
from util.util import _fix_bin


class Program(object):
    def __init__(self, code: str):
        self._code = code
        self._bytecode = []
        self._compile()

    def _compile(self):
        lines = self._code.splitlines()
        memory_addr = 0

        logger.debug('\n--------------- Starting Compile ---------------\n')

        for line in lines:
            if self._do_compile(line):
                index = lines.index(line)
                line = line.replace(' ', '')
                addr = -1

                if '#' in line:
                    line = line[:line.index('#')]

                if ':' in line:
                    addr = int(line[:4], 2)
                    line = line[5:]

                logger.debug('Compiling line #' + str(index) + ' : ' + line + ' ...')

                try:
                    self._check_instruction(line)
                except exception.CompilerError as e:
                    raise exception.CompilerError(e.args[0], index)

                if addr is -1:
                    addr = memory_addr
                    memory_addr += 1

                self._bytecode.append(_fix_bin(bin(addr)) + line)

        logger.debug('\n--------------- Compiled Code ---------------\n\n' + '\n'.join(self._bytecode))

    @staticmethod
    def _check_instruction(line: str) -> bool:
        try:
            if len(line) is not 8:
                raise IndexError('LineError')

            if line[:4] not in _INSTRUCTION_SET:
                raise BufferError('InstructionError')

            int(line, 2)

            return True
        except ValueError:
            raise exception.CompilerError('failed to decode binary number {}'.format(line), -1)
        except IndexError:
            raise exception.CompilerError('failed to load {} - too few characters'.format(line), -1)
        except BufferError:
            raise exception.CompilerError('failed to resolve instruction {} - not available'.format(line[:4]), -1)

    @staticmethod
    def _do_compile(line: str) -> bool:
        if '1' not in line and '0' not in line or len(line) == 0:
            return False

        return True

    def get_instruction(self, line: int) -> str:
        return self._bytecode[line][4:]

    def get_memory_addr(self, line: int) -> int:
        return int(self._bytecode[line][:4], 2)

    def get_line_count(self) -> int:
        return len(self._bytecode)
