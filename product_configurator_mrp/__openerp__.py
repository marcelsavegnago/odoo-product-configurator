# -*- coding: utf-8 -*-
{
    'name': 'Product Configurator Manufacturing',
    'version': '9.0.1.0.0',
    'category': 'Manufacturing',
    'summary': 'BOM Support for configurable products',
    'author': 'Pledra',
    'license': 'AGPL-3',
    'website': 'http://www.pledra.com/',
    'depends': [
        'mrp',
        'product_configurator'
    ],
    "data": [
        'security/configurator_security.xml',
        'security/ir.model.access.csv',
        'views/product_view.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
