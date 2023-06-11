from odoo import api, fields, models, _

class hr_attendance(models.Model):
    _inherit = 'hr.attendance'

    date = fields.Date(string='Date', store=True, readonly=True, compute='_compute_date_attendance')

    @api.depends('check_in')
    def _compute_date_attendance(self):
        for record in self:
            record['date'] = record.check_in.date()