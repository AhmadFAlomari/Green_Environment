import math
from odoo import api, models,fields


class LoyaltyChargingType(models.Model):
    _name = 'loyalty.charging.type'
    _description = "Loyalty Charging Type"

    name = fields.Char(string="Charging Type")