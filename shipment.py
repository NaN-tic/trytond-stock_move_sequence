# This file is part of the stock_move_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['ShipmentIn', 'ShipmentOut', 'ShipmentOutReturn']


class ShipmentIn:
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.in'

    @classmethod
    def _get_inventory_moves(cls, incoming_move):
        move = super(ShipmentIn, cls)._get_inventory_moves(incoming_move)
        if not move:
            return
        move.sequence = incoming_move.sequence
        return move

    @fields.depends('incoming_moves')
    def on_change_incoming_moves(self):
        incoming_moves = ()

        sequence = [0]
        for m in self.incoming_moves:
            if m.sequence:
                sequence.append(m.sequence)

        last_sequence = sorted(sequence, reverse=True)[0]

        for m in self.incoming_moves:
            if not m.sequence:
                last_sequence += 1
                m.sequence = last_sequence
            incoming_moves += (m,)
        self.incoming_moves = incoming_moves


class ShipmentOut:
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.out'

    def _get_inventory_move(self, move):
        inventory_move = super(ShipmentOut, self)._get_inventory_move(move)
        inventory_move.sequence = move.sequence
        return inventory_move

    @fields.depends('outgoing_moves')
    def on_change_outgoing_moves(self):
        outgoing_moves = ()

        sequence = [0]
        for m in self.outgoing_moves:
            if m.sequence:
                sequence.append(m.sequence)

        last_sequence = sorted(sequence, reverse=True)[0]

        for m in self.outgoing_moves:
            if not m.sequence:
                last_sequence += 1
                m.sequence = last_sequence
            outgoing_moves += (m,)
        self.outgoing_moves = outgoing_moves


class ShipmentOutReturn:
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.out.return'

    @classmethod
    def _get_inventory_moves(cls, incoming_move):
        move = super(ShipmentOutReturn,
            cls)._get_inventory_moves(incoming_move)
        if not move:
            return
        move.sequence = incoming_move.sequence
        return move
