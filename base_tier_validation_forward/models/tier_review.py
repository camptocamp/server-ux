# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class TierReview(models.Model):
    _inherit = "tier.review"
    _order = "sequence"

    name = fields.Char(related="definition_id.name")
    status = fields.Selection(
        selection_add=[("forwarded", "Forwarded")],
    )
    review_type = fields.Selection(
        related="definition_id.review_type",
    )
    reviewer_id = fields.Many2one(
        comodel_name="res.users",
        related="definition_id.reviewer_id",
    )
    reviewer_group_id = fields.Many2one(
        comodel_name="res.groups",
        related="definition_id.reviewer_group_id",
    )
    sequence = fields.Integer()
    has_comment = fields.Boolean(
        related="definition_id.has_comment",
    )
    approve_sequence = fields.Boolean(
        related="definition_id.approve_sequence",
    )
