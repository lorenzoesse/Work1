# -*- coding: utf-8 -*-

from odoo import models, fields


class Book(models.Model):
    _name = "book"

    bookName = fields.Char(string="Book title", required=True)
    isbnCode = fields.Char(string="ISBN Code", required=True)
    publishYear = fields.Date(string="Year of publish")
    author = fields.Char(string="Author", required=True)

    loaner = fields.Many2one('res.partner',string="On loan to")

# checking that the ISBN Code is unique
    _sql_constraints = [
        ('code_unique',
         'UNIQUE(isbnCode)',
         "The ISBN code must be unique"),
    ]
