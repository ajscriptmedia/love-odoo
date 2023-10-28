# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Vehicle(models.Model):
    _name = 'vehicle'
    _description = "Vehicle"

    name = fields.Char()
    logo = fields.Binary()
    year_model = fields.Integer()
    date_manufactured = fields.Date()
    short_description = fields.Text()
    long_description = fields.Html()
    active = fields.Boolean(default=True)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])
    vehicle_parts = fields.Many2many("vehicle.parts")
    vehicle_services = fields.One2many("vehicle.services", "vehicle_id")

    def unlink(self):
        for record in self:
            if record.state == 'confirmed':
                raise ValidationError("You can't delete confirmed vehicles. Archive it instead.")
        super(Vehicle, self).unlink()


class VehicleServices(models.Model):
    _name = 'vehicle.services'
    _description = "Vehicle Services"

    name = fields.Char()
    vehicle_id = fields.Many2one("vehicle")

    def send_mail(self):
        self.env['mail.mail'].sudo().create({
            'email_from': self.env.user.email_formatted,
            'author_id': self.env.user.partner_id.id,
            'body_html': "body of the email",
            'subject': 'Email Subject',
            'email_to': "ajscriptmedia@gmail.com",
            'auto_delete': True,
        }).send()


class VehicleParts(models.Model):
    _name = 'vehicle.parts'
    _description = "Vehicle Parts"

    name = fields.Char()
