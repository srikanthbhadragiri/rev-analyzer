# Read / Parse XML files from directory 'xml'.
# 1. Read the Header, get the xml file name, store it in a dict (for key value pair)
# 2. Check for new file name if it exists in claim_file_details, if exists then donot process the file, go to next file from the list.

import xml.etree.ElementTree as ET
import pandas as pd
import psycopg2
import time
import datetime

fileName = "MF1397_A001_2021-03-31_IS015009.xml";

fileNames = ["MF1397_A001_2021-03-31_IS015009.xml", "MF1397_A001_2021-03-31_IS015008.xml",
             "MF1397_A001_2021-03-31_IS015007.xml", "MF1397_A001_2021-03-31_IS015006.xml"]

tree = ET.parse('../xml/MF1397_A001_2021-03-31_IS015009.xml')
root = tree.getroot()

# c = ET.SubElement(a, 'nested-node 2')
# d = ET.SubElement(c, 'innermost node')


def establishConn():
    return psycopg2.connect(
        database="MoviesDB", user='postgres', password='root', host='127.0.0.1', port='5432'
    )


def verifyConnection(conn):
    if conn:
        cursor = conn.cursor()
        cursor.execute("select version()")
        data = cursor.fetchone()
        print("Connection established to: ", data)


header_dict = {"FileName": fileName}


def writeFileDetails(conn, header_dict):
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO claim_file_details (File_Name, Claim_Type, Sender_ID, Receiver_ID, Submission_Date, Disposition_Flag) VALUES (%s, %s, %s, %s, %s, %s)",
            (header_dict['FileName'], "claim", header_dict['SenderID'], header_dict['ReceiverID'],
             header_dict['TransactionDate'], header_dict['DispositionFlag']))
        conn.commit


# cursor.execute("INSERT INTO claim_file_details (File_Name, ClaimType) VALUES ('MF1397_A001_2021-03-31_IS015009.xml', 'claim')")

def writeFileClaim(conn, cla_df):
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            " INSERT INTO Claim_Master(Claim_ID,Sender_ID,Receiver_ID,Submission_Date,ID_Payer,Member_ID,Payer_ID,Provider_ID,Emirates_IDNumber,"
            "Gross,PatientShare,Net,VAT,Enc_Facility_ID,Enc_Type,Enc_Patient_ID,Enc_Start_Time,Enc_End_Time,Enc_Start_Type,Enc_End_Type) VALUES(%s)",
            (cla_df['ID']))
        conn.commit


def retriveData(conn, table_name):
    if conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM %s " % table_name)

        # Fetching 1st row from the table
        result = cursor.fetchall();
        print(result)


# Read Header


def read_header():
    for header in root.iter('Header'):
        for element in header:
            if element.tag == 'TransactionDate':
                print(element.text)
                # timeValue = datetime.datetime.strptime(element.text, "%d/%m/%Y %I:%M")
                timeValue = datetime.datetime.strptime(element.text, "%d/%m/%Y %H:%M")
                # % d - % b - % Y - % H: % M: % S
                print('timeValue ', timeValue)
                # timeValue.strftime("YYYYMMDD HH:mm:ss (%Y%m%d %H:%M:%S)")
                # print('timeValue ', timeValue)
                timestamp = time.mktime(timeValue.timetuple())
                print("timestamp ", timestamp)
                # 31/03/2021 10:20
                # 20210331 10:20
                # header_dict[element.tag] = "20210331 10:20"  # timestamp
                header_dict[element.tag] = timeValue #"2021-03-31 10:20:00"  # timestamp
            else:
                header_dict[element.tag] = element.text


# execution of this file
read_header()
print(str(header_dict))


def Read_Claim(Claim):
    for cla in root.iter('Claim'):
        cla_dict = cla.attrib.copy()
        # print(type(mov_dict), mov_dict)
        cla_dict.update(cla.attrib)
        cla_dict["SenderID"] = header_dict["SenderID"]
        cla_dict["ReceiverID"] = header_dict["ReceiverID"]
        cla_dict["TransactionDate"] = "20210331 10:20"
        for feature in cla:
            if feature.tag != "Diagnosis" and feature.tag != "Activity" and feature.tag != "Encounter":
                cla_dict[feature.tag] = feature.text

        yield cla_dict
        # print(cla_dict)


cla_df = pd.DataFrame(list(Read_Claim(root.iter('Claim'))))
print(cla_df)

#
# read_claim()
# print(claim_dict)

# Write to Database
conn = establishConn()
verifyConnection(conn)
writeFileDetails(conn, header_dict)
conn.commit();
# retriveData(conn, 'claim_file_details')
# writeFileClaim(conn,cla_df)


# Read Claim

# def iter_movie(Claim):
#     for mov in root.iter('Claim'):
#         mov_dict = mov.attrib.copy()
#         # print(type(mov_dict), mov_dict)
#         mov_dict.update(mov.attrib)
#         for feature in mov:
#             mov_dict[feature.tag] = feature.text
#         print(mov_dict)
#         yield mov_dict
#
# mov_df = pd.DataFrame(list(iter_movie(root.iter('Claim'))))
# print(mov_df)
