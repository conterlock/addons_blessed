# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError


class CategoryProductBrand(models.Model):
    _name = 'publications.bl'

    product_id = fields.Many2one('product.template')
    portal = fields.Char('Portal')
    url = fields.Char('URL')
    price = fields.Float('Precio')
    public = fields.Boolean(string='Publicado', default=False)

    def do_public(self):
        raise UserError(('Hola!!! Este Boton está en construcción, disculpa las molestias.'))


