import logging

from computer.clock import Clock
from computer.instr import get_instruction
from computer.ram import RAM

class Computer(object):
    def __init__(self, arch: int, ram_size: int, clock_speed: int):
        self._ram = RAM(ram_size)
        self._clock = Clock(clock_speed, self)
        self._pc = 0
        self._a = '00000000'
        self._b = '00000000'
        self._carry_flag = 0
        self._zero_flag = 0

        logging.debug('\n--------------- System Information ---------------\n')
        logging.debug('RAM Size : ' + str(self._ram.get_size()) + ' bit')
        logging.debug('CPU Clock Speed : ' + str(clock_speed) + ' Hz')
        logging.debug('CPU Arch : ' + str(arch) + ' bit')

    def get_ram(self) -> RAM:
        return self._ram

    def get_clock(self) -> Clock:
        return self._clock

    def tick(self):
        instr = self._ram.get_content(self._pc)
        instruction = get_instruction(instr[:4])(instr[4:])

        logging.debug('[CPU] Running instruction #' + str(self._pc) + ' : [' + instruction.get_basename() + '] ' + instr[:4] + ' using parameter ' + instr[4:])

        instruction.process(self)
