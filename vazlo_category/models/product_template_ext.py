# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError


class ProductTemplateExt(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one('category.product.brand', string='Marca')
    model_id = fields.Many2one('category.product.models', string='Modelo')
    cylinder_id = fields.Many2one('category.product.cylinder', string='Cilindraje')
    anio = fields.Many2one('category.product.year', string='Año')
    publications_ids = fields.One2many('publications.bl', 'product_id', string='Publicaciones', ondelete='cascade')