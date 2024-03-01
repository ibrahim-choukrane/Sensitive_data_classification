import pandas as pd
import numpy as np


# Define the sensitivity rules
sensitivity_rules = {
    ('Clients', 'Nom', 'Prénom', 'Adresse', 'Code postal', 'Ville', 'Pays', 'Téléphone', 'Email', 'Date de naissance', 'Numéro de sécurité sociale'): 'Secret',
    ('Clients', 'Situation matrimoniale', 'Revenu annuel', 'ID client'): 'Confidentiel',
    ('Comptes', 'ID compte', 'ID client'): 'Secret',
    ('Comptes', 'Solde', 'Date d\'ouverture', 'Taux d\'intérêt', 'Frais mensuels'): 'Secret',
    ('Transactions', 'ID compte', 'ID transaction', 'Date', 'Montant', 'Type de transaction'): 'Secret',
    ('Prêts', 'ID prêt', 'ID client', 'Montant du prêt', 'Taux d\'intérêt', 'Durée du prêt', 'Date de début', 'Date de fin', 'Paiement mensuel'): 'Secret',
    ('Cartes bancaires', 'ID carte', 'ID client', 'Numéro de carte', 'Date d\'expiration', 'Code PIN'): 'Très Secret',
}


