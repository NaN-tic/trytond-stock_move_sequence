# This file is part of the stock_move_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import move
from . import shipment
from . import sale
from . import purchase


def register():
    Pool.register(
        move.Move,
        shipment.ShipmentIn,
        shipment.ShipmentOut,
        shipment.ShipmentOutReturn,
        module='stock_move_sequence', type_='model')
    Pool.register(
        sale.SaleLine,
        depends=['sale'],
        module='stock_move_sequence', type_='model')
    Pool.register(
        purchase.PurchaseLine,
        depends=['purchase'],
        module='stock_move_sequence', type_='model')
