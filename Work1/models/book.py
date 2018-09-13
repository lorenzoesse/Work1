# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Book(models.Model):
    _name = "book"


    bookName = fields.Char(string="Book title", required=True)
    isbnCode = fields.Char(string="ISBN Code", required=True)
    publishYear = fields.Date(string="Year of publish")
    author = fields.Char(string="Author", required=True)

    loaner = fields.Many2one('res.partner', string="On loan to")

# checking that the ISBN Code is unique
#    _sql_constrains = [
#        ('code_unique',
#         'UNIQUE(isbnCode)',
#         "The ISBN code must be unique"),
#    ]

    @api.constrains('isbnCode')
    def check_isbn_unique(self):
        for record in self:
            same_isbn_code = self.search([('isbnCode', '=', record.isbnCode)])
            if len(same_isbn_code) > 1:
                raise ValidationError('ISBN Code should be unique')
        return True
