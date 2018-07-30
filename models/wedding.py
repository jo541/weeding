from odoo import models, fields, api, _


class weddingPhoto(models.Model):
    _name = "wedding.photo"

    name = fields.Char(string='Photo name')
    photo = fields.Binary(string='Photo')
    user = fields.Many2many(
        'res.users', string='People', ondelete='restrict')