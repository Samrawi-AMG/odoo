from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    latitude = fields.Float("Latitude", digits=(16, 6))
    longitude = fields.Float("Longitude", digits=(16, 6))
