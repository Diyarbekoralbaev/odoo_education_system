from datetime import timedelta
import base64

from odoo import models, fields, api


class Payment(models.Model):
    _name = 'ems.payment'
    _description = 'Payment'

    student_id = fields.Many2one('ems.student', string='Student', required=True)
    group_id = fields.Many2one('ems.group', string='Group', required=True)
    amount = fields.Float(string='Amount', required=True)
    date = fields.Date(string='Date', required=True)
    note = fields.Text(string='Note')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
    ], string='State', default='draft')
    cheque_pdf = fields.Binary(string='Cheque PDF', attachment=True)

    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    @api.model
    def get_last_week_payments(self):
        last_week = fields.Date.today() - timedelta(days=7)
        payments = self.search([('date', '>=', last_week)])
        return payments
