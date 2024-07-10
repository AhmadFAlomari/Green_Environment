import math
from odoo import api, models,fields


class LoyaltyCar(models.Model):
    _name = 'loyalty.car'
    _description = "Loyalty Car"
    _rec_name = "number"

    number = fields.Char(string="Number")
    driver_name = fields.Char(string="Driver Name")
    driver_phone = fields.Char(string="Driver Phone")
    charging_history = fields.One2many(comodel_name="loyalty.charging.histories",inverse_name="loyalty_car_id",string="Charging Histories")
    manufacturers_id = fields.Many2one(comodel_name="fleet.vehicle.model.brand",string="Manufacturers")
    model_id = fields.Many2one(comodel_name="fleet.vehicle.model",string="Model")
    image_128 = fields.Image(related='manufacturers_id.image_128', readonly=True)
    charging_type = fields.Many2one(comodel_name="loyalty.charging.type",string="Charging Type")


    @api.onchange('manufacturers_id')
    def _onchange_manufacturers_id(self):
        for rec in self:
            if not rec.charging_type and rec.manufacturers_id and rec.manufacturers_id.charging_type:
                rec.charging_type = rec.manufacturers_id.charging_type

