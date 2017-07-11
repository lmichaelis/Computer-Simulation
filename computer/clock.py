from time import sleep

from util import logger


class Clock(object):
    def __init__(self, speed: int, computer):
        self._running = True
        self._speed = speed
        self._computer = computer

    def _run(self):
        while self._running:
            self._computer.tick()
            sleep(1 / self._speed)

        logger.debug('\n--------------- Execution Finished ---------------\n')

    def start(self):
        logger.debug('\n--------------- Executing Program ---------------\n')

        self._running = True
        self._run()

    def stop(self):
        self._running = False