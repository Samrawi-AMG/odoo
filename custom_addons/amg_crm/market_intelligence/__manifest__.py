# -*- coding: utf-8 -*-
{
    'name': "market intelligence",

    'summary': "Marketing Intelligence Module tha integrates with CRM Leads and Competitor Analysis",

    'description': """
This module integrates with CRM Leads and Competitor Analysis to provide insights into the market and identify opportunities for improvement. It provides a dashboard with key metrics such as Leads by Region, Leads by Source, Leads by Industry, Competitor Analysis, and Leads by Sales Stage. It also provides a Lead Scoring mechanism to 
prioritize leads based on their potential value to the company.
    """,

    'author': "Business Appllication Group",
    'website': "https://www.businessappligroup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/CRM',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','product','uom','competitor','mail','crm_lead_geolocation'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/market_intelligence_rule.xml',
        'views/views.xml',
        'data/sequence.xml'

    ],
    "application": False,
    "installable": True,
    "auto_install": False,
    "license": "AGPL-3"

}

