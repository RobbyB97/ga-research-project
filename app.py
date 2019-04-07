"""
    Author: Robby Bergers

    This is the main file for testing Genetic Algorithms.
"""

import logging
import os
from chessenv.board import Board

# Set logger
log = logging.getLogger('GA_Project')
log.setLevel(logging.INFO)
handlerpath = os.path.dirname(os.path.realpath(__file__)) + '/app.log'
handler = logging.FileHandler(handlerpath)
handler.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)s]: %(message)s')
handler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)
log.addHandler(consoleHandler)
log.addHandler(handler)
log.info('Running file ~/main/app.py:')

if __name__ == '__main__':
    x = Board()
    x.print_board()
    log.warning('ay')
