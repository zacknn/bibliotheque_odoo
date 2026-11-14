from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Emprunt(models.Model):
    _name = 'gestion_bibliotheque.emprunt'
    _description = 'Emprunt'

    # TP3: Default today, readonly
    date_debut = fields.Date(
        string='Date de début', 
        required=True, 
        default=fields.Date.today,
        readonly=True
    )
    date_fin = fields.Date(string='Date de fin')
    rendu = fields.Selection([
        ('oui', 'Oui'),
        ('non', 'Non')
    ], string='Rendu', default='non')
    
    # Relation: Many Emprunts made by One Emprunteur
    emprunteur_id = fields.Many2one('gestion_bibliotheque.emprunteur', string='Emprunteur', required=True)
    
    # Relation: One Emprunt has Many Lignes
    emprunt_ligne_ids = fields.One2many(
        'gestion_bibliotheque.emprunt_ligne',
        'emprunt_id',
        string='Livres empruntés'
    )

    # TP3: Constraint - date_debut must be today
    @api.constrains('date_debut')
    def _check_date_debut(self):
        for record in self:
            if record.date_debut and record.date_debut != fields.Date.today():
                raise ValidationError("La date de début doit être la date du jour!")

    # TP3: Auto-set rendu to 'oui' when date_fin is today
    @api.onchange('date_fin')
    def _onchange_date_fin(self):
        if self.date_fin and self.date_fin == fields.Date.today():
            self.rendu = 'oui'