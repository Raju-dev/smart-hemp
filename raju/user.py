from openerp import models, fields, api

class FieldsUser(models.Model):
	_inherit = 'res.users'
	x_metrc_api_key = fields.Char('Metrc api key')