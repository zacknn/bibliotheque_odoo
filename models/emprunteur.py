from odoo import api, fields, models


class Emprunteur(models.Model):
    _name = 'gestion_bibliotheque.emprunteur'
    _description = 'Emprunteur'
    _rec_name = 'nom_complet'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    date_naissance = fields.Date(string='Date de naissance')
    nationalite = fields.Char(string='Nationalité', default='Algérienne')
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ], string='Sexe', default='homme')
    
    # TP3: Computed field for number of loans
    nbr_emprunt = fields.Integer(
        string='Nombre d\'emprunts',
        compute='_compute_nbr_emprunt',
        store=True
    )
    
    # Relation avec les emprunts
    emprunt_ids = fields.One2many('gestion_bibliotheque.emprunt', 'emprunteur_id', string='Emprunts')
    
    @api.depends('emprunt_ids')
    def _compute_nbr_emprunt(self):
        for record in self:
            record.nbr_emprunt = len(record.emprunt_ids)
    
    @api.depends('nom', 'prenom')
    def _compute_nom_complet(self):
        for record in self:
            record.nom_complet = f"{record.prenom} {record.nom}"
    
    nom_complet = fields.Char(string='Nom complet', compute='_compute_nom_complet', store=True)