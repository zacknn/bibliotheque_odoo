from odoo import fields, models


class Livre(models.Model):
    _name = 'gestion_bibliotheque.livre'
    _description = 'Livre'
    _rec_name = 'titre'

    titre = fields.Char(string='Titre', required=True)
    langue = fields.Selection([
        ('francais', 'Français'),
        ('arabe', 'Arabe'),
        ('anglais', 'Anglais')
    ], string='Langue', default='francais')
    annee = fields.Integer(string='Année de publication')
    nbre_pages = fields.Integer(string='Nombre de pages')
    isbn = fields.Char(string='ISBN')
    image_livre = fields.Binary(string='Image du livre', attachment=True)
    
    # Relation: Many Livres written by One Auteur
    auteur_id = fields.Many2one('gestion_bibliotheque.auteur', string='Auteur', required=True)
    
    # Relation: One Livre appears in Many Emprunt_Lignes 
    emprunt_ligne_ids = fields.One2many(
        'gestion_bibliotheque.emprunt_ligne',
        'livre_id',
        string='Lignes d\'emprunt'
    )