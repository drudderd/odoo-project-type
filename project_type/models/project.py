# -*- coding: utf-8 -*-
# By DDR

from odoo import api, models, fields

class Project(models.Model):
	_inherit = "project.project"

	project_type = fields.Selection([
        ('internal', 'Company internal'),
		('sales', 'Sales project'),
        ('customer', 'Customer project'),
    ])
