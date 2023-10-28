# -*- coding: utf-8 -*-
{
    'name' : 'Your Module',
    'version' : '1.0',
    'summary': 'Your Module Summary',
    'sequence': -1,
    'description': """Your Module Description""",
    'category': 'Website',
    'depends' : ['base', 'sale', 'website'],
    'data': [
        'security/vehicle_security.xml',
        'security/ir.model.access.csv',
        'data/vehicle_data.xml',
        'views/vehicle.xml',
        'views/sale_order.xml',
        'views/snippets.xml',
        'reports/vehicle_report.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'assets': {
        'web.assets_backend': [
            'your_module/static/src/components/**/*.js',
            'your_module/static/src/components/**/*.xml',
        ],
        'web._assets_primary_variables': [
            ('prepend', 'your_module/static/src/scss/primary_variables_backend.scss'),
            'your_module/static/src/scss/primary_variables_frontend.scss'
        ],
    },
}