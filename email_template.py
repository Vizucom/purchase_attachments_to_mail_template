# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _

class email_template(osv.osv):
    
    _inherit = "email.template"

    def get_po_attachments(self, cr, uid, template_id, res_id, context=None):
        attachment_model = self.pool.get('ir.attachment')
        attachment_ids = attachment_model.search(cr, uid, [('res_model','=','purchase.order'),('res_id','=',res_id)], context=context)
        return attachment_ids

    def generate_email_batch(self, cr, uid, template_id, res_ids, context=None, fields=None):
        results = super(email_template, self).generate_email_batch(cr, uid, template_id, res_ids, context=context)
        
        for res_id in res_ids:
            template = self.get_email_template(cr, uid, template_id, res_id, context)
            if template.send_purchase_order_attachments:
                ''' Iterate all the PO's attachments, and add them to the e-mail message '''
                po_attachment_ids = self.get_po_attachments(cr, uid, template_id, res_id, context=context)
                results[res_id]['attachment_ids'].extend(po_attachment_ids)
                
        return results

    _columns = {
        'send_purchase_order_attachments': fields.boolean(_('Send Purchase Order Attachments'), help=_('In the PO e-mail composition wizard, attach also all attachments related to the PO')),      
    }
    
    _defaults = {
        'send_purchase_order_attachments': False,
    }