CREATE TABLE IF NOT EXISTS Claim_File_Details
(
    File_Name VARCHAR ( 100 ) PRIMARY KEY,
    Claim_Type VARCHAR ( 100 ),
    Sender_ID VARCHAR ( 100 ),
    Receiver_ID VARCHAR ( 100 ),
    Submission_Date TIMESTAMP,
    Disposition_Flag VARCHAR ( 50 ),
    Claim_IDs VARCHAR ( 2000 ),
    Record_Count INTEGER
);
commit;

CREATE TABLE IF NOT EXISTS Claim_Master (
	Claim_ID  VARCHAR ( 250 ) PRIMARY KEY,
	Sender_ID VARCHAR ( 250 )  NOT NULL,
	Receiver_ID VARCHAR ( 250 ) NOT NULL,
	Submission_Date TIMESTAMP NOT NULL,
	ID_Payer VARCHAR ( 250 ),
	Member_ID VARCHAR ( 250 ) NOT NULL,
	Payer_ID VARCHAR ( 250 ) NOT NULL,
	Provider_ID VARCHAR ( 250 ) NOT NULL,
	Emirates_IDNumber VARCHAR ( 250 ) NOT NULL,
	Gross NUMERIC(7,2) NOT NULL,
	PatientShare VARCHAR ( 250 ) NOT NULL,
	Net NUMERIC(7,2) NOT NULL,
	VAT NUMERIC(7,2) NOT NULL,
	Enc_Facility_ID VARCHAR ( 250 ) NOT NULL,
	Enc_Type VARCHAR ( 250 ) NOT NULL,
	Enc_Patient_ID VARCHAR ( 250 ) NOT NULL,
	Enc_Start_Time TIMESTAMP NOT NULL,
	Enc_End_Time TIMESTAMP NOT NULL,
	Enc_Start_Type VARCHAR ( 250 ) NOT NULL,
	Enc_End_Type VARCHAR ( 250 ) NOT NULL
);
commit;

CREATE TABLE IF NOT EXISTS Claim_Diagnosis (
	Diagnosis_ID  SERIAL PRIMARY KEY,
	Claim_ID VARCHAR ( 250 ) REFERENCES Claim_Master(Claim_ID),
	Diagnosis_Type VARCHAR ( 250 ) NOT NULL,
	Diagnosis_Code VARCHAR ( 250 ) NOT NULL
);
commit;

CREATE TABLE IF NOT EXISTS Claim_Activity (
	Activity_ID  VARCHAR ( 250 ) PRIMARY KEY,
	Claim_ID VARCHAR ( 250 ) REFERENCES Claim_Master(Claim_ID),
	Act_Start_Time TIMESTAMP NOT NULL,
	Act_Type VARCHAR ( 250 ) NOT NULL,
	Act_Code VARCHAR ( 250 ) NOT NULL,
	Act_Net VARCHAR ( 250 ) NOT NULL,
	Act_Quantity VARCHAR ( 250 ) NOT NULL,
	Ordering_Clinician VARCHAR ( 250 ) NOT NULL,
	Clinician VARCHAR ( 250 ) NOT NULL,
	PriorAuthorization_ID VARCHAR ( 250 ),
	VAT NUMERIC(7,2) NOT NULL,
	VAT_Percent NUMERIC(7,2) NOT NULL
);
commit;

CREATE TABLE IF NOT EXISTS Claim_Act_Observation (
    Observation_ID SERIAL PRIMARY KEY,
	Activity_ID  VARCHAR ( 250 ) REFERENCES Claim_Activity(Activity_ID),
	Claim_ID VARCHAR ( 250 ) REFERENCES Claim_Master(Claim_ID),
	Obs_Type VARCHAR ( 250 ),
	Obs_Code VARCHAR ( 250 ),
	Obs_Value VARCHAR ( 250 ),
	Obs_ValueType VARCHAR ( 250 )
);
commit;

CREATE TABLE IF NOT EXISTS Remittance_Master (
	Remittance_ID  SERIAL PRIMARY KEY,
	Claim_ID VARCHAR ( 250 ), -- REFERENCES Claim_Master(Claim_ID),
	Sender_ID VARCHAR ( 250 ) NOT NULL,
	Receiver_ID VARCHAR ( 250 ) NOT NULL,
	Submission_Date VARCHAR ( 250 ) NOT NULL,
	ID_Payer VARCHAR ( 250 ) NOT NULL,
	Provider_ID VARCHAR ( 250 ) NOT NULL,
	Payment_Reference VARCHAR ( 250 ) NOT NULL,
	Date_Settlement VARCHAR ( 250 ) NOT NULL,
	Enc_Facility_ID VARCHAR ( 250 ) NOT NULL
);
commit;

CREATE TABLE IF NOT EXISTS Remittance_Activity (
    Remit_Act_ID SERIAL PRIMARY KEY,
	Activity_ID VARCHAR ( 250 ), -- REFERENCES Claim_Activity(Activity_ID),
    Claim_ID VARCHAR ( 250 ), -- REFERENCES Claim_Master(Claim_ID),
	Act_StartTime TIMESTAMP NOT NULL,
	Act_Type VARCHAR ( 250 ) NOT NULL,
	Act_Code VARCHAR ( 250 ) NOT NULL,
	Act_Quantity VARCHAR ( 250 ) NOT NULL,
	Act_Net VARCHAR ( 250 ) NOT NULL,
	Ordering_Clinician VARCHAR ( 250 ) NOT NULL,
	Clinician VARCHAR ( 250 ) NOT NULL,
	Payment_Amount NUMERIC(7,2) NOT NULL,
    Denial_Code VARCHAR ( 250 )
);
commit;

CREATE TABLE IF NOT EXISTS Resub_Master (
    Resub_Claim SERIAL PRIMARY KEY,
	Claim_ID VARCHAR ( 250 ), -- REFERENCES Claim_Master(Claim_ID),
	Sender_ID VARCHAR ( 250 )  NOT NULL,
	Receiver_ID VARCHAR ( 250 ) NOT NULL,
	Submission_Date TIMESTAMP NOT NULL,
	ID_Payer VARCHAR ( 250 ),
	Member_ID VARCHAR ( 250 ) NOT NULL,
	Payer_ID VARCHAR ( 250 ) NOT NULL,
	Provider_ID VARCHAR ( 250 ) NOT NULL,
	Emirates_IDNumber VARCHAR ( 250 ) NOT NULL,
	Gross NUMERIC(7,2) NOT NULL,
	PatientShare VARCHAR ( 250 ) NOT NULL,
	Net NUMERIC(7,2) NOT NULL,
	VAT NUMERIC(7,2) NOT NULL,
	Enc_Facility_ID VARCHAR ( 250 ) NOT NULL,
	Enc_Type VARCHAR ( 250 ) NOT NULL,
	Enc_Patient_ID VARCHAR ( 250 ) NOT NULL,
	Enc_Start_Time TIMESTAMP NOT NULL,
	Enc_End_Time TIMESTAMP NOT NULL,
	Enc_Start_Type VARCHAR ( 250 ) NOT NULL,
	Enc_End_Type VARCHAR ( 250 ) NOT NULL,
    Resub_Type VARCHAR ( 250 ) NOT NULL,
    Resub_Comment VARCHAR ( 2000 ),
    Resub_Attachment BYTEA
);
commit;

CREATE TABLE IF NOT EXISTS Resub_Diagnosis
(
    Diagnosis_ID VARCHAR ( 250 ),
    Claim_ID VARCHAR ( 250 ), -- REFERENCES Claim_Master(Claim_ID),
    Diagnosis_Type VARCHAR ( 250 ) NOT NULL,
    Diagnosis_Code VARCHAR ( 250 ) NOT NULL
);
commit;

CREATE TABLE IF NOT EXISTS Resub_Activity (
	Activity_ID  VARCHAR ( 250 ),
	Claim_ID VARCHAR ( 250 ), -- REFERENCES Claim_Master(Claim_ID),
	Act_Start_Time TIMESTAMP NOT NULL,
	Act_Type VARCHAR ( 250 ) NOT NULL,
	Act_Code VARCHAR ( 250 ) NOT NULL,
	Act_Net VARCHAR ( 250 ) NOT NULL,
	Act_Quantity VARCHAR ( 250 ) NOT NULL,
	Ordering_Clinician VARCHAR ( 250 ) NOT NULL,
	Clinician VARCHAR ( 250 ) NOT NULL,
	PriorAuthorization_ID VARCHAR ( 250 ),
	VAT NUMERIC(7,2),
	VAT_Percent NUMERIC(7,2)
);
commit;

CREATE TABLE IF NOT EXISTS Resub_Act_Observation (
	Activity_ID  VARCHAR ( 250 ),-- REFERENCES Claim_Activity(Activity_ID),
	Claim_ID VARCHAR ( 250 ), -- REFERENCES Claim_Master(Claim_ID),
	Obs_Type VARCHAR ( 250 ),
	Obs_Code VARCHAR ( 250 ),
	Obs_Value VARCHAR ( 250 ),
	Obs_ValueType VARCHAR ( 250 )
);
commit;


-- DROP TABLE IF EXISTS Resub_Master;
-- DROP TABLE IF EXISTS Resub_Diagnosis;
-- DROP TABLE IF EXISTS Resub_Activity;
-- DROP TABLE IF EXISTS Resub_Act_Observation;
-- DROP TABLE IF EXISTS Claim_File_Details;
-- DROP TABLE IF EXISTS Resub_Diagnosis;
-- DROP TABLE IF EXISTS Resub_Master;
-- DROP TABLE IF EXISTS Remittance_Activity;
-- DROP TABLE IF EXISTS Remittance_Master;
-- DROP TABLE IF EXISTS Claim_Act_Observation;
-- DROP TABLE IF EXISTS claim_activity;
-- DROP TABLE IF EXISTS Claim_Diagnosis;
-- DROP TABLE IF EXISTS Claim_Master;

-- ALTER TABLE claim_diagnosis ALTER COLUMN diagnosis_code TYPE VARCHAR( 250 )
-- ALTER TABLE claim_activity DROP COLUMN PatientShare;
-- ALTER TABLE claim_activity ALTER COLUMN priorauthorization_id TYPE VARCHAR( 250 )
-- ALTER TABLE claim_activity ALTER COLUMN priorauthorization_id DROP NOT NULL
-- ALTER TABLE Remittance_Master ALTER COLUMN Sender_ID TYPE VARCHAR( 250 )
-- ALTER TABLE Remittance_Master ALTER COLUMN EncounterFacility_ID TYPE VARCHAR( 250 )
-- ALTER TABLE Remittance_Activity ADD COLUMN Denial_Code VARCHAR ( 250 ) NOT NULL
-- ALTER TABLE Remittance_Activity ALTER COLUMN Denial_Code DROP NOT NULL
-- ALTER TABLE Remittance_Activity DROP COLUMN Remittance_ID



