# -*- coding: utf-8 -*-
{
    'name': "appbox config for mrp_workorder",

    'summary': """
        AppBox configuration for mrp_workorder.
        Provide barcode scanner support for android mobile app.
        """,

    'description': """
        Android App: https://play.google.com/store/apps/details?id=com.odooappbox
        iPhone App: https://apps.apple.com/us/app/odooappbox/id1465496744
    """,

    'author': "You Zengjian",
    'website': "https://github.com/youzengjian/OdooAppBox",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '1.0.0',

    # any module necessary for this one to work correctlyapp_action.xml
    # app_menu.xml
    'depends': ['base', 'product', 'stock', 'mrp', 'appbox', 'appbox_base', 'appbox_product', 'appbox_stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/app_view_mrp_workorder.xml',
        'data/app_action.xml',
        'data/app_menu.xml',
    ],
    'application': True,
}