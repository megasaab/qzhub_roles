# -*- coding: utf-8 -*-
{
    'name': "Qzhub roles",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        create own big group with accesses
    """,

    'author': "QZHub",
    'website': "ppm.qzhub.com",

    'category': 'Security',
    'version': '0.1',


    'depends': ['base',
                'base_user_role'],


    'data': [
        'views/qzh_role_template.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
