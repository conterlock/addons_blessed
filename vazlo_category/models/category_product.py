# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError


class CategoryProductBrand(models.Model):
    _name = 'category.product.brand'

    name = fields.Char('Nombre')
    code = fields.Char('Código')
    models_ids = fields.One2many('category.product.models', 'brand_base_id', string='modelos', ondelete='cascade')

class CategoryProductModel(models.Model):
    _name = 'category.product.models'

    name = fields.Char('Nombre')
    code = fields.Char('Código')
    brand_base_id = fields.Many2one('category.product.brand')
    # cylinder_id = fields.One2many('category.product.cylinder', 'model_base_id', string='Cilindraje', ondelete='cascade')

class CategoryProductYear(models.Model):
    _name = 'category.product.year'

    name = fields.Char('Nombre')
    code = fields.Char('Código')

class CategoryProductCylinder(models.Model):
    _name = 'category.product.cylinder'

    name = fields.Char('Nombre')
    code = fields.Char('Código')
    year_base_id = fields.Many2one('category.product.year')
    # model_base_id = fields.Many2one('category.product.models')
    # brand_base_id = fields.Many2one('category.product.brand')
