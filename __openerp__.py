# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'PO Attachments to E-mail Templates',
    'category': 'Sales',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['purchase','email_template'],
    'description': """
PO Attachments to E-mail Templates
==================================
 * Extends e-mail templates to enable adding purchase order's attachments automatically to e-mails

Usage
-----
 * Edit the Purchase Order e-mail template and check the box "Send also Purchase Order Attachments"
   
 """,
    'data': [
        'view/email_template.xml',
    ],
}
