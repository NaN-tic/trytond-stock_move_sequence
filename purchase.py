# This file is part of the stock_move_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
__all__ = ['PurchaseLine']

__metaclass__ = PoolMeta


class PurchaseLine:
    __name__ = 'purchase.line'

    def get_move(self):
        move = super(PurchaseLine, self).get_move()
        if not move:
            return
        move.sequence = self.sequence
        return move
