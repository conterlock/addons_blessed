# -*- coding: utf-8 -*-
{
    "name": "Product Category for Vazlo",
    "summary": "module for the distribution of vazlo products",
    "category": "Themes/Backend",
    "author": "Luis Millan",
    "depends": [
        "base",
        "sale",
        "product"
    ],
    "data": [
        "views/category_product_view.xml",
        "views/product_template_ext.xml",
        "views/publications_bl.xml",
        "security/ir.model.access.csv",
    ],
    "application": True,
    "installable": True,
}