'''
a massive multiplayer tictactoe server

This is WIP, no quite working yet...
'''

import logging
from tornado import gen
from webalchemy import server

from board import Board

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class TickTackToeApp:
    @gen.coroutine
    def initialize(self, **kwargs):
        # remember these for later use
        self.rdoc = kwargs['remote_document']
        log.info('New session opened, id={}'.format(kwargs['session_id']))

        self.board = Board(self.rdoc, 13, 500.0)
        self.rdoc.body.append(self.board.svg)

if __name__ == "__main__":
	from tictactoe_example import TickTackToeApp
	server.run(TickTackToeApp)