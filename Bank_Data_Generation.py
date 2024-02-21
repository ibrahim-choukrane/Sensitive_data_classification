#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install faker')


# In[31]:


import pandas as pd
import random
from faker import Faker
import string

fake = Faker('fr_FR')
custom_names = ['Tazim ','Sofian ','El Mahi ','Zubayr','Ismail','Ghaydaa','Nesma','Khadija','Farizah', 'Zhour','Ouahid','Mohammed','Abdelilah','Yassine','Mojiz','Attiq','Houssam','Hayat','Mouad','Ahmed','Imane','Hafssa','Achraf','Salah','Mohamed', 'Amir', 'Ibrahim', 'Naïm', 'Ali', 'Anas', 'Youssef', 'Younès', 'Ayoub', 'Wassim',
    'Zakaria', 'Amine', 'Hamza', 'Ismaïl', 'Ahmed', 'Nassim', 'Haroun', 'Moussa', 'Yassine','Kâmil', 'Mohammed', 'Omar', 'Qassim', 'Iyad', 'Mehdi']
custom_Lnames = ['Chafik','Lemsih','Ben Haddou','El Aoufi','Nissaboury','Laroui','Lamrani','Serghini','Kaghat','Hajuji','Laroui',
                'Allal','Lamrani','El Hachmi','Khatibi','Lahouiri','Hnika', 'Jarfi', 'Intissar','Ennasibi','El Baadioui',
                'Chahidi','Bennani','Ababou', 'Abbassi', 'Abitbol', 'Aït Merghad', 'Akhrif', 'Alami', 'Alaoui', 'Allali', 'Amrabat',
    'Ayouch', 'Azoulay', 'Belhaj', 'Belkacem', 'Ben M’Barek', 'Benhenia', 'Benjelloun', 'Benkhadra',
    'Bensaïd', 'Bensouda', 'Berrada', 'Bouab', 'Bouazza', 'Bouzaglo', 'Bouzidi', 'Chebbak', 'Cherkaoui',
    'Cherki', 'Chokri', 'Daoudi', 'Debbagh', 'Diba', 'El Azzouzi', 'El Fassi', 'El Ghazouani', 'El Khannouss',
    'Elfassi', 'Elkaïm', 'Elmaleh', 'Fassi Fihri', 'Fellous', 'Fennich', 'Hadida', 'Hamadi', 'Hariri', 'Harrak',
    'Harrouni', 'Hassani', 'Chérifs idrissides', 'Jarir', 'Kacem', 'Karchaoui', 'Kasmi', 'Kettani', 'Kharbouch',
    'Knafo', 'Lahlou', 'Laroussi', 'Lasri', 'Lasry', 'Loukili', 'Maâninou', 'Majd', 'Mansouri', 'MBarek',
    'MDaghri', 'Mimoun', 'Mimouni', 'Naciri', 'Nakache', 'Naouri', 'Ouaknin', 'Ouazzani', 'Oulad', 'Rabhi',
    'Regragui', 'Salihi', 'Salmi', 'Sbaï', 'Sbihi', 'Seghir', 'Senhaji', 'Skalli', 'Slaoui', 'Taghzout',
    'Tahiri', 'Taïeb', 'Tazi', 'Yahya', 'Zaoui', 'Zem']

quartiers_casablanca = [
    'Aïn Diab', 'Belvédère ', 'Bourgogne ', 'Californie ', 'CIL ',
    'Derb Ghallef', 'Derb Sultan', 'Gauthier ', 'Habous ', 'Hay El Hanaa', 'Hay El Hassani',
    'Hay Salama', 'Inara', 'La Colline ', 'Oasis ', 'Oulfa', 'Racine ',
    'Les Roches Noires', 'Salmia 1', 'Salmia 2', 'Sidi Maârouf'
]

quartiers_marrakech = [
    'Aïn Itti ', 'Bab oukkala ', 'Bab El Khemis ', 'Dar Tounsi ',
    'El Azzouzia ', 'Guéliz', 'Kasbah de Marrakech', "L'Hivernage", "M'hamid ",
    'Massira ', 'Médina de Marrakech', 'Quartiers nord de Marrakech', 'Semlalia ',
    'Sidi Ghanem ', 'Sidi Youssef Ben Ali', 'Socoma', 'Tamansourt', 'Targa '
]

quartiers_meknes = [
    'Bassatine', 'Hamria','Belle Vue 3', 'Californie','Sidi Bouzkri', 'Ancienne Medina'
]

quartiers_rabat = [
    'Hassan', 'Hay Ryad', 'Agdal ', 'Yacoub El Mansour ','Qamra'
]

quartiers_fes =['Essaada', 'Al azhar', 'Ennakhil', 'Lala Soukaina', 'Badr','Lido']
villes = {
    'Casablanca': quartiers_casablanca,
    'Marrakech': quartiers_marrakech,
    'Meknes': quartiers_meknes,
    'Rabat': quartiers_rabat,
    'Fés': quartiers_fes
}
villes_keys = list(villes.keys())

# Generate data for the Clients table
num_clients = 500
clients_data = {
    "ID_Client": [fake.random_number(digits=6) for _ in range(num_clients)],
    "Nom": [random.choice(custom_names) for _ in range(num_clients)],
    "Prenom": [random.choice(custom_names) for _ in range(num_clients)],
    "Genre": [random.choice(['M', 'F']) for _ in range(num_clients)],
    "Date_de_Naissance": [fake.date_of_birth() for _ in range(num_clients)],
    "Adresse": [str(random.randint(1, 100)) + ', ' + random.choice(villes_keys) + ', ' 
                 + random.choice(villes[random.choice(villes_keys)]) + ', Maroc' for _ in range(num_clients)],
    "Telephone": ['+2126{:08d}'.format(random.randint(0, 99999999)) for _ in range(num_clients)],  
    "CIN": [random.choice(string.ascii_uppercase) + str(fake.random_number(digits=6)) for _ in range(num_clients)],  # Adjusted range to num_clients
    "flag_MRE": [random.choice(['O', 'N']) for _ in range(num_clients)],
    "flag_contencieux": [random.choice(['O', 'N']) for _ in range(num_clients)],
    "ID_Compte": [fake.random_number(digits=6) for _ in range(num_clients)],
    "id_agence": [fake.random_number(digits=4) for _ in range(num_clients)]  

}
clients_df = pd.DataFrame(clients_data)

# Generate data for the Transactions table
num_transactions = 500
transactions_data = {
    "ID_transaction": [fake.random_number(digits=6) for _ in range(num_transactions)],
    "ID_Compte": [fake.random_number(digits=6) for _ in range(num_transactions)],
    "Type": [random.choice(['Dépôt', 'Retrait']) for _ in range(num_transactions)],
    "Date_Creation": [fake.date_this_decade().strftime('%d%m%y') for _ in range(num_clients)],
    "Montant": [fake.random_number(digits=4) for _ in range(num_transactions)]
}
transactions_df = pd.DataFrame(transactions_data)

# Generate data for the Comptes table
num_comptes = 500
type_de_contrat=(
    'Compte courant', 'Compte epargne',
    'Compte cheques', 'Compte a terme',
    'Compte de depot a vue', 'Compte joint'
     )
comptes_data = {
    "ID_Compte": [fake.random_number(digits=6) for _ in range(num_comptes)],
    "ID_Client": [fake.random_number(digits=6) for _ in range(num_comptes)],
    "Type": [random.choice(type_de_contrat) for _ in range(num_comptes)],
    "Solde": [fake.random_number(digits=4) for _ in range(num_comptes)],
    "Date_Creation": [fake.date_this_decade() for _ in range(num_comptes)]
}
comptes_df = pd.DataFrame(comptes_data)

num_agences=500
agence_names = ["M HAITA","OULAD TEIMA", "TATA", "TAZNAKHT","TINGHIR", "MOKHTAR SOUSSI (MRE)","HASSAN 1er",
    "ZAGORA","AZEMMOUR", "OUMI RABII","BEN AHMED","BERRECHID","TISSIR", "BIR JDID","SIDI OUASSEL","SIDI RAHAL PLAGE",
    "DEROUA","EL BROUJ","BEN AHMED", "LIGUE ARABE","SAADA","IBN KHALDOUNE", "OUALIDIA", "JAWHARA","LALLA ZAHRA",
    "MEDINA","ANNASR","ESSALAM","ESSAFAA", "NASSIM","BOUCHRIT","HAD OULAD FREJ", "HAD SOUALEM","JEMAA SHAIM",
    "KHEMIS ZEMAMRA", "OULED ABBOU","OULAD SAID","MOHAMED V","R’BAT","L.HNIA HAMRIA","LIBERTE","BIADA",
    "HASSAN II", "ZAOUIA", "MIFTAH EL KHEIR","IBN BATTOUTA","BIR ANZARANE","MOULAY DRISS 1er","SEBT GZOULA"
]
addresse_agences = [
    "M HAITA (MRE) - ROUTE DE MARRAKECH",
    "OULAD TEIMA - OULAD TEIMA CENTRE",
    "TATA - BD MOHAMMED V",
    "TAZNAKHT - CENTRE DE TAZNAKHT",
    "TINGHIR - BD.MOHAMMED V",
    "MOKHTAR SOUSSI (MRE) - AVENUE PRINCE HERITIER SIDI MED BP:44",
    "HASSAN 1er - Lotissement Essadaouia route de Tafraoute Tiznit",
    "ZAGORA - AVENUE MOHAMMED V",
    "AZEMMOUR - Bd Zerktouni Azemour",
    "OUMI RABII - Boulevard Mohamed V N° 230 Azemmour 241000",
    "BEN AHMED - BOULEVARD MOULAY ABDELLAH",
    "BERRECHID - 34.AVENUE MOHAMMED V",
    "TISSIR - Bd Hassan II lotissement Halima lot N° 1 Berrechid",
    "BIR JDID - ROUTE PRINCIPALE CENTRE BIR JDID",
    "SIDI OUASSEL - ROUTE SIDI OUASSEL AVENUE BOUJDOUR SAFI",
    "SIDI RAHAL PLAGE - Sidi Rahal, Chatii n° 31 et 32",
    "DEROUA - Lot N°2 bis lotissement Khadija",
    "EL BROUJ - BOULEVARD MOHAMMED V",
    "BEN AHMED - BOULEVARD MOULAY ABDELLAH",
    "LIGUE ARABE - 7 Avenue Mohammed VI 24000 EL JADIDA",
    "SAADA - Zankat Charif Idrissi Quartier saƒda, EL JADIDA",
    "IBN KHALDOUNE - 7 AV. HASSAN II & RUE IBN KHALD",
    "OUALIDIA - NAHJ HASSANI II, OUALIDIA",
    "JAWHARA - 7, Dachra imm. 3 route de Marrakech Provinced’El Jadida",
    "LALLA ZAHRA - Angle Avenue Echouhada et rue Churchil El Jadida",
    "MEDINA - 2, rue Ben Simon place Moulay El Hassan 24000 EL Jadida",
    "ANNASR - 64 Quartier Moulhia El Jadida 24000",
    "ESSALAM - N° 77 quartier Essalam 24000",
    "ESSAFAA - 6 BOULEVARD MOHAMED V EL JADIDA",
    "NASSIM - Bd, El Alaouiyines, 33 lot Nassim III El Jadida",
    "BOUCHRIT - ANG BD ZERKTOUNI & RUE PASTEUR 24000 EL JADIDA",
    "HAD OULAD FREJ - ROUTE SECONDAIRE N° 105 24300 H.OULED FREJ",
    "HAD SOUALEM - ROUTE EL JADIDA LOT SAHEL .LOT 209.",
    "JEMAA SHAIM - ROUTE DE CASABLANCA JEMAA SHAIM",
    "KHEMIS ZEMAMRA - ROUTE DE TNINE GHARBIA 24200 KH.ZEMAMRA",
    "OULED ABBOU - Bd. Hassan II N° 12 Ouled Abbou",
    "OULAD SAID - Lotissement El Kheir, Lot n° 36 – Oulad Said Centre – Route secondaire n°105 – Province de Settat",
    "MOHAMED V - PLACE MED V V N BP: 175",
    "R’BAT - PLACE DE L’INDEPENDANCE",
    "L.HNIA HAMRIA - BD DRISS BEN NACER",
    "LIBERTE - AVENUE DE LA LIBERTE",
    "BIADA - Rue Atlas Quartier BIADA",
    "HASSAN II - Angle Bd Kennedy et Bd Hassan II (ex Bd C) 20250 Safi",
    "ZAOUIA - Quartier sidi Ouassel, Safi 46000",
    "ZAOUIA - Quartier sidi Ouassel, Safi 46000",
    "MIFTAH EL KHEIR - Bd, Fkih Haskouri route Had Hrara Safi",
    "IBN BATTOUTA - Avenue Ibn Battouta qurtier Bled El Jed Safi",
    "BIR ANZARANE - Avenue Bir anzarane lotissement zone d’activité économique tranche 1 lot N°68 Youssou",
    "MOULAY DRISS 1er - 26, boulevard Kennedy, Safi",
    "SEBT GZOULA - ROUTE KHEMIS N’GA SEBT GZOULA"
]

agences_data ={
    "ID_agence": [fake.random_number(digits=4) for _ in range(num_agences)],
    "nom_agence" :[random.choice(agence_names) for _ in range(num_agences)],
    "Addresse" : [random.choice(addresse_agences) for _ in range(num_agences)],
    "Telephone": ['+2125{:08d}'.format(random.randint(0, 99999999)) for _ in range(num_agences)],
}
agences_df = pd.DataFrame(agences_data)


# In[32]:


clients_df


# In[33]:


transactions_df


# In[34]:


comptes_df


# In[35]:


agences_df


# In[ ]:




