from odoo import models, fields, api


class Course(models.Model):
    _name = 'ems.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price', required=True, default=0)
    duration = fields.Integer(string='Duration in days')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
    ], string='State', default='draft')

    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'
