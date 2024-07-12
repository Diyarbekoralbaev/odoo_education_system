from odoo import models, fields, api


class Teacher(models.Model):
    _name = 'ems.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    course_ids = fields.Many2many('ems.course', string='Courses')

