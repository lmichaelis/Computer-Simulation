from argparse import ArgumentParser

import util.logger as logger
from computer.computer import Computer
from util.program import Program

ARCHITECTURE = 8
RAM_SIZE = 16
CLOCK_SPEED = 10


def main():
    #    prg = compiler.compile("""LDA 14
    # ADD 15
    # OUT 0
    # HLT 0
    #
    # 14: 5
    # 15: 10
    # """)

    # prg = '0001 1110\n' \
    #      '0010 1111 # Test comment\n' \
    #      '1110 0000\n' \
    #      '1111 0000\n' \
    #      '\n' \
    #      '1110: 00001010\n' \
    #      '1111: 00000101'

    parser = ArgumentParser(description='Computer Simulation of Ben Eater\'s breadboard computer.')
    parser.add_argument('file', metavar='File', type=str, help='The file to run the simulation with.')
    parser.add_argument('--clock-speed', dest='clock_speed', default=10, type=int, metavar='Speed',
                        help='Set the clock speed of the CPU')
    parser.add_argument('--ram-size', dest='ram_size', default=16, metavar='Size', type=int,
                        help='The size of the RAM \'slots\' (writable memory adresses)')
    args = parser.parse_args()

    with open(args.file, 'r') as f:
        prg = f.read()

    logger.debug('\n--------------- Loading Program ---------------\n')
    logger.debug('\n'.join(prg.splitlines()))

    prg = Program(prg)

    # Computer Setup

    computer = Computer(ARCHITECTURE, args.ram_size, args.clock_speed)
    computer.get_ram().load_program(prg)  # Load Program into RAM
    computer.get_clock().start()  # Start clock


if __name__ == '__main__':
    main()
