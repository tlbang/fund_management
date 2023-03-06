# -*- coding:utf-8 -*-

{
    'name': 'Fund Management',
    'category': 'Services/Project',
    'version': '1.0',
    'depends': [
        'base',
        'utm',        
        'base_automation',        
    ],
    'data': [        
        'data/data.xml',
        'data/automation.xml',
        'security/fund_security.xml',
        'security/ir.model.access.csv',
        'views/fund.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
