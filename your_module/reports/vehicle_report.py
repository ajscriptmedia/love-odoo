# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools


class ReportVehiclePDF(models.AbstractModel):
    _name = 'report.your_module.report_vehicle'
    _description = 'Vehicle Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['vehicle'].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs,
            'other_data': "Add any other data you want",
        }


class ReportVehicleView(models.Model):
    _name = 'vehicle.report'
    _description = 'Vehicle Report'
    _auto = False

    name = fields.Char()
    service_id = fields.Many2one('vehicle.services')

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute('''
            CREATE OR REPLACE VIEW %s AS (
            SELECT row_number() OVER () as id, v.name, vs.id as service_id
            FROM vehicle v LEFT JOIN vehicle_services vs on vs.vehicle_id = v.id
            )''' % (self._table,)
        )

