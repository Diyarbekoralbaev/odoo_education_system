# -*- coding: utf-8 -*-
# from odoo import http


# class EducationPaymentSystem(http.Controller):
#     @http.route('/education_payment_system/education_payment_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/education_payment_system/education_payment_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('education_payment_system.listing', {
#             'root': '/education_payment_system/education_payment_system',
#             'objects': http.request.env['education_payment_system.education_payment_system'].search([]),
#         })

#     @http.route('/education_payment_system/education_payment_system/objects/<model("education_payment_system.education_payment_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('education_payment_system.object', {
#             'object': obj
#         })

