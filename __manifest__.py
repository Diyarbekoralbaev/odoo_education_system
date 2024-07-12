# -*- coding: utf-8 -*-
{
    'name': "education_payment_system",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """Module for managing courses, teachers, students, groups, and payments in educational centers.""",

    'author': "Diyarbek Oralbaev",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/teacher_views.xml',
        'views/student_views.xml',
        'views/group_views.xml',
        'views/payment_views.xml',
        'views/teacher_payment_views.xml',
        'reports/course_report.xml',
        'reports/payment_report.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
