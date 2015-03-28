# This file is part of the stock_move_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .move import *
from .shipment import *
from .sale import *
from .purchase import *


def register():
    Pool.register(
        Move,
        ShipmentIn,
        ShipmentOut,
        ShipmentOutReturn,
        SaleLine,
        PurchaseLine,
        module='stock_move_sequence', type_='model')
