# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Vehicle(http.Controller):
    # @http.route('/vehicles', auth="public,user,none", type="http,json", methods=['GET','POST','DELETE'], cors="*", csrf=False, website=True)
    @http.route('/vehicles', auth="public", type="http", methods=['GET'], website=True)
    def vehicles(self):
        vehicles = request.env['vehicle'].search([])
        data = {
            "vehicles": vehicles
        }

        return request.render('your_module.vehicles', data)
