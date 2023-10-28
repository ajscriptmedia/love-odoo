# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model_create_multi
    def create(self, vals):
        res = super().create(vals)
        # inherit res values before saving to database
        return res

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        # inherit res values before saving to database
        return res

    def unlink(self):
        res = super(SaleOrder, self).unlink()
        # check some condition before deleting the record
        return res

    def my_query(self):
        products = self.env['sale.order'].search([('id', '=', 7)]).order_line.filtered(lambda p:p.product_id.categ_id.id == 8).mapped('product_id').sorted(lambda p: p.name).mapped('name')

        print("products ==>", products)

    total_amount = fields.Float(compute="_compute_total_amount")

    @api.depends('order_line.product_id.list_price')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(order.order_line.mapped('price_subtotal'))
