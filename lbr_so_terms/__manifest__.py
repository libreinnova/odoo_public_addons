###############################################################################
#
# Copyright(c): 2022 Libreinnova (<https://libreinnova.com/>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# See LICENSE file for full copyright and licensing details.
# All Rights Reserved
#
###############################################################################
{
    'name': 'SO terms & conditions',
    'version': '13.0.1.0',
    'summary': 'Add terms and conditions to the SO PDF report',
    'description': '',
    'category': 'Sales',
    'author': 'Libreinnova',
    'website': 'https://github.com/libreinnova/odoo_public_addons',
    'license': 'AGPL-3',
    'images': [
        'static/description/banner.png',
        'static/description/icon.png'
    ],
    'depends': [
        'sale'
    ],
    'data': [
        'report/sale_order.xml',
        'templates/assets.xml',
        'views/res_company.xml'
    ],
    'installable': True,
    'application': False,
}
