from odoo import api, fields, models


class Auteur(models.Model):
    _name = 'gestion_bibliotheque.auteur'
    _description = 'Auteur'
    _rec_name = 'nom_complet'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    date_naissance = fields.Date(string='Date de naissance')
    nationalite = fields.Char(string='Nationalité', default='Algérienne')
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ], string='Sexe', default='homme')
    
    # Relation avec les livres (un auteur peut écrire plusieurs livres)
    livre_ids = fields.One2many('gestion_bibliotheque.livre', 'auteur_id', string='Livres')
    
    @api.depends('nom', 'prenom')
    def _compute_nom_complet(self):
        for record in self:
            record.nom_complet = f"{record.prenom} {record.nom}"
    
    nom_complet = fields.Char(string='Nom complet', compute='_compute_nom_complet', store=True)