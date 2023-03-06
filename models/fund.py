# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, SUPERUSER_ID
from datetime import datetime, timedelta, date
from openerp.exceptions import UserError
from random import randint

class Period(models.Model):
    _name = "fund.period"
    _description = "Fund Period"     
    _inherit = ['mail.thread.cc', 'mail.activity.mixin', 'utm.mixin']  
    _order = 'name'      

    name = fields.Char("Name", required=True, tracking=True)     

    sequence = fields.Integer(
        "Sequence", default=10,
        help="Gives the sequence order when displaying a list of stages.")
    requirements = fields.Text("Requirements")

    is_closed = fields.Boolean('Closed')
    date_start = fields.Date(string='Start Date', required=True, tracking=True)
    date_end = fields.Date(string='End Date', required=True, tracking=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Trùng tên!"),
    ]

class Fundcategory(models.Model):
    _name = "fund.category"
    _description = "Fund category"     
    _inherit = ['mail.thread.cc', 'mail.activity.mixin', 'utm.mixin']  
    _order = 'name'      

    name = fields.Char("Name", required=True, tracking=True)     

    sequence = fields.Integer(
        "Sequence", default=10,
        help="Gives the sequence order when displaying a list of stages.")
    requirements = fields.Text("Requirements")
    
    is_closed = fields.Boolean('Closed')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Trùng tên!"),
    ]

class Fundtransactions(models.Model):
    _name = "fund.transactions"
    _description = "Fund category"     
    _inherit = ['mail.thread.cc', 'mail.activity.mixin', 'utm.mixin']  
    _order = 'date_start'      

    name = fields.Char("Name", required=True, tracking=True)     

    sequence = fields.Integer(
        "Sequence", default=10,
        help="Gives the sequence order when displaying a list of stages.")
    requirements = fields.Text("Requirements")
    
    is_closed = fields.Boolean('Closed')

    type = fields.Selection([
        ('0', 'Thu'),
        ('1', 'Chi'),
    ], tracking=True, required=True, string="Type")

    date = fields.Date(string='Date', required=True, tracking=True)
    amount = fields.Float(string='Amount', required=True, tracking=True)

    category_id = fields.Many2one('fund.category', string='Category', tracking=True, required=True)   

    period_id = fields.Many2one('fund.period', string='Period', compute='_compute_period', tracking=True, store=True)
    @api.depends('date')
    def _compute_period(self):
        for rec in self:
            period = False
            if rec.date:
                period = self.env["fund.period"].sudo().search([("date_start", "<=", rec.date),("date_end", ">=", rec.date)])
                if not period:
                    raise UserError('Kỳ đã đóng hoặc không tồn tại!')
            if period:
                rec.period_id = period.id
            else:
                rec.period_id = False

    note = fields.Char("Note", required=True, tracking=True)