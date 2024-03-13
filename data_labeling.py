import pandas as pd
import numpy as np
import sys
import os


# Define the sensitivity rules
sensitivity_rules = {
    'Customer': {'CIN': 'Secret', 'Nom' : 'Secret', 'Prenom': 'Secret', 'Genre': 'Secret', 'Adresse': 'Secret', 'Code postal': 'Secret', 'Ville': 'Secret', 'Pays': 'Secret', 'Téléphone': 'Secret', 'Email': 'Secret', 'Date_de_Naissance': 'Secret', 'Numéro de sécurité sociale': 'Secret' , 'Telephone': 'Secret', 'Situation matrimoniale' : 'Confidentiel', 'Revenu annuel' : 'Confidentiel', 'ID_Client' : 'Confidentiel', 'flag_MRE': 'Confidentiel', 'flag_contencieux': 'Confidentiel', 'ID_Compte':'Confidentiel', 'id_agence':'Confidentiel'},
    'employe': {'CIN': 'Secret','Nom' : 'Secret', 'Prenom': 'Secret', 'Genre': 'Secret','Adresse': 'Secret', 'Zipcode': 'Secret', 'Ville': 'Secret', 'Pays': 'Secret', 'Numero_tele': 'Secret', 'Email': 'Secret', 'Date_naissance': 'Secret', 'Date_recrutement': 'Secret', 'NumeroSecuriteSocial': 'Secret', 'Telephone': 'Secret', 'Situation matrimoniale' : 'Confidentiel', 'Revenu annuel' : 'Confidentiel', 'EmployeeID' : 'Confidentiel','Poste': 'Confidentiel', 'Salaire': 'Confidentiel','Departement': 'Confidentiel'},
    'Account' : {'ID_Compte': 'Confidentiel', 'ID_Client' : 'Confidentiel', 'Type': 'Secret', 'Solde': 'Secret', 'Date_Creation': 'Secret', 'Taux_Interet': 'Secret', 'Frais_Mensuels': 'Secret'},
    'transactions' : {'ID_Compte' : 'Secret', 'ID_transaction' : 'Secret', 'Date' : 'Secret', 'Montant' : 'Secret', 'Type' : 'Secret', 'Date_Creation': 'Secret'},
    'loan' : {'ID_Prêt': 'Secret', 'ID_Client': 'Secret', 'Montant_Pret': 'Secret', 'Taux_Interet': 'Secret', 'Duree_Pret': 'Secret', 'Date_Debut': 'Secret', 'Date_Fin': 'Secret', 'Paiement_Mensuel': 'Secret'},
    'agences' : {'ID_agence': 'Restreint', "nom_agence": 'Restreint', "Addresse": 'Restreint' , "Telephone": 'Restreint'},
    'bank_card' : {'ID_Carte': 'Très Secret', 'ID_Client': 'Très Secret', 'Numero_carte': 'Très Secret', 'Date_expiration': 'Très Secret', 'Code_PIN': 'Très Secret', 'Type_carte': "Secret"},
'produit_data': {"ID_Produit": 'Restreint', "Type_Produit": 'Restreint', "Caract_Produit": 'Restreint', "Conditions_utilisation": 'Restreint'},
    'Taux_Interets_data': {"ID_Taux": 'Restreint', "Type_Produit": 'Restreint', "Taux_Interet": 'Restreint'},
    'annonces_data': {"ID_Annonce": 'Restreint', "Title": 'Restreint', "Date": 'Restreint', "Description": 'Restreint'},
    'education_data': {"ID_Ressource": 'Restreint', "Title": 'Restreint', "Description": 'Restreint', "URL_or_reference": 'Restreint'},
    'community_engagement_data': {"ID_Evenement": 'Restreint', "Nom_Evenement": 'Restreint', "Date": 'Restreint', "Lieu": 'Restreint', "Description": 'Restreint'},
    'faqs_data': {"ID_Question": 'Restreint', "Question": 'Restreint', "Reponse": 'Restreint'},
    'contact_info_data': {"ID_Contact": 'Restreint', "Type_Contact": 'Restreint', "Coordonnees_Contact": 'Restreint'},
    'surveys_data': {'ID_Enquete': 'Restreint', "Titre_Enquete": 'Restreint', "Questions": 'Restreint'},
    'atm_data': {'ATM_ID': 'Restreint', "Localisation": 'Restreint', "Informations": 'Restreint'},
}

if ( len(sys.argv) == 2 ) and ( os.path.splitext(sys.argv[1])[1] == '.csv'):
    
    embeddings = pd.read_csv(sys.argv[1])
    
    embeddings.index = pd.MultiIndex.from_frame(embeddings.loc[:,["Unnamed: 0","Unnamed: 1"]],names= ("Table", "Column"))
    embeddings.drop(["Unnamed: 0","Unnamed: 1"], axis=1, inplace=True)
    
    labels = [sensitivity_rules[table][column] for table, column in embeddings.index]
    
    serie_labels = pd.Series(labels)
    
    embeddings['sensitivity'] = serie_labels.to_numpy()
        
    embeddings.to_csv(f"labeled_{os.path.splitext(sys.argv[1])[0]}.csv")

else:
    print("Please provide appropriate parameters")