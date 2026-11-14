{  # noqa: B018
    'name': 'Gestion Bibliothèque',
    'version': '3.0',
    'category': 'Library',
    'summary': 'Gestion d une bibliothèque (TP3)',
    'description': """
        TP3: Champs calculés, contraintes et onchange
        - editable="top" sur One2many
        - Champs isbn, nbre_pages, langue dans emprunt_ligne
        - Mise à jour automatique via onchange
        - nbr_emprunt calculé
        - Contraintes sur date_debut
        - Auto-update rendu quand date_fin = aujourd'hui
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/auteur_views.xml',
        'views/livre_views.xml',
        'views/emprunteur_views.xml',
        'views/emprunt_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}