# This file is part of the stock_move_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
__all__ = ['SaleLine']

__metaclass__ = PoolMeta


class SaleLine:
    __name__ = 'sale.line'

    def get_move(self, shipment_type):
        move = super(SaleLine, self).get_move(shipment_type)
        if not move:
            return
        move.sequence = self.sequence
        return move
