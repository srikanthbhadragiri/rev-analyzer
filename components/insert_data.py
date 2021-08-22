def writeFileDetails(conn, header):
    print("In writeFileDetails")
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO claim_file_details ( "
            "File_Name, Claim_Type, "
            "Sender_ID, Receiver_ID, "
            "Submission_Date, Disposition_Flag, Claim_IDs, Record_Count) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (header['FileName'], header['ClaimType'],
             header['SenderID'], header['ReceiverID'],
             header['TransactionDate'], header['DispositionFlag'], header['Claims'], int(header['RecordCount'])))
        conn.commit


def writeClaimMaster(conn, claims, header):
    print("In writeClaimMaster")
    if conn:
        cursor = conn.cursor()

        for clm in claims:
            claim = clm["claim"]
            cursor.execute(
                " INSERT INTO Claim_Master ("
                "Claim_ID, Sender_ID, Receiver_ID, Submission_Date, "
                "ID_Payer, Member_ID, Payer_ID, Provider_ID, Emirates_IDNumber, "
                "Gross, PatientShare, Net, VAT, Enc_Facility_ID, "
                "Enc_Type, Enc_Patient_ID, Enc_Start_Time, Enc_End_Time, Enc_Start_Type, "
                "Enc_End_Type) "
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (claim["ClaimID"], header["SenderID"], header['ReceiverID'], header['TransactionDate'],
                 claim["IDPayer"], claim["MemberID"], claim["PayerID"], claim["ProviderID"], claim["EmiratesIDNumber"],
                 claim["Gross"], claim["PatientShare"], claim["Net"], claim["VAT"], claim["FacilityID"],
                 claim["FacilityType"], claim["PatientID"], claim["Start"], claim["End"], claim["StartType"],
                 claim["EndType"]))

        conn.commit


def writeClaimDiagnosis(conn, claims):
    if conn:
        cursor = conn.cursor()
        for clm in claims:
            diagnosis = clm["diagnosis"]
            for diag in diagnosis:
                cursor.execute(
                    "INSERT INTO Claim_Diagnosis ("
                    "Claim_ID, Diagnosis_Type, Diagnosis_Code) "
                    "VALUES (%s, %s, %s)",
                    (diag['ClaimID'], diag['Type'], diag['Code']))

        conn.commit


def writeClaimActivity(conn, claims):
    if conn:
        cursor = conn.cursor()
        for clm in claims:
            activity = clm["activity"]
            for acti in activity:
                cursor.execute(
                    "INSERT INTO Claim_Activity ("
                    "Activity_ID, Claim_ID, Act_Start_Time, Act_Type, Act_Code, "
                    "Act_Net, Act_Quantity, Ordering_Clinician, Clinician, "
                    "PriorAuthorization_ID, VAT, VAT_Percent) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (acti['ID'], acti['ClaimID'], acti['Start'], acti['Type'], acti['Code'],
                     acti['Net'], acti['Quantity'], acti['OrderingClinician'], acti['Clinician'],
                     acti['PriorAuthorizationID'], float(acti['VAT']), float(acti['VATPercent'])))
        conn.commit


def writeClaimActObs(conn, claims):
    if conn:
        cursor = conn.cursor()
        for clm in claims:
            activity = clm["activity"]
            for acti in activity:
                observations = acti["Observations"]
                for obs in observations:
                    # print(obs)
                    cursor.execute(
                        "INSERT INTO Claim_Act_Observation ("
                        "Activity_ID, Claim_ID, Obs_Type, Obs_Code, Obs_Value, Obs_ValueType) "
                        "VALUES (%s, %s, %s, %s, %s, %s)",
                        (obs['ID'], obs['ClaimID'], obs['Type'], obs['Code'], obs['Value'], obs['ValueType']))
        conn.commit


def writeResubMaster(conn, claims, header):
    print("In writeResubMaster")
    if conn:
        cursor = conn.cursor()

        for clm in claims:
            claim = clm["claim"]
            cursor.execute(
                " INSERT INTO Resub_Master ("
                "Claim_ID, Sender_ID, Receiver_ID, Submission_Date, "
                "ID_Payer, Member_ID, Payer_ID, Provider_ID, Emirates_IDNumber, "
                "Gross, PatientShare, Net, VAT, Enc_Facility_ID, "
                "Enc_Type, Enc_Patient_ID, Enc_Start_Time, Enc_End_Time, Enc_Start_Type, "
                "Enc_End_Type, Resub_Type, Resub_Comment) "
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (claim["ClaimID"], header["SenderID"], header['ReceiverID'], header['TransactionDate'],
                 claim["IDPayer"], claim["MemberID"], claim["PayerID"], claim["ProviderID"], claim["EmiratesIDNumber"],
                 claim["Gross"], claim["PatientShare"], claim["Net"], claim["VAT"], claim["FacilityID"],
                 claim["FacilityType"], claim["PatientID"], claim["Start"], claim["End"], claim["StartType"],
                 claim["EndType"], claim["ResubType"], claim["ResubComment"]))

        conn.commit

def writeRemitMaster(conn, claims, header):
    if conn:
        cursor = conn.cursor()

        for clm in claims:
            claim = clm["claim"]
            cursor.execute(
                " INSERT INTO Remittance_Master ("
                "Claim_ID, Sender_ID, Receiver_ID, Submission_Date, "
                "ID_Payer, Provider_ID, Payment_Reference, "
                "Date_Settlement, Enc_Facility_ID) "
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (claim["ClaimID"], header["SenderID"], header['ReceiverID'], header['TransactionDate'],
                 claim["IDPayer"], claim["ProviderID"], claim["PaymentReference"],
                 claim["DateSettlement"], claim["FacilityID"]))

        conn.commit


def writeRemitActivity(conn, claims):
    if conn:
        cursor = conn.cursor()
        for clm in claims:
            activity = clm["activity"]
            for acti in activity:
                cursor.execute(
                    "INSERT INTO Remittance_Activity ("
                    "Activity_ID, Claim_ID, Act_StartTime, Act_Type, Act_Code, "
                    "Act_Net, Act_Quantity, Ordering_Clinician, Clinician, "
                    "Payment_Amount, Denial_Code) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (acti['ID'], acti['ClaimID'], acti['Start'], acti['Type'], acti['Code'],
                     acti['Net'], acti['Quantity'], acti['OrderingClinician'], acti['Clinician'],
                     float(acti['PaymentAmount']), acti['DenialCode']))
        conn.commit
