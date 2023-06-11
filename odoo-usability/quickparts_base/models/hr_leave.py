from odoo import api, fields, models, _

class hr_leave(models.Model):
    _inherit = 'hr.leave'

    date_from_only = fields.Date(string='Date from only', store=True, readonly=True, compute='_compute_date_from_only')
    date_to_only = fields.Date(string='Date to only', store=True, readonly=True, compute='_compute_date_to_only')

    @api.depends('date_from')
    def _compute_date_from_only(self):
        for record in self:
            record['date_from_only'] = record.date_from.date()

    @api.depends('date_to')
    def _compute_date_to_only(self):
        for record in self:
            record['date_to_only'] = record.date_to.date()

    