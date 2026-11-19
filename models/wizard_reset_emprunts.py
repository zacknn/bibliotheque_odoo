from odoo import fields, models


class WizardResetEmprunts(models.TransientModel):
    _name = 'gestion_bibliotheque.wizard_reset_emprunts'
    _description = 'Wizard Reset Emprunts'

    emprunteur_id = fields.Many2one(
        'gestion_bibliotheque.emprunteur',
        string='Emprunteur',
        required=True,
        default=lambda self: self.env.context.get('active_id')
    )

    def action_reset(self):
        """Delete all emprunts of this borrower"""
        self.ensure_one()
        
        # Find all emprunts of this borrower
        emprunts = self.env['gestion_bibliotheque.emprunt'].search([
            ('emprunteur_id', '=', self.emprunteur_id.id)
        ])
        
        # Delete them all
        emprunts.unlink()
        
        return {'type': 'ir.actions.act_window_close'}