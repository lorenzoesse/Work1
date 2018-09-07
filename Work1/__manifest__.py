# -*- coding: utf-8 -*-
{
    'name': "Work1",

    'summary': """
        Gestione libri di una libreria""",

    'description': """
        Gestione dei libri di una libreria con riferimenti a chi li prende in prestito
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
