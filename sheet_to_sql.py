import gspread
from oauth2client.service_account import ServiceAccountCredentials
import mysql.connector
from datetime import datetime

# Connexion à l'API Google Sheets
scope = [
"https://spreadsheets.google.com/feeds",
"https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("etude-tdah001-0c880b1df4b4.json", scope)
client = gspread.authorize(creds)
spreadsheet = client.open("Données_TDAH")
sheet = spreadsheet.sheet1
data = sheet.get_all_records()
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Privé",
    database="tdah_Table"
)

cursor = db.cursor()

for row in data:
    def safe_int(value):
        try:
            return int(value)
        except:
            return None
        
    values=( 
        datetime.now(),
         row['Quel est votre sexe? '],
         row["quel est votre tranche d’âge "],
         row["Age au diagnostic "], row["Type de TDAH"],
        safe_int(row["Difficultés scolaire ? "]),
        safe_int(row["Difficultés Professionnel ? "]),
        row["Avez vous reçu de l’aide scolaire ? "],
        row["Avez vous déjà perdu un emploi ou démissionner à cause du TDAH"],
        safe_int(row["quel est limpact que le TDAH a  sur vous ?"]),
        safe_int(row["Avez vous souvent des conflits avec vos proches? "]),
        safe_int(row["Vous sentez vous isolé ? "]),
        safe_int(row["Avez vous du mal à vous organiser ? "]),
        safe_int(row["Avez vous du mal à gérer vos émotions ? "]),
        safe_int(row["Le TDAH impacte votre confiance en soit ? "])

        
    )
    query = """

    INSERT INTO teah_survey (

        timestamp, sexe, tranche_age, age_diagnostic, type_tdah,

        difficulte_scolaire, difficulte_professionnelle, aide_scolaire, perte_emploi,

        impact_general, conflits_proches, isolement, organisation,

        gestion_émotions, confiance_en_soi

    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, values)

# Étape 5 : Valider et fermer
db.commit()
cursor.close()
db.close()
