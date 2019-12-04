# -*- coding: utf-8 -*-
{
    'name': "appbox_task",

    'summary': """AppBox Task""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['appbox', 'appbox_base', 'project', 'appbox_timesheet'],

    # always loaded
    'data': [
        'data/app_view_res_users.xml',
        # 'data/app_view_project.xml',
        'data/app_view_project_task.xml',
        'data/app_action.xml',
        'data/app_menu.xml',
    ],
    'application': True,
}