from odoo import models, fields, api


class TeacherPayment(models.Model):
    _name = 'ems.teacher_payment'
    _description = 'Teacher Payment'

    teacher_id = fields.Many2one('ems.teacher', string='Teacher', required=True)
    amount = fields.Float(string='Amount', required=True)
    date = fields.Date(string='Date', required=True)
    note = fields.Text(string='Note')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
    ], string='State', default='draft')

    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'
