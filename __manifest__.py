# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Wedding',
    'category': 'Website',
    'summary': 'r',
    'website': '',
    'version': '1.0',
    'description': """
        """,
    'depends': ['website'],
    'data': [
        'views/wedding_photo.xml',
        'views/website_templates.xml',
        'security/account_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
