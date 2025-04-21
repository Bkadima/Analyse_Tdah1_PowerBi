USE tdah_Table;
drop table if exists teah_survey;
CREATE TABLE teah_survey (
id INT AUTO_INCREMENT PRIMARY KEY,
timestamp DATETIME,
sexe VARCHAR(50),
tranche_age VARCHAR(50),
age_diagnostic VARCHAR(50),
type_tdah VARCHAR(100),
difficulte_scolaire TINYINT,
difficulte_professionnelle TINYINT,
aide_scolaire VARCHAR(50),
perte_emploi VARCHAR(50),
impact_general TINYINT,
conflits_proches TINYINT,
isolement TINYINT,
organisation TINYINT,
gestion_émotions TINYINT,
confiance_en_soi TINYINT
);

