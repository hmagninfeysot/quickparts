from odoo import api, fields, models, _

class hr_employee_public(models.Model):
    _inherit = 'hr.employee.public'

    allow_attendee = fields.Boolean(string='Saisie sur présence')