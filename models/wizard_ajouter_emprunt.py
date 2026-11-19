from odoo import api, fields, models


class WizardAjouterEmprunt(models.TransientModel):
    _name = 'gestion_bibliotheque.wizard_ajouter_emprunt'
    _description = 'Wizard Ajouter Emprunt'

    emprunteur_id = fields.Many2one(
        'gestion_bibliotheque.emprunteur',
        string='Emprunteur',
        required=True,
        default=lambda self: self.env.context.get('active_id')
    )
    
    date_fin = fields.Date(string='Date de fin', required=True)
    
    # Temporary lines for the wizard
    ligne_ids = fields.One2many(
        'gestion_bibliotheque.wizard_ligne',
        'wizard_id',
        string='Livres à emprunter'
    )

    def action_ajouter(self):
        """Create emprunt with lines"""
        self.ensure_one()
        
        # Create the emprunt
        emprunt = self.env['gestion_bibliotheque.emprunt'].create({
            'emprunteur_id': self.emprunteur_id.id,
            'date_fin': self.date_fin,
            'rendu': 'non',
        })
        
        # Prepare lines list for One2many
        lignes = []
        for ligne in self.ligne_ids:
            lignes.append((0, 0, {
                'livre_id': ligne.livre_id.id,
                'isbn': ligne.isbn,
                'nbre_pages': ligne.nbre_pages,
                'langue_livre': ligne.langue_livre,
            }))
        
        # Fill the One2many field
        emprunt.emprunt_ligne_ids = lignes
        
        return {'type': 'ir.actions.act_window_close'}


class WizardLigne(models.TransientModel):
    _name = 'gestion_bibliotheque.wizard_ligne'
    _description = 'Wizard Ligne'

    wizard_id = fields.Many2one(
        'gestion_bibliotheque.wizard_ajouter_emprunt',
        string='Wizard'
    )
    livre_id = fields.Many2one(
        'gestion_bibliotheque.livre',
        string='Livre',
        required=True
    )
    isbn = fields.Char(string='ISBN')
    nbre_pages = fields.Integer(string='Pages')
    langue_livre = fields.Selection([
        ('francais', 'Français'),
        ('arabe', 'Arabe'),
        ('anglais', 'Anglais')
    ], string='Langue')

    @api.onchange('livre_id')
    def _onchange_livre_id(self):
        if self.livre_id:
            self.isbn = self.livre_id.isbn
            self.nbre_pages = self.livre_id.nbre_pages
            self.langue_livre = self.livre_id.langue