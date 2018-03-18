# -*- coding: utf-8 -*-
# Copyright 2018 Uakami - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Brella',
    'version': '11.0.0.1.0',
    'category': 'Sale',
    'author': 'Uakami',
    'website': "https://uakami.com/",
    'license': 'AGPL-3',
    'depends': [
        'brella_groups',
        'brella_sale',
        'studio_customization',
        'sale_total_discount',
        'sale_show_total_discount',
        'website_link_tracker_lead',
        'crm_sync_participants_marketing_automation',
    ],
    'data': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
