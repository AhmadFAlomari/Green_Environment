from odoo import models, fields

class FleetVehicleModelBrand(models.Model):
    _inherit = 'fleet.vehicle.model.brand'

    charging_type = fields.Many2one(
        comodel_name='loyalty.charging.type',
        string='Charging Type'
    )
