import math
from odoo import api, models,fields


class LoyaltyChargingHistories(models.Model):
    _name = 'loyalty.charging.histories'
    _description = "Loyalty Charging Histories"


    datetime = fields.Datetime(string="Charging Time", default=fields.Datetime.now)
    amount = fields.Float(string="Charging Amount")
    loyalty_car_id = fields.Many2one(comodel_name="loyalty.car",string="Car")
    company_currency = fields.Many2one("res.currency", string='Currency',compute="_compute_company_currency", compute_sudo=True)
    driver_name = fields.Char(related="loyalty_car_id.driver_name",store=True)
    driver_phone = fields.Char(related="loyalty_car_id.driver_phone",store=True)

    @api.depends('datetime')
    def _compute_company_currency(self):
        for rec in self:
            rec.company_currency = self.env.company.currency_id



