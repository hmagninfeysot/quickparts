from odoo import api, fields, models, _

class hr_employee(models.Model):
    _inherit = 'hr.employee'

    allow_attendee = fields.Boolean(string='Saisie sur présence')