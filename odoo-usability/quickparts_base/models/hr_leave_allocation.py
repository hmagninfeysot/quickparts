from odoo import api, fields, models, _

class hr_leave_allocation(models.Model):
    _inherit = 'hr.leave.allocation'

    name_timbrage = fields.Char(string='Nom du timbrage')