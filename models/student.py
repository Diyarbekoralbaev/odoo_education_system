from odoo import models, fields, api


class Student(models.Model):
    _name = 'ems.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    group_ids = fields.Many2many('ems.group', string='Groups')
    payment_ids = fields.One2many('ems.payment', 'student_id', string='Payments')
