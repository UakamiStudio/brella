# -*- coding: utf-8 -*-
# Copyright 2018 Uakami - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'User Groups for Brella',
    'version': '11.0.1.0.0',
    'category': 'Sale',
    'author': 'Uakami',
    'website': "https://uakami.com/",
    'license': 'AGPL-3',
    'depends': [
        'base'
    ],
    'data': [
        'module/module_data.xml',
        'security/brella_groups.xml',
    ],
    'installable': True,
    'auto_install': False
}
