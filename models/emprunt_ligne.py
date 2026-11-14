from odoo import api, fields, models


class EmpruntLigne(models.Model):
    _name = 'gestion_bibliotheque.emprunt_ligne'
    _description = 'Ligne d\'emprunt'
    _rec_name = 'livre_id'

    # Relation: Many lines belong to One Emprunt
    emprunt_id = fields.Many2one(
        'gestion_bibliotheque.emprunt',
        string='Emprunt',
        required=True,
        ondelete='cascade'
    )

    # Relation: Many lines reference One Livre
    livre_id = fields.Many2one(
        'gestion_bibliotheque.livre',
        string='Livre',
        required=True
    )

    # Related field: auto-show author from the selected book
    auteur_id = fields.Many2one(
        related='livre_id.auteur_id',
        string='Auteur',
        store=True
    )

    # TP3: New fields (copied from book via onchange)
    isbn = fields.Char(string='ISBN')
    nbre_pages = fields.Integer(string='Nombre de pages')
    langue_livre = fields.Selection([
        ('francais', 'Français'),
        ('arabe', 'Arabe'),
        ('anglais', 'Anglais')
    ], string='Langue')

    # TP3: Auto-update fields when livre changes
    @api.onchange('livre_id')
    def _onchange_livre_id(self):
        if self.livre_id:
            self.isbn = self.livre_id.isbn
            self.nbre_pages = self.livre_id.nbre_pages
            self.langue_livre = self.livre_id.langue