from util import logger
from util.util import _fix_bin
from util.program import Program


class RAM(object):
    def __init__(self, size: int):
        self._content = []

        for i in range(size):
            self._content.append('')

    def load_program(self, prg: Program):
        logger.debug('\n------------- Initial RAM Loading -------------\n')

        for i in range(prg.get_line_count()):
            addr = prg.get_memory_addr(i)
            instr = prg.get_instruction(i)

            logger.debug('Loading instruction to memory address ' + _fix_bin(bin(addr)) + ' : ' + instr + '  ...')

            self._content[addr] = instr

    def get_content(self, content: int):
        p = self._content[content]
        return p

    def write(self, addr: int, content: str):
        self._content[addr] = content

    def get_size(self) -> int:
        return len(self._content) * 16
