# -*- coding: utf-8 -*-
{
    'name': "competitor",

    'summary': "This module allows you to create competitor tracking module",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/CRM',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/competitor_rule.xml',
        'views/views.xml',
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license":"GPL-3",

}

