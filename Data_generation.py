from faker import Faker
import random
import csv
from datetime import datetime, timedelta
import string
import pandas as pd

fake = Faker('fr_FR')

# Function to generate random date within a given range
def generate_random_date(start_date, end_date):
    return fake.date_between_dates(date_start=start_date, date_end=end_date)

# Function to generate a random social security number
def generate_social_security_number():
    return fake.ssn()

# Function to generate a random phone number
def generate_phone_number():
    return '+2126{:08d}'.format(random.randint(0, 99999999))

# Function to generate a random email address
def generate_email(first_name, last_name):
    return fake.email()

# Function to generate a random salary
def generate_salary():
    return random.randint(2500, 50000)

# Function to generate a random card number
def generate_card_number():
    return fake.credit_card_number(card_type='mastercard')

# Function to generate a random expiration date for a card
def generate_card_expiration_date():
    return fake.credit_card_expire()

# Function to generate a random PIN code for a card
def generate_pin_code():
    return fake.credit_card_security_code(card_type='mastercard')

# Function to generate a random loan amount
def generate_loan_amount():
    return random.randint(1000, 50000)

# Function to generate a random interest rate for a loan
def generate_interest_rate():
    return round(random.uniform(1, 10), 2)

# Function to generate a random loan term
def generate_loan_term():
    return random.randint(12, 60)

# Function to generate a random date within a range for loan start and end dates
def generate_loan_dates():
    start_date = fake.date_this_year()
    end_date = start_date + timedelta(days=random.randint(30, 365))
    return start_date, end_date

def generate_address(random_city, cities):
    return f"{random_city}, {random.choice(cities[random_city])}"
    

# Function to generate a random monthly payment based on loan amount, interest rate, and loan term
def calculate_monthly_payment(loan_amount, interest_rate, loan_term):
    monthly_interest_rate = interest_rate / 100 / 12
    denominator = (1 - (1 + monthly_interest_rate) ** -loan_term) / monthly_interest_rate
    monthly_payment = loan_amount / denominator
    return round(monthly_payment, 2)

# Customer names

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
    "ID_Client": [fake.uuid4() for _ in range(num_clients)],
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
    "ID_Compte": [fake.uuid4() for _ in range(num_clients)],
    "id_agence": [fake.uuid4() for _ in range(num_clients)]  

}
clients_df = pd.DataFrame(clients_data)
clients_df.to_csv("Customer.csv" , index=False)


# Generate data for the Transactions table
num_transactions = 500
transactions_data = {
    "ID_transaction": [fake.uuid4() for _ in range(num_transactions)],
    "ID_Compte": [fake.uuid4() for _ in range(num_transactions)],
    "Type": [random.choice(['Dépôt', 'Retrait']) for _ in range(num_transactions)],
    "Date_Creation": [fake.date_this_decade().strftime('%d%m%y') for _ in range(num_clients)],
    "Montant": [fake.random_number(digits=4) for _ in range(num_transactions)]
}
transactions_df = pd.DataFrame(transactions_data)

# Save Agence table to CSV file
transactions_df.to_csv("transactions.csv", index=False)


# Generate data for the Comptes table
num_comptes = 500
type_de_contrat=(
    'Compte courant', 'Compte epargne',
    'Compte cheques', 'Compte a terme',
    'Compte de depot a vue', 'Compte joint'
     )
comptes_data = {
    "ID_Compte": [fake.uuid4() for _ in range(num_comptes)],
    "ID_Client": [fake.uuid4() for _ in range(num_comptes)],
    "Type": [random.choice(type_de_contrat) for _ in range(num_comptes)],
    "Solde": [fake.random_number(digits=4) for _ in range(num_comptes)],
    "Date_Creation": [fake.date_this_decade() for _ in range(num_comptes)]
}
comptes_df = pd.DataFrame(comptes_data)

# Save Account table to CSV file
comptes_df.to_csv("Account.csv", index=False)




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
    "ID_agence": [fake.uuid4() for _ in range(num_agences)],
    "nom_agence" :[random.choice(agence_names) for _ in range(num_agences)],
    "Addresse" : [random.choice(addresse_agences) for _ in range(num_agences)],
    "Telephone": ['+2125{:08d}'.format(random.randint(0, 99999999)) for _ in range(num_agences)],
}
agences_df = pd.DataFrame(agences_data)

# Save Agence table to CSV file
agences_df.to_csv("agences.csv", index=False)


# Create Employee table
employee_data = []
for _ in range(10):
    city = random.choice(villes_keys)
    employee_data.append([
        fake.uuid4(),  # Employee ID
        random.choice(custom_Lnames),  # Last Name
        random.choice(custom_names),  # First Name
        generate_address(city,villes),  # Address
        random.randint(10000, 99000),  # Zipcode
        city,  # City
        "Morocco",  # Country
        generate_phone_number(),  # Phone Number
        generate_email(fake.first_name(), fake.last_name()),  # Email
        fake.date_of_birth(),  # Date of Birth
        generate_social_security_number(),  # Social Security Number
        fake.date_this_decade(),  # Hire Date
        fake.job(),  # Position
        generate_salary(),  # Salary
        fake.word()  # Department
    ])

# Save Employee table to CSV file
with open('employee.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["EmployeeID", "LastName", "FirstName", "Address", "Zipcode", "City", "Country", "PhoneNumber",
                     "Email", "DateOfBirth", "SocialSecurityNumber", "HireDate", "Position", "Salary", "Department"])
    writer.writerows(employee_data)

# Function to determine credit card type based on provider
def determine_card_type(provider):
    if "visa" in provider.lower():
        return "Visa"
    elif "mastercard" in provider.lower():
        return "MasterCard"
    elif "american express" in provider.lower():
        return "American Express"
    else:
        return "Other"

# Create Bank-Card table
card_data = []
for _ in range(10):
    card_provider = fake.credit_card_provider()
    card_data.append([
        fake.uuid4(),  # Card ID
        fake.uuid4(),  # Customer ID
        generate_card_number(),  # Card Number
        generate_card_expiration_date(),  # Expiration Date
        determine_card_type(card_provider),  # Card Type
        generate_pin_code()  # PIN Code
    ])

# Save Bank-Card table to CSV file
with open('bank_card.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["CardID", "CustomerID", "CardNumber", "ExpirationDate", "CardType", "PINCode"])
    writer.writerows(card_data)

loan_data = []
for _ in range(10):
    loan_amount = generate_loan_amount()
    interest_rate = generate_interest_rate()
    loan_term = generate_loan_term()
    start_date, end_date = generate_loan_dates()
    monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term)

    loan_data.append([
        fake.uuid4(),  # Loan ID
        fake.uuid4(),  # Customer ID
        loan_amount,  # Loan Amount
        interest_rate,  # Interest Rate
        loan_term,  # Loan Term
        start_date,  # Start Date
        end_date,  # End Date
        monthly_payment  # Monthly Payment
    ])

# Save LOAN table to CSV file
with open('loan.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["LoanID", "CustomerID", "LoanAmount", "InterestRate", "LoanTerm", "StartDate", "EndDate", "MonthlyPayment"])
    writer.writerows(loan_data)

