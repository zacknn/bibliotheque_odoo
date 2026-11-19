{  # noqa: B018
    'name': 'Gestion Bibliothèque',
    'version': '4.0',
    'category': 'Library',
    'summary': 'Gestion d une bibliothèque (TP4)',
    'description': """
        TP4: Wizards et droits d'accès
        - Wizard Ajouter Emprunts
        - Wizard Réinitialiser Emprunts (Directeur only)
        - Groupes Directeur/Secrétaire
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/wizard_views.xml',
        'views/auteur_views.xml',
        'views/livre_views.xml',
        'views/emprunteur_views.xml',
        'views/emprunt_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}