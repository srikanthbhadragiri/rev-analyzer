# UI page with Browse button                                        DONE
# Browse one file (claim | remittance)
#  Processing steps for single file
#   --> Get File Names                                              DONE
#   --> System to check for filename if it exists in Claim_File_Details table,      DONE
#       --> if exists --> do not process,                                           DONE
#       --> else
#           --> if type is claim --> Process
#           --> if type is remit --> process only if claim exists in the DB


# Browse and select multiple files ( claim | remittance )           DONE
#   --> Keep the selected file names in a list.                     DONE
#   --> Process as above


import components.create_db as db
import components.process_xml as xd
import components.insert_data as ind
import components.validate_data as vd
import components.common as cm

from tkinter import *
from tkinter import filedialog

ws = Tk()
ws.title("Revenue Analyzer")
ws.geometry("1024x768")
ws['bg'] = '#fb0'

txtarea = Text(ws, width=120, height=20)
txtarea.pack(pady=20)
xmlFileNames = []
db_conn = cm.getDBConn()  # Get a successful DB connection Object


def createDBTables():
    # Create tables in database
    print('button clicked')
    if db_conn:
        print('in createDB TAbles')
        db.createTables(db_conn)
    else:
        print("DB tables not created!")


Button(
    ws,
    text="Create DB Tables",
    command=createDBTables
).pack(side=LEFT, expand=False, fill=X, padx=10)


def selectFiles():
    # clear xmlFileNames list
    xmlFileNames.clear()

    tf = filedialog.askopenfilenames(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.xml"),)
    )
    txtarea.insert(END, "--- List of Selected Files ---\n")
    for f in tf:
        tf = open(f)
        xmlFileNames.append(tf.name)
        data = tf.name[tf.name.rindex("/") + 1:]  # tf.name
        txtarea.insert(END, data)
        txtarea.insert(END, '\n')
        tf.close()

    txtarea.insert(END, '\n Total selected files ' + str(len(xmlFileNames)) + '\n')
    print('xmlFileNames : ', xmlFileNames)


Button(
    ws,
    text="Open File",
    command=selectFiles
).pack(side=LEFT, expand=False, fill=X, padx=20)


def getClaimType(data):
    for clm in data:
        # print(clm['claim']['ClaimType'])
        return clm['claim']['ClaimType']


def getProcessedClaimIds(data):
    print("getProcessedClaimIds ---- ")
    clm_list = []
    for clm in data:
        # print(clm['claim']['ClaimID'])
        clm_list.append(clm['claim']['ClaimID'])

    return clm_list


def processFiles():
    print("start processing files ", xmlFileNames)
    if len(xmlFileNames) > 0:
        print('ready to process')
        for file in xmlFileNames:
            # print(file)
            fileName = file[file.rindex("/") + 1:]
            print(fileName)
            exists = vd.ifFileNameExists(db_conn, fileName)
            print("RESULT ", exists)
            if not exists:
                print(fileName + ' - File can be processed...')
                # check for type of file
                claim_type = xd.getTypeofClaim(file)
                print("Claim Type ", claim_type)
                if claim_type == cm.CLAIM_SUBMISSION:
                    # Process Claims XML
                    clm_header = xd.getClaimHeaderData(file)
                    clm_data = xd.getClaimData(file)

                    # print(clm_header)
                    # print(clm_data)

                    claimIdList = getProcessedClaimIds(clm_data)
                    clm_header['ClaimType'] = getClaimType(clm_data)
                    # clm_header['Claims'] = claimIdList
                    clm_header['Claims'] = ",".join(claimIdList)
                    # clm_header['Claims'] = 'CLD115959', 'CLD115979', 'CLD115915', 'CLD115976', 'CLD115985', 'CLD115933'
                    print('claimIdList - ', claimIdList)
                    print('claimIdList header- ', clm_header['Claims'])

                    # Write Claims to DB
                    ind.writeFileDetails(db_conn, clm_header)

                    if clm_header['ClaimType'] == 'Resubmission':
                        print("This is of type Resubmission ---- ")
                        ind.writeResubMaster(db_conn, clm_data, clm_header)
                        txtarea.insert(END, '\n' + fileName + ' ReSubmit Claim written into DB Successfully...')
                    elif clm_header['ClaimType'] == 'Submission':
                        print("This is of type Submission ---- ")
                        ind.writeClaimMaster(db_conn, clm_data, clm_header)
                        ind.writeClaimDiagnosis(db_conn, clm_data)
                        ind.writeClaimActivity(db_conn, clm_data)
                        ind.writeClaimActObs(db_conn, clm_data)
                        txtarea.insert(END, '\n' + fileName + ' Claim written into DB Successfully...')

                elif claim_type == cm.REMITTANCE_ADVICE:
                    # Process Remittance XML
                    print('In Remittance -- ')
                    rmt_header = xd.getRemittanceHeaderData(file)
                    rmt_data = xd.getRemitData(file)

                    claimIdList = getProcessedClaimIds(rmt_data)
                    print(' final claim id list ', claimIdList)
                    rmt_header['Claims'] = ",".join(claimIdList)

                    # print(rmt_header)
                    # print(rmt_data)

                    # Write Remittance to DB
                    if len(claimIdList) > 0:
                        ind.writeFileDetails(db_conn, rmt_header)
                        ind.writeRemitMaster(db_conn, rmt_data, rmt_header)
                        ind.writeRemitActivity(db_conn, rmt_data)

                        txtarea.insert(END, '\n' + fileName + ' A total of ' + str(len(claimIdList)) + 'Remittance written into DB Successfully...')
                    else:
                        txtarea.insert(END, '\n' + fileName + ' Remittance Not written into DB')
            else:
                txtarea.insert(END, '\n' + fileName + ' already exists in DB ...')
                print(fileName + ' - File already processed ...')

        # clear xmlFileNames
        xmlFileNames.clear()

    else:
        txtarea.insert(END, '\n' + 'No Files Selected...')
        print('No Files Selected for processing')


Button(
    ws,
    text="Process Claim Files",
    command=processFiles
).pack(side=LEFT, expand=False, fill=X, padx=20)


def getA001():
    allClaims = vd.allA001ClaimsMarch(db_conn)
    print(type(allClaims))
    print(allClaims[0])
    print(allClaims[1])


Button(
    ws,
    text="March A001",
    command=getA001
).pack(side=LEFT, expand=False, fill=X, padx=20)


ws.mainloop()

# Process Remittance XML
# print(xd.remit_header_data)
# print(xd.remit_data)

# Write Remittance to DB
# ind.writeFileDetails(db_conn, xd.remit_header_data)
# ind.writeRemitMaster(db_conn, xd.remit_data, xd.remit_header_data)
# ind.writeRemitActivity(db_conn, xd.remit_data)


# for dlm in xd.claims_data:
#     print(dlm["activity"])

# for dlm in xd.claims_data:
#     print(dlm["diagnosis"])


# for clm in xd.claims_data:
#     # print(type(clm))
#     print(clm)
#     writeClaimMaster(conn, clm["claim"])
#     # print(clm["claim"]["ClaimID"])
