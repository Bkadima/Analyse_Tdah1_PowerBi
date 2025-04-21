# Étude sur l’Impact Social du TDAH

Ce projet vise à analyser les impacts sociaux du TDAH à travers différentes tranches d’âge. Les données sont collectées via un Google Form, stockées dans une base MySQL à l’aide d’un script Python, puis analysées visuellement dans Power BI.

---

## Objectifs

- Étudier l’impact du TDAH sur l’organisation, la concentration, et la vie sociale
- Visualiser les tendances selon l’âge, le sexe, et le type de TDAH
- Créer un tableau de bord interactif à des fins de vulgarisation ou de recherche

---

## Étapes du projet

### 1. **Création du formulaire Google**
Un Google Form a été conçu pour récolter des données anonymes :
- Sexe, tranche d’âge, type de TDAH
- Niveau de difficulté dans différents aspects de la vie (échelle de 1 = un peu à 5 = énormément)

### 2. **Stockage dans Google Sheets**
Les réponses sont automatiquement transférées dans une feuille Google Sheets liée.

### 3. **Sauvegarde sur le cloud**
La Google Sheet est téléchargée localement au format CSV pour traitement, sous le nom :
- `Donnees_TDAH.csv`

### 4. **Insertion dans MySQL via Python**
Un script Python (`sheet_to_sql.py`) permet d’insérer automatiquement les données dans une **table MySQL déjà existante** appelée `Tdah_sql`.

> La table doit être créée manuellement au préalable à l’aide d’un script SQL adapté à la structure du CSV.
> Le script Python n’effectue pas la création de la table, il ajoute uniquement les lignes.

> Voir le fichier [`sheet_to_sql.py`](./sheet_to_sql.py) pour les détails.

### 5. **Analyse dans Power BI**
La connexion directe entre MySQL et Power BI **n’a pas abouti pour des raisons techniques encore inconnues**.
Cependant, les données ont pu être récupérées via le fichier `Donnees_TDAH.csv` et analysées dans Power BI avec succès.

Fichier Power BI utilisé :
- `TDAH Analyse.pbix`

---

## Structure du dépôt

```bash
├── Donnees_TDAH.csv # Données exportées depuis Google Sheets
├── sheet_to_sql.py # Script Python pour insertion des données dans MySQL
├── TDAH Analyse.pbix # Fichier Power BI contenant les visualisations
├── README.md # Documentation du projet