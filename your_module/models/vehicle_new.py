# -*- coding: utf-8 -*-

from odoo import api, fields, models


class VehicleNew(models.Model):
    """ Create new model based from existing model """

    _name = "vehicle.new"
    _inherit = "vehicle"

    added_new_field = fields.Char()

    def added_new_method(self):
        return True
