# This file is part of the stock_move_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['PurchaseLine']


class PurchaseLine:
    __metaclass__ = PoolMeta
    __name__ = 'purchase.line'

    def get_move(self, move_type):
        move = super(PurchaseLine, self).get_move(move_type)
        if not move:
            return
        move.sequence = self.sequence
        return move
