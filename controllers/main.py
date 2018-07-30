import werkzeug

from odoo import fields, http, _
from odoo.http import request
from odoo.addons.website_mail.controllers.main import _message_post_helper


class WeddingHttp(http.Controller):

    @http.route("/photos", type='http', auth="public", website=True)
    def index(self, *args, **kwargs):
        photos = request.env['wedding.photo'].search([])
        return request.render('wedding.photos', {'photos': photos})