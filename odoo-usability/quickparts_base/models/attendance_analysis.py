from odoo import api, fields, models, _
from datetime import datetime

class attendance_analysis(models.Model):
    _name = "attendance_analysis"
    _description ="Analyse des absences"
 
    name = fields.Char(string='Nom', required=True)
    date = fields.Date(string='Date')
    employee_id = fields.Many2one('hr.employee', string='Employé')
    hours_attendance = fields.Float(string='Présence')
    hours_leave = fields.Float(string='Absence')
    hours_public_holiday = fields.Float(string='Jour férier')
    hours_theoretical = fields.Float(string='Théorique')
    gap = fields.Float(string='Gap')

    def action_recalculate_allocation(self):
        self.ensure_one()
        allocations = self.env['hr.leave.allocation'].search([('name_timbrage', '=', self.name)])
        allocations.write({'state': 'draft'})
        allocations.unlink()
        hours_theo = self.hours_theoretical
        nb_days = round((self.gap/hours_theo),2)
        self.env['hr.leave.allocation'].create({
            'holiday_type' : 'employee',
            'employee_id': self.employee_id.id,
            'name' : 'Allocation automatique timbrage',
            'holiday_status_id': 6,
            'allocation_type' : 'regular',
            'number_of_days': nb_days,
            'state' : 'validate',
            'name_timbrage' : self.name,
        })