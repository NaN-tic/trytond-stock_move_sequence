# This file is part of the stock_move_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields, sequence_ordered
from trytond.pool import PoolMeta

__all__ = ['Move']


class Move(sequence_ordered()):
    __metaclass__ = PoolMeta
    __name__ = 'stock.move'

    @classmethod
    def __setup__(cls):
        super(Move, cls).__setup__()
        cls._order.insert(0, ('sequence', 'ASC'))

    @classmethod
    def create(cls, vlist):
        sequence = 0
        vlist = [x.copy() for x in vlist]
        for values in vlist:
            if not values.get('sequence'):
                sequence += 1
                values['sequence'] = sequence
        return super(Move, cls).create(vlist)
