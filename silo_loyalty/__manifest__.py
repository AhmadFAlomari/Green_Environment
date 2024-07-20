# -*- coding: utf-8 -*-
{
    'name': 'SILO Loyalty',
    'version': '17.0.1.0.0 ',
    'category': 'SILO',
    'summary': 'SILO Loyalty.',
    'description': 'SILO Loyalty.',
    'author': 'Silo loya;ty',
    'company': 'Green Envireoment',
    'maintainer': 'Green Envireoment',
    'website': 'https://silo.my-env-green.com',
    'depends': ['fleet'],
    "data": [
        'security/ir.model.access.csv',
        'security/group.xml',
        'views/loyalty_car_views.xml',
        'views/loyalty_charging_type_views.xml',
        'views/fleet_vehicle_model_brand_views.xml',
        'views/loyalty_charging_history_views.xml',

    ],
    'assets': {
        'web.assets_backend': [
            'silo_loyalty/static/src/css/theme.scss',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
