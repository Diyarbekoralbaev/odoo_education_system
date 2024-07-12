from odoo import models, fields, api


class Group(models.Model):
    _name = 'ems.group'
    _description = 'Group'

    name = fields.Char(string='Name', required=True)
    course_id = fields.Many2one('ems.course', string='Course')
    teacher_id = fields.Many2one('ems.teacher', string='Teacher')
    student_ids = fields.Many2many('ems.student', string='Students')
    payment_ids = fields.One2many('ems.payment', 'group_id', string='Payments')
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

    def release_fees(self):
        payments = self.env['ems.payment'].search([('group_id', '=', self.id)])
        for payment in payments:
            payment.state = 'done'
